import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'C': [ 'Chicago', 'chicago.csv'],
              'N': [ 'New York','new_york_city.csv'],
              'W': [ 'Washington','washington.csv'] }


def load_Filtered_Data():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        
        city =input("Would you like to see data for? Type C - Chicago,N - New York, W - Washington\n")
        
        if city.upper() in CITY_DATA:
            print("City Selected :", CITY_DATA[city.upper()][0])
            print("Loading File :", CITY_DATA[city.upper()][1])
            city=CITY_DATA[city.upper()][1]
            break
        else :
            print("Please Input the right City.")

    df = pd.read_csv(city)

    print('-'*40)
    
    # convert the Start Time column to datetime

    # get user input for month (all, january, february, ... , june)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month

    unique_months=np.sort(df.month.unique())

    print("Valid Months in Data:",unique_months)

    while True:

        month =input("Enter a Valid Month (in Numbers) :\n")
        
        if str(month.lower()) == "all":
            print("All Months Selected")
            break  
        if int(month) in unique_months:
            print("Month Selected:",calendar.month_name[int(month)])
            df = df[df['month'] == int(month)]
            break
        else :
            print("Please Input the right Month.")
            
    print('-'*40)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    df['weekday'] = df['Start Time'].dt.dayofweek    
    
    unique_weekdays=np.sort(df.weekday.unique())

    print("Valid Weekday in Data:",unique_weekdays)
    
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    while True:

        weekday =input("Enter a Valid Weekday (in Numbers) :\n")
        
        if str(weekday.lower()) == "all":
            print("All Weekday Selected")
            break                
        elif int(weekday) in unique_weekdays:
            print("Weekday Selected:",days[int(weekday)])
            df = df[df['weekday'] == int(weekday)]
            break
        else :
            print("Please Input the right Weekday.")

    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('\nMost Popular Month :',calendar.month_name[int(popular_month)])
   
    # display the most common day of week
    
    popular_weekday = df['weekday'].mode()[0]
    
    print('\nMost Common day of Week :',days[popular_weekday])

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('\nMost Common Hour :',popular_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    popular_StartStation = df['Start Station'].mode()[0]
    print('\nMost Commonly used Start Station :',popular_StartStation)
    
    # display most commonly used end station
    
    popular_EndStation = df['End Station'].mode()[0]
    print('\nMost Commonly used End Station :',popular_EndStation)

    # display most frequent combination of start station and end station trip

    popular_StartEndStation = (df['Start Station'] + ' ' + df['End Station']).mode()[0]
    print('\nMost frequent combination of start station and end station trip :',popular_StartEndStation)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    TotalTravelTime=df['Trip Duration'].sum()
    print('\nTotal Travel Time :',TotalTravelTime)

    # display mean travel time
    
    MeanTravelTime=df['Trip Duration'].mean()
    print('\nMean Travel Time :',MeanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print("Count of User Types:\n",user_types)
    else :
        print("User Type data is not available for this Data Frame")
    
    # Display counts of gender
    if 'Gender' in df.columns:
        user_gender = df['Gender'].value_counts()
        print("Count of Genders:\n",user_gender)
    else :
        print("Gender data is not available for this Data Frame")
        
    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        byear_min = df['Birth Year'].min()
        byear_max = df['Birth Year'].max()
        byear_mode = df['Birth Year'].mode()[0]

        print("Youngest Traveller Year : ",byear_min," Oldest Traveller Year : ",byear_max," Most Common Year of Birth : ",byear_mode)

    else :
        print("Birth Year data is not available for this Data Frame")       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('\n Displaying Data...\n')
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    end_loc=5
    while (view_data.lower() == "yes"):
        print(df.iloc[start_loc:end_loc])
        print('-'*40)
        start_loc += 5
        end_loc +=5
        view_data = input("Do you wish to see next 5 rows ?: ").lower()
    
def main():
    while True:
        df = load_Filtered_Data()
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
    main()
