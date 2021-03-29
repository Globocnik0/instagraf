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

def make_graph(filename, tittle = None, x_label = None, y_label = None, fit = None):

    x_values = []
    y_values = []

    if filename.endswith((".txt")):
        with open(filename,'r') as f:
            reader = csv.reader(f,delimiter='\t')
            for row in reader:
                x_values.append(int(float(row[0])))
                y_values.append(int(float(row[1])))

    if filename.endswith((".csv")):
        with open(filename,'r') as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                x_values.append(int(float(row[0])))
                y_values.append(int(float(row[1]))) 

    if filename.endswith((".xlsx")) or filename.endswith((".XLSX")):
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
        ax.plot(x, np.poly1d(param)(x), label=r"$linear fit$", color="green", linewidth="1")

    if fit == 'quadratic':
        param = np.polyfit(x_values, y_values, 2)
        ax.plot(x, np.poly1d(param)(x), label=r"$quadratic fit$", color="green", linewidth="1")

    if fit == 'cubic':
        param = np.polyfit(x_values, y_values, 3)
        ax.plot(x, np.poly1d(param)(x), label=r"$cubic fit$", color="green", linewidth="1")

    if fit == 'exponential':
        param, cov = curve_fit(exponential_fit, x_values, y_values) 
        ax.plot(x, exponential_fit(x, param[0], param[1], param[2]) , label=r"exponential fit", color="green", linewidth="1")    

    if fit == 'logarithmic':
        param, cov = curve_fit(logarithmic_fit, x_values, y_values) 
        ax.plot(x, exponential_fit(x, param[0], param[1], param[2]) , label=r"logarithmic fit", color="green", linewidth="1")    
    

    ax.scatter(x_values, y_values, s=20, label="Data", color="red")
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label) 
    ax.ticklabel_format(axis="x", style="sci",
                        scilimits=(0, 0))  # sci notation za osi
    ax.ticklabel_format(axis="y", style="sci",
                        scilimits=(0, 0))  # sci notation za osi
    ax.grid(linewidth=0.5)
    ax.legend()
    plt.savefig(os.path.splitext(os.path.join(os.getcwd(),'..', "graphs_made", os.path.basename(filename)))[0])



"""
print(param)
print(cov)
print(np.sqrt(np.diag(cov)))
"""

      