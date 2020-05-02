import csv


def one_solution():
    reader = csv.DictReader(people)
    for row in reader:
        print(row['Name'], "is", row['Gender'], "and", row['Age'], "years old")
    # I think this method is better because it's easier to read


def second_solution():
    data = people.readlines()
    for line in data[1:]:
        print(line.split(',')[0], "is", line.split(',')[2].strip('\n'), "and", line.split(',')[1], "years old.")
    # Without ".strip('\n')" the rest of the text gets written in new line, don't know why.


with open("people.csv", "r") as people:
    one_solution()
    second_solution()
