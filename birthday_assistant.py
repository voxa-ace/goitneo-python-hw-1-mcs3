"""
Birthday Assistant

This script calculates and displays upcoming birthdays

for a list of co-workers.
"""

import datetime
import users

def get_birthdays_per_week(user_list):
    """
    Calculate and display upcoming birthdays for the given list of workers.

    Args:
        user_list (list): A list of user dictionaries containing name and
    birthday.

    Returns:
        None
    """
    current_date = datetime.datetime.today().date()
    users_to_present = {}

    for user in user_list:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            day_name = birthday_this_year.strftime('%A')
            if day_name not in users_to_present:
                users_to_present[day_name] = []
            users_to_present[day_name].append(name)

    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"]

    for day in ordered_days:
        if day in users_to_present:
            if day in ("Saturday", "Sunday"):
                if "Monday" not in users_to_present:
                    users_to_present["Monday"] = []
                users_to_present["Monday"].extend(users_to_present[day])
                del users_to_present[day]

    for day in ordered_days:
        if day in users_to_present:
            print(f"{day}: {', '.join(users_to_present[day])}")

if __name__ == "__main__":
    get_birthdays_per_week(users.users)
