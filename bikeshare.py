import time
import pandas as pd
import numpy as np

"""Loading raw data"""

def load_data():
    
    chicago_data = pd.read_csv('chicago.csv')
    new_york_data = pd.read_csv('new_york_city.csv')
    washington_data = pd.read_csv('washington.csv')
    return chicago_data, new_york_data, washington_data

def show_raw_data(df):
    start_row = 0
    while True:
       
        show_data = input("Would you like to see 5 rows of raw data? (yes/no): ").strip().lower()
        if show_data != 'yes':
            break

       
        print(df.iloc[start_row:start_row + 5])
        start_row += 5

        
        if start_row >= len(df):
            print("No more data to display.")
            break


def popular_times(city_data, city_name):
   
    city_data['Start Time'] = pd.to_datetime(city_data['Start Time'])
    city_data['Month'] = city_data['Start Time'].dt.month
    city_data['Day'] = city_data['Start Time'].dt.day_name()
    city_data['Hour'] = city_data['Start Time'].dt.hour

    top_5_months = city_data['Month'].value_counts().nlargest(5).index.tolist()
    top_5_days = city_data['Day'].value_counts().nlargest(5).index.tolist()
    top_5_hours = city_data['Hour'].value_counts().nlargest(5).index.tolist()

    return top_5_months, top_5_days, top_5_hours

def interactive_popular_times(city_data, city_name):

    top_5_months, top_5_days, top_5_hours = popular_times(city_data, city_name)


    while True:
        try:
            user_month = int(input("Which month would you like to travel in? (1-12): "))
            if user_month < 1 or user_month > 12:
                print("Please enter a valid month (1-12)!")
                continue
            break
        except ValueError:
            print("Please enter a number!")

    user_day = input("Which day would you like to travel? (e.g., Monday, Tuesday, ...): ").strip().capitalize()

    while True:
        try:
            user_hour = int(input("Which time of the day would you like to travel? (Enter hour in 0-23 format): "))
            if user_hour < 0 or user_hour > 23:
                print("Please enter a valid hour (0-23)!")
                continue
            break
        except ValueError:
            print("Please enter a number!")


    month_status = "very crowded" if user_month in top_5_months else "not very crowded"
    day_status = "many people are traveling" if user_day in top_5_days else "fewer people are traveling"
    hour_status = "very crowded" if user_hour in top_5_hours else "not very crowded"

    print(f"In {city_name}, the month you selected ({user_month}) is {month_status}, "
          f"but on the day you chose ({user_day}), on average {day_status}, "
          f"and at {user_hour}:00, it is {hour_status}.")

def station_stats(city_data, city_name):

    popular_start_station = city_data['Start Station'].mode()[0]
    popular_end_station = city_data['End Station'].mode()[0]
    city_data['Trip'] = city_data['Start Station'] + " -> " + city_data['End Station']
    popular_trip = city_data['Trip'].mode()[0]

    print(f"In {city_name}, the most common start station is {popular_start_station}.")
    print(f"The most common end station is {popular_end_station}.")
    print(f"The most common trip is from {popular_trip}.")

def travel_time_stats(city_data, city_name):
 
    total_travel_time = city_data['Trip Duration'].sum()
    average_travel_time = city_data['Trip Duration'].mean()

    print(f"In {city_name}, the total travel time is {total_travel_time} seconds.")
    print(f"The average travel time is {average_travel_time:.2f} seconds.")

def user_stats(city_data, city_name):

    user_types = city_data['User Type'].value_counts()
    print(f"\n{city_name.title()} user types:\n{user_types}")

    if 'Gender' in city_data.columns:
        gender_count = city_data['Gender'].value_counts(dropna=True)
        print(f"\n{city_name.title()} gender count:\n{gender_count}")
    else:
        print(f"\n{city_name.title()} does not have gender data available.")

    if 'Birth Year' in city_data.columns:
        earliest_birth_year = city_data['Birth Year'].min()
        most_recent_birth_year = city_data['Birth Year'].max()
        most_common_birth_year = city_data['Birth Year'].mode()[0]
        print(f"\n{city_name.title()} birth year statistics:")
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print(f"\n{city_name.title()} does not have birth year data available."
              
def display_data(df):
   
    start_loc = 0
    while True:
        show_data = input("Would you like to see 5 rows of raw data? (yes/no): ").strip().lower()
        
        if show_data != 'yes':
            print("Exiting data display.")
            break
        
        print(df.iloc[start_loc:start_loc + 5])
        
        start_loc += 5

        if start_loc >= len(df):
            print("No more data to display.")
            break


def main():

    chicago_data, new_york_data, washington_data = load_data()

    while True:
        city = input("Which city would you like to know about? (chicago, new york, washington): ").strip().lower()

        if city == "chicago":
            data = chicago_data
            city_name = "Chicago"
        elif city == "new york":
            data = new_york_data
            city_name = "New York"
        elif city == "washington":
            data = washington_data
            city_name = "Washington"
        else:
            print("Invalid city! Please enter either 'chicago', 'new york', or 'washington'.")
            continue
        break

    display_data(data)


    print("What would you like to know?")
    print("1. Popular travel times")
    print("2. Station statistics")
    print("3. Travel time statistics")
    print("4. User statistics")
    choice = input("Please enter the number of the analysis you want (1-4): ")

    if choice == "1":
        interactive_popular_times(data, city_name)
    elif choice == "2":
        station_stats(data, city_name)
    elif choice == "3":
        travel_time_stats(data, city_name)
    elif choice == "4":
        user_stats(data, city_name)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()