from datetime import datetime


def ask_input():
    print("Input date in format dd-mm-yyyy")
    return input('Enter here: ')


def year_difference():
    current_date = datetime.now()
    user_date = datetime.strptime(ask_input(), "%d-%m-%Y")

    difference = (current_date - user_date).days
    age = int(difference//(365+1/4))
    return (age)


print(year_difference())
