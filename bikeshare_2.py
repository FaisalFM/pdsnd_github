import time
import pandas as pd


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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    '''----'''

    while True:
        city = input("-------\nWould you like to see data for Chicago, New York City or Washington?\n").lower()

        if city in CITY_DATA.keys():
            break
    # get user input for month (all, january, february, ... , june)

    while True: # if the month in the list, will break and go for the next
        month = input("Please enter a month or enter All  (e.g. January, February, ... or June): \n").lower()
        if month in ["all","january","february","march",
                     "april","may","june"]:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a a weekday or enter All  (e.g.  Sunday): \n").lower()
        if day in ["all","sunday","monday","tuesday",
                     "wednesday","thursday","friday","saturday"]:
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
    '''---'''

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month



    df["day"] = df["Start Time"].dt.weekday_name



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
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month_pd = df['Start Time'].dt.strftime('%b').mode()[0]
    common_month = "-The most common month is: {}.".format(common_month_pd)
    print(common_month)

    # display the most common day of week
    common_day_pd = df['day'].mode()[0]
    common_day = "-The most common day is: {}.".format(common_day_pd)
    print(common_day)


    # display the most common start hour
    common_hour_pd = df['Start Time'].dt.hour.mode()[0]
    common_hour = "-The most common start hour is: {}.".format(common_hour_pd)
    print(common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("-The most commonly used start station: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("-The most commonly used end station: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['combination'] = (df['Start Station'] + ' and ' +  df['End Station'])
    most_combination = str(df['combination'].mode()[0])
    print("-The most frequent combination of start station and end station trip: {}".format(most_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum() / 3600
    print("-Total travel time : {}  hours".format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean() / 60
    print("-The average travel time : {}  minutes".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("-Counts of user types: \n\n{}".format(user_types))


    # Display counts of gender
    try:
        counts_gendar = df['Gender'].value_counts()
        print("\n-Counts of gender: \n{}".format(counts_gendar))

    except:
        pass

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print("\n\nEarliest year of birth: {} \nRecent year of birth: {}\nCommon year of birth: {}".format(earliest,recent,common_year))
    except:
        pass

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(city):


    df = open(CITY_DATA[city])
    df = pd.read_csv(df)
    i = 0
    n = 5
    row_data = input("-Do you want to see 5 lines of  raw data?\n   (Yes or No )\n").lower()
    while row_data == 'yes':
        if row_data != 'yes':
            break
        print(print(df.iloc[i:n]))
# will add 5 for the rows
        row_data = input("\n-Do you want to see next 5 lines of  raw data?\n   (Yes or No )\n").lower()
        i += 5
        n += 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
