import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
         city=input('Please enter the city: ').lower()    
         if city not in CITY_DATA:
            print('Please enter city from chicago, new york city, washington')
         else:
             break

    MONTH_DATA=['january','february','march','april','may','june','all']
    while True:
        month=input('Please enter the month: ').lower()
        if month not in MONTH_DATA:
            print('Please enter month from january, february, march,april,may,june,all')
        else:
            break

    DAY_DATA=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day=input('Please enter the day: ').lower()
        if day not in DAY_DATA:
            print('Enter the day from monday,tuesday,wednesday,thursday,friday,saturday,sunday,all') 
        else:
            break

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
    df=pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    start_time = time.time()
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    df['Start Time'] =pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('most_common_month: ',common_month)

    df['day']=df['Start Time'].dt.day
    common_day = df['day'].mode()[0]
    print('most_common_day: ',common_day)

    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('most_common_hour: ',common_hour)
    
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
   
    common_start_station=df['Start Station'].mode()[0]
    print('most common start station: ',common_start_station)

    common_end_station=df['End Station'].mode()[0]
    print('most_common_end_station: ',common_end_station)

    frequent_stations_combination=df.groupby(['Start Station','End Station']).size().nlargest(0)
    print('most frequent combination of start and end station: \n ',frequent_stations_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time=df['Trip Duration'].sum()
    print('total travel time: ',total_travel_time)

    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time: ',mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types=df['User Type'].value_counts()
    print('counts of user types: ',user_types)
    
    if 'Gender' in df.columns:
        count_gender=df['Gender'].value_counts()
        print('counts of gender: \n',count_gender)
    else:
        print('Gender data missing')

    if 'Birth Year' in df.columns:
        earliest_year=df['Birth Year'].min()
        most_recent_year=df['Birth Year'].max()
        most_common_year=df['Birth Year'].count()
    else:
        print('Birth Year data missing')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   
def raw_input(df):
    view_data=input('Would you like to view 5 rows of individual trip data. Enter yes or no.:\n ').lower()
    raw_data=0
    while True:    
        if view_data!='yes':
            break
        print(df.iloc[0:5])
        raw_data += 5
        more_rows=input('Would you like to view 5 more rows. Enter yes or no.:\n ').lower()
        if more_rows=='yes':
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
