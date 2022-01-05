import datetime

def calendar(year,month):
    weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']


    current_date = datetime.date(year, month, 1)

    if (current_date.weekday() == 6):
        current_date -= datetime.timedelta(days=1)

    while (current_date.weekday() != 6):
        current_date -= datetime.timedelta(days=1)

    print(' ' * 4 + months[month - 1] + ', ' + str(year))

    date_string = ' '.join(weeks)
    print(date_string)

    while True:
        for i in range(7):
            current_date += datetime.timedelta(days=1)
            print(str(current_date.day).ljust(4), end='')
        print()
        if (current_date.month != month):
            break

year = int(input('Enter the year\n'))
month = int(input('Enter month (1 - 12)\n'))

calendar(year,month)
