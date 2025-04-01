import pandas as pd 
import numpy as np 
import os 
def calculate_demographic_data(print_data=True):
# Correct the filepath to point to the CSV file, not the Python script
    filepath = os.path.join( "Demographic Data Analyzer", "adult.data.csv.csv")

    # Read the CSV file
    df = pd.read_csv(filepath)

    # Print first few rows and column names
    print(df.head())
    print("Column names:")
    print(df.columns.tolist())
    race_count=pd.Series(df[' race'].value_counts())
    print(race_count)

    # What is the average age of men?
    # Fix 'Male' to match exactly how it appears in the data
    # Also add space to 'age' if needed
    average_men = round(df[df[' sex'] == ' Male']['age'].mean(), 1)
    # print(average_men)

    # What is the percentage of people who have a Bachelor's degree?
    # Fix the space before Bachelors
    bachelors_percentage = round((len(df[df[' education'] == ' Bachelors'])/len(df[' education']))* 100, 1)
    # print(bachelors_percentage)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = len(df[((df[' education'] == ' Bachelors')|
                              (df[' education'] == ' Masters') | 
                              (df[' education'] == ' Doctorate'))])
    lower_education = len(df[((df[' education']  != ' Bachelors' ) &
                             (df[' education'] != ' Masters') & 
                             (df[' education'] !=' Doctorate'))])

    higher_education_above_50k = len(df[((df[' education'] == ' Bachelors') | 
                                       (df[' education'] == ' Masters') | 
                                       (df[' education'] == ' Doctorate')) &
                                        (df[' income'] == ' >50K')])
    lower_education_above_50k = len(df[~((df[' education']  == ' Bachelors' ) &
                                       (df[' education'] == ' Masters') & 
                                       (df[' education'] == ' Doctorate')) &
                                       (df[' income'] == ' >50K')])

    higher_education_rich=round((higher_education_above_50k/higher_education)* 100, 1)
    lower_education_rich=round((lower_education_above_50k/lower_education)* 100, 1)
    # print(higher_education_rich,lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df[' hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df[' hours-per-week'] == min_work_hours])  # Changed from 1 to min_work_hours
    num_min_workers_rich = len(df[(df[' hours-per-week'] == min_work_hours) & (df[' income'] == ' >50K')])
    
    # Avoid division by zero by checking if num_min_workers is not zero
    rich_per = round((num_min_workers_rich / num_min_workers) * 100, 1) if num_min_workers > 0 else 0

    # What country has the highest percentage of people that earn >50K?
    df1 = round((df[(df[' income'] == ' >50K')][' native-country'].value_counts()/df[' native-country'].value_counts()) *100 ,1)
    df1 = df1.sort_values(ascending=False)
    highest_earning_country = df1.index[0]
    highest_earning_country_percentage = df1[0]

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df[' income'] == ' >50K') & (df[' native-country'] == ' India')]
    top_IN_occupation = india_rich[' occupation'].value_counts().index[0] if not india_rich.empty else 'No data'


    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_men)
        print(f"Percentage with Bachelors degrees: {bachelors_percentage}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_per}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
            'race_count': race_count,
            'average_age_men': average_men,
            'percentage_bachelors': bachelors_percentage,
            'higher_education_rich': higher_education_rich,
            'lower_education_rich': lower_education_rich,
            'min_work_hours': min_work_hours,
            'rich_percentage': rich_per,
            'highest_earning_country': highest_earning_country,
            'highest_earning_country_percentage':
            highest_earning_country_percentage,
            'top_IN_occupation': top_IN_occupation
        }

# Add this line to call the function
calculate_demographic_data()
