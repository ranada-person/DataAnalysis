import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# File: DataAnalysis.py
# Author: Ranada Person
# Due Date: 6.23.2020
# Purpose: Week 5 Lab - Allows user to pick between 2 files and perform histogram analysis
# and plots for select variables on the datasets


def file_selection():
    # Function to display menu options for selecting a file
    # List of Menu Options
    print('Select the file you want to analyze:')
    print('1. Population Data')
    print('2. Housing Data')
    print('3. Exit the Program')
    # Try/Catch to ensure valid menu option is picked
    valid_option = False
    while not valid_option:
        try:
            user_file = int(input())
            return user_file
            valid_option = True
        except ValueError:
            print('Please enter a valid menu option: ')


def pop_data_menu():
    # Function to display menu options for the population data file
    # List of Menu Options
    print('Select the Column you want to analyze: ')
    print('1. Pop Apr 1 ')
    print('2. Pop Jul 1 ')
    print('3. Change Pop ')
    print('4. Exit Column ')
    # Try/Catch to ensure valid menu option is picked
    valid_option = False
    while not valid_option:
        try:
            selection = int(input())
            return selection
            valid_option = True
        except ValueError:
            print('Please enter a valid menu option: ')


def housing_data_menu():
    # Function to display menu options for the housing data file
    # List of Menu Options
    print('Select the Column you want to analyze: ')
    print('1. Age ')
    print('2. Bedrooms ')
    print('3. Built ')
    print('4. Rooms ')
    print('5. Utility ')
    print('6. Exit Column')
    # Try/Catch to ensure valid menu option is picked
    valid_option = False
    while not valid_option:
        try:
            selection = int(input())
            return selection
        except ValueError:
            print('Please enter a valid menu option: ')


def get_statistics(column):
    # Function to get and print statistics for chosen column
    column = column
    print('The statistics for this column are:')
    count = column.shape[0]
    print('Count: ', count)
    mean = np.mean(column)
    print('Mean: ', mean)
    standard_deviation = np.std(column)
    print('Standard Deviation: ', standard_deviation)
    minimum = min(column)
    print('Minimum: ', minimum)
    maximum = max(column)
    print('Maximum: ', maximum)


def get_histogram(column):
    # Function that creates and saves histogram
    column = column
    print('The Histogram of this column can be downloaded now.')
    print()
    # Histogram of the data
    n, bins, patches = plt.hist(column, 20, density=True, facecolor='b',
                                alpha=0.75)
    plt.grid(True)
    # Assign to a figure
    fig1 = plt
    return fig1


# Start of the main application
print('*********** Welcome to the Python Data Analysis Application ***********')
while True:
    file = file_selection()
    if file == 1:
        print('You selected Population Data')
        # Read Population Data file
        population_df = pd.read_csv('PopChange.csv')
        # Run the pop_data_menu function to determine what the user wants to do
        pop_selection = pop_data_menu()

        if pop_selection == 1:
            print('You selected Pop Apr 1')
            column_choice = population_df['Pop Apr 1']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('PopApr1.svg')
        elif pop_selection == 2:
            print('You selected Pop Jul 1 ')
            column_choice = population_df['Pop Jul 1']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('PopJul1.svg')
        elif pop_selection == 3:
            print('You selected Change Pop ')
            column_choice = population_df['Change Pop']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('ChangePop.svg')
        elif pop_selection == 4:
            print('You selected Exit Column ')
            print()
    elif file == 2:
        print('You have selected Housing Data')
        housing_df = pd.read_csv('Housing.csv')
        # Run the housing_data_menu function to determine what the user wants to do
        housing_selection = housing_data_menu()

        if housing_selection == 1:
            print('You selected Age ')
            column_choice = housing_df['AGE']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('HousingAGE.svg')
        elif housing_selection == 2:
            print('You selected Bedrooms ')
            column_choice = housing_df['BEDRMS']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('HousingBEDRMS.svg')
        elif housing_selection == 3:
            print('You selected Built ')
            column_choice = housing_df['BUILT']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('HousingBUILT.svg')
        elif housing_selection == 4:
            print('You selected Rooms ')
            column_choice = housing_df['ROOMS']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('HousingROOMS.svg')
        elif housing_selection == 5:
            print('You selected Utility ')
            column_choice = housing_df['UTILITY']
            get_statistics(column_choice)
            fig = get_histogram(column_choice)
            # Save Figure for Download
            fig.savefig('HousingUTILITY.svg')
        elif housing_selection == 6:
            print('You selected Exit Column ')
            print()
    elif file == 3:
        print("Goodbye!")
        sys.exit()
    else:
        print('Enter a menu option')


