import csv
import time


def first_solution():
    reader = csv.DictReader(people)
    for row in reader:
        print(row['Name'], "is", row['Gender'], "and", row['Age'], "years old")


def second_solution():
    data = people.readlines()
    for line in data[1:]:
        name, age, gender = line.split(",")
        gender = gender.replace("\n", "")
        print(f"{name} is {gender} and {age} years old.")


with open("people.csv", "r") as people:
    first_solution()
    second_solution()

time.sleep(5)
