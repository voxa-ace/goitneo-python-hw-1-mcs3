import users
import datetime


def get_birthdays_per_week(users):
    current_date = datetime.datetime.today().date()
    users_to_present: dict[str, list] = {}

    for user in users:
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

    for day, users_list in users_to_present.items():
        print(f"{day}: {', '.join(users_list)}")

# отсортировать дни


if __name__ == "__main__":
    get_birthdays_per_week(users.users)
