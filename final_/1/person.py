import re
from datetime import date


class Person:
    def __init__(self, first_name: str, middle_name: str,
                 last_name: str, date_of_birth: str, gender: int,
                 identity: str, mobile_number: str):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.__identity = identity

        self.date_of_birth = ""
        self.set_date_of_birth(date_of_birth)

        self.phone_number = ""
        self.set_phone_number(mobile_number)

    def set_phone_number(self, phone_number: str):
        # \d stands for digit
        phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        if phone_num_regex.match(phone_number):
            self.phone_number = phone_number
        else:
            print("the phone number provided is not valid")

    def set_date_of_birth(self, date_of_birth: str):
        phone_num_regex = re.compile(r'\d\d:\d\d:\d\d\d\d')
        if phone_num_regex.match(date_of_birth):
            self.date_of_birth = date_of_birth
        else:
            print("date of birth provided is not valid")

    def get_age(self):
        if len(self.date_of_birth) == 0:
            return -1  # date of birth is not initialized

        dates = self.date_of_birth.split(":")
        year = int(dates[2])
        month = int(dates[1])
        day = int(dates[0])

        birthdate = date(year, month, day)

        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
