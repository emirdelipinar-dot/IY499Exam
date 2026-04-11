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
    print("\n--- Student Grade Entry System ---")
    grade_list = []
    
    while True:
        user_input = input("Enter a student grade (0-100) or 'q' to save and finish: ")
        
        if user_input.lower() == 'q':
            break
        try:
            # Converting input to float (Continuous numerical data)
            grade = float(user_input)
            if 0 <= grade <= 100:
                grade_list.append(grade)
            else:
                print("Error: Grade must be between 0 and 100.")
        except ValueError:
            # Error Recovery: Handles non-numeric inputs
            print("Invalid input! Please enter a numerical value (e.g., 75.5).")

if grade_list:
        # Saving data to a CSV file
    df = pd.DataFrame(grade_list, columns=["Grades"])
    df.to_csv("student_grades.csv", index=False)
    print(f"Success: {len(grade_list)} records saved to 'student_grades.csv'.")
else:
    print("No data was entered. File not updated.")
        
#Read numerical data from csv file using Pandas
def read_data():
   try:
        # File Access: Reading from the CSV
        df = pd.read_csv("student_grades.csv")
        raw_grades = df["Grades"].tolist()
        
        # Requirement: Application of a Sorting Algorithm
        # We sort the data in ascending order before processing
        raw_grades.sort()
        
        # User specifies class width for binning (Grouping)
        width_input = input("Enter the class width for grouping data (e.g., 10): ")
        class_width = float(width_input)
# Creating Bins using NumPy
        bins = np.arange(0, 100 + class_width, class_width)
        
        # Binning the data into categories
        df['Class_Range'] = pd.cut(df['Grades'], bins=bins)
        
        # Creating a Frequency Distribution Table
        freq_table = df['Class_Range'].value_counts().sort_index().reset_index()
        freq_table.columns = ['Class Range', 'Frequency']
        
        # Calculating Midpoints for each class
        freq_table['Midpoint'] = freq_table['Class Range'].apply(lambda x: x.mid)
        
        return raw_grades, freq_table
   except FileNotFoundError:
        # Error Recovery: Handles missing files without using 'os'
        print("\nError: 'student_grades.csv' not found. Please add data first (Option 1).")
        return None, None
   except ValueError:
        print("\nError: Invalid class width entered.")
        return None, None
   except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None, None

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


    
