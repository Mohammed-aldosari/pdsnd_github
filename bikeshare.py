import time
import pandas as pd
import numpy as np
# Creating dictionary for (chicago, new york city, washington)
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHi.. Let\'s get your specific inputs for the bikeshare data you want to analyze:')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nSelect the name of the city as written below: \n1- chicago\n2- new york city\n3- washington\nType your answer here: ")
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            print("\nwrong input try again: ")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nNow select the month as written below: \n1- january \n2- february \n3- march \n4- april \n5- may \n6- june \n7- all\nType your answer here: ")
        if (month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            print("\nwrong input try again: ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nNow select the day as written below: \n1- monday \n2- tuesday \n3- wednesday \n4- thursday \n5- friday \n6- saturday \n7- sunday \n8- all\nType your answer here:  ")
        if (day == 'monday' or day == 'tuesday'  or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            print("\nwrong input try again: ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nMost common month: ',most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nMost common day: ',most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('\nMost common hour: ',most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station: ',most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station: ',most_commonly_used_end_station)


    # display most frequent combination of start station and end station trip
    combination_of_start_station_and_end_station_trip = df['Start Station'] + ' and ' +df['End Station']
    df['combination_of_start_station_and_end_station_trip'] = combination_of_start_station_and_end_station_trip
    frequent_combination_of_start_station_and_end_station_trip = df['combination_of_start_station_and_end_station_trip'].mode()[0]
    print('\nMost frequent combination of start station and end station trip: ',frequent_combination_of_start_station_and_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
    #    trip_duration_stats(df)
    #    user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
