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


class uploaded_data:

    def __init__(self, username, filepath, title = None, x_label = None, y_label = None, fit = None):
        self.username = username
        self.filepath = filepath
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.fit = fit

    x_values = []
    y_values = []

    def read_file(self):
        if self.filepath.endswith((".txt")):
            with open(self.filepath,'r') as f:
                reader = csv.reader(f,delimiter='\t')
                for row in reader:
                    self.x_values.append(int(float(row[0])))
                    self.y_values.append(int(float(row[1])))

        if self.filepath.endswith((".csv")):
            with open(self.filepath,'r') as f:
                reader = csv.reader(f,delimiter=',')
                for row in reader:
                    self.x_values.append(int(float(row[0])))
                    self.y_values.append(int(float(row[1]))) 

        if self.filepath.endswith((".xlsx")) or self.filepath.endswith((".XLSX")):
            df = pd.read_excel(self.filepath, header = None)
            self.x_values = df[0].tolist()
            self.y_values = df[1].tolist()
    
    fig = plt.figure()
    ax = fig.add_subplot()

    def make_fit(self):
        x = np.linspace(np.amin(self.x_values), np.amax(self.x_values), 500)

        if self.fit == 'linear':
            param = np.polyfit(self.x_values, self.y_values, 1)
            self.ax.plot(x, np.poly1d(param)(x), label=r"$linear fit$", color="green", linewidth="1")

        if self.fit == 'quadratic':
            param = np.polyfit(self.x_values, self.y_values, 2)
            self.ax.plot(x, np.poly1d(param)(x), label=r"$quadratic fit$", color="green", linewidth="1")

        if self.fit == 'cubic':
            param = np.polyfit(self.x_values, self.y_values, 3)
            self.ax.plot(x, np.poly1d(param)(x), label=r"$cubic fit$", color="green", linewidth="1")

        if self.fit == 'exponential':
            param, cov = curve_fit(exponential_fit, self.x_values, self.y_values) 
            self.ax.plot(x, exponential_fit(x, param[0], param[1], param[2]) , label=r"exponential fit", color="green", linewidth="1")    

        if self.fit == 'logarithmic':
            param, cov = curve_fit(logarithmic_fit, self.x_values, self.y_values) 
            self.ax.plot(x, exponential_fit(x, param[0], param[1], param[2]) , label=r"logarithmic fit", color="green", linewidth="1") 


    def make_and_save_graph(self):
        self.fig.suptitle(self.title, fontweight="bold")
        self.ax.scatter(self.x_values, self.y_values, s=20, label="Data", color="red")
        self.ax.set_ylabel(self.y_label)
        self.ax.set_xlabel(self.x_label) 
        self.ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))  # sci notation za osi
        self.ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))  # sci notation za osi
        self.ax.grid(linewidth=0.5)
        self.ax.legend()

        if not os.path.exists(os.path.join(os.getcwd(),'..', "graphs_made", self.username)):
            os.makedirs(os.path.join(os.getcwd(),'..', "graphs_made", self.username))

        plt.savefig(os.path.splitext(os.path.join(os.getcwd(),'..', "graphs_made", self.username , os.path.basename(self.filepath)))[0])


"""
print(param)
print(cov)
print(np.sqrt(np.diag(cov)))
"""
#shranit graf
#imet shranjeno samo .txt


      