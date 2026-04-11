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
def compute_statistics(data, grouped_df,)
   if data is None or grouped_df is None:
        return

    # Calculating central tendency and dispersion
   results = {
        "Mean": statistics.mean(data),
        "Median": statistics.median(data),
        "Variance": statistics.variance(data) if len(data) > 1 else 0,
        "Standard Deviation": statistics.stdev(data) if len(data) > 1 else 0
    }
# Handling the Mode
try:
 mode_val = statistics.mode(data)
except statistics.StatisticsError:
 mode_val = "Multiple modes found"

# Finding the Modal Class from the frequency table
 modal_class = grouped_df.loc[grouped_df['Frequency'].idxmax(), 'Class Range']

# Displaying results in a clear tabular format
print("\n" + "="*40)
print("      STATISTICAL ANALYSIS REPORT")
print("="*40)
for key, value in results.items():
    print(f"{key:20}: {value:.2f}")
   
    print(f"{'Mode':20}: {mode_val}")
    print(f"{'Modal Class':20}: {modal_class}")
    print("-" * 40)
    print("\n--- Frequency Distribution Table ---")
    print(grouped_df)
    
    # Saving analysis results to a new CSV file
    grouped_df.to_csv("frequency_results.csv", index=False)
    print("\nFrequency table has been saved to 'frequency_results.csv'.")

#Draw a histogram from grouped data using Matplotlib
def draw_histogram(data):
   if data is None:
        return
    
    # Data Visualisation
plt.figure(figsize=(10, 6))
plt.hist(data, bins='auto', color='royalblue', edgecolor='black', alpha=0.8)
plt.title("Histogram of Student Grade Distribution", fontsize=14)
plt.xlabel("Grades", fontsize=12)
plt.ylabel("Frequency (Number of Students)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
#Main method to run the program
def main():
#upload the data
  while True:
        menu = "\n***** Student Analytics Application *****\n"
        menu += "1. Input and Save Student Grades\n"
        menu += "2. View Statistics and Frequency Table\n"
        menu += "3. Generate Histogram Visualisation\n"
        menu += "4. Exit"
        print(menu)
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            get_user_data()
        elif choice == "2":
            raw_data, freq_df = read_data()
            if raw_data is not None:
                compute_statistics(raw_data, freq_df)
        elif choice == "3":
            raw_data, _ = read_data()
            if raw_data is not None:
                draw_histogram(raw_data)
        elif choice == "4":
            print("Exiting program. Have a nice day!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()


    
