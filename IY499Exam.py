'''
Programmer: Emir Delipinar
Date: 2026

'''

import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt
import statistics

#Get data and save into csv file using Pandas
def get_user_data():
    print("Data saved")
#Read numerical data from csv file using Pandas
def read_data():
    print("Data was loaded.")
#Compute mean, median, mode, modal class, variance, Standard Deviation using statistics
def compute_statistics(data, grouped_df, frequency, midpoint):
    print("Display all Statistics.")
#Draw a histogram from grouped data using Matplotlib
def draw_histogram(grouped_df):
    print("**** Histogram ****")
#Main method to run the program
def main():
#upload the data
   while True:
    menu += "\n***** Grouped Data Application *****\n"
    menu += "\n1. Add and save data"
    menu += "\n2. Show Statistics"
    menu += "\n3. Draw Histogram"
    menu += "\n4.Exit"
    print(menu)
    choice = input("Enter your choice(1-6):")

    if choice == "1":
        get_user_data()
    elif choice =="2":
        read_data()
        compute_statistics("data","grouped_df","frequency","midpoint")
    elif choice == "3":
        draw_histogram("grouped_df")
    elif choice == "4":
        print("Good bye")
        break
    else:
        print("Invalid option. Please Try again.")

    if __name__=="__main__":
        main()


    
