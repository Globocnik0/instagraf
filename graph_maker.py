from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math as m
from scipy.optimize import curve_fit
import csv
import os



def exponential_fit(x,a,b,c):
    return a * np.exp(-b*x) + c

def logarithmic_fit(x,a,b,c):
    return a * np.log(b*x) + c

def make_graph(username, filename, tittle = None, x_label = 'x axis', y_label = None, fit = None):

    x_values = []
    y_values = []


    # if filename.endswith((".csv")):
    #     with open(filename,'r') as f:
    #         reader = csv.reader(f,delimiter=',')
    #         for row in reader:
    #             x_values.append(int(float(row[0])))
    #             y_values.append(int(float(row[1]))) 

    if filename.endswith((".txt")):
        df = pd.read_csv(filename, header = None, delimiter='\t')
        x_values = df[0].tolist()
        y_values = df[1].tolist()

    elif filename.endswith((".csv")):
        df = pd.read_csv(filename, header = None, delimiter=';') #Delimiter je lahko tudi ','
        x_values = df[0].tolist()
        y_values = df[1].tolist()

    elif filename.endswith((".xlsx")) or filename.endswith((".XLSX")):
        df = pd.read_excel(filename, header = None)
        x_values = df[0].tolist()
        y_values = df[1].tolist()

 

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle(tittle,
                fontweight="bold")

    x = np.linspace(np.amin(x_values), np.amax(x_values), 500)

    if fit == 'linear':
        param = np.polyfit(x_values, y_values, 1)
        fitf = np.poly1d(param)
        fit_label = r"$linear fit$"

    elif fit == 'quadratic':
        param = np.polyfit(x_values, y_values, 2)
        fitf = np.poly1d(param)
        fit_label = r"$quadratic fit$"

    elif fit == 'cubic':
        param = np.polyfit(x_values, y_values, 3)
        fitf = np.poly1d(param)
        fit_label = r"$cubic fit$"

    elif fit == 'exponential':
        param, cov = curve_fit(exponential_fit, x_values, y_values) 
        fitf = lambda x: exponential_fit(x, param[0], param[1], param[2])
        fit_label = r"exponential fit"  

    elif fit == 'logarithmic':
        param, cov = curve_fit(logarithmic_fit, x_values, y_values) 
        fitf = lambda x: logarithmic_fit(x, param[0], param[1], param[2])
        fit_label = r"logarithmic fit" 
    
    if not fit == 'None': 
        ax.plot(x, fitf(x), label=fit_label, color="green", linewidth="1") #plot fit function
        
    ax.scatter(x_values, y_values, s=20, label="Data", color="red")
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label) 
    ax.ticklabel_format(axis="x", style="sci",
                        scilimits=(0, 0))  # sci notation za osi
    ax.ticklabel_format(axis="y", style="sci",
                        scilimits=(0, 0))  # sci notation za osi
    ax.grid(linewidth=0.5)
    ax.legend()

    if not os.path.exists(os.path.join(os.getcwd(), "database", "graphs_made", username)):
        os.makedirs(os.path.join(os.getcwd(), "database", "graphs_made", username))

    plt.savefig(os.path.splitext(os.path.join(os.getcwd(), "database", "graphs_made", username , os.path.basename(filename)))[0])



"""
print(param)
print(cov)
print(np.sqrt(np.diag(cov)))
"""
#shranit graf


      