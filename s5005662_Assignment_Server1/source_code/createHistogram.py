import os
from matplotlib import pyplot as mpl
import numpy as nmpy


def create_histogram():  # Creating a histogram of data using the data.txt
    y = nmpy.genfromtxt('received_files/data.txt')
    mpl.hist(y, 50, normed=1, facecolor="y", edgecolor="g")  # Cosmetic changes to the histogram
    mpl.xlabel("X-axis")  # Labelling the axis
    mpl.ylabel("Y-axis")  # ^
    mpl.title("Histogram of data.txt")  # Titling the histogram
    mpl.grid(True)  # Showing a grid to make reading the histogram easier
    mpl.show()