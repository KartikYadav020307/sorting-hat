import sys
import csv


def main():
    chck_crct_args()
    list = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list.append(row)
    except FileNotFoundError:
        sys.exit(".csv file doesn't exist")

    output = []
    for row in list:
        house = slct_house(row[" characteristic"])
        grade = slct_grade(row["birthdate"])
        output.append({"name": row["name"], "house": house, "grade": grade})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "grade"])
        writer.writerow({"name": "name", "house": "house", "grade": "grade"})
        for row in output:
            writer.writerow(
                {"name": row["name"], "house": row["house"], "grade": row["grade"]})


def chck_crct_args():
    if len(sys.argv) < 3:
        sys.exit("Too Few Command Line Arguments")
    if len(sys.argv) > 3:
        sys.exit("Too Many Command Line Arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a .csv file")


def slct_house(charac):
    if charac in ["courage", "loyalty", "adventure"]:
        return "Gryffindor"
    elif charac in ["dedication", "patience", "honesty"]:
        return "Hufflepuff"
    elif charac in ["wisdom", "creativity", "perfectionism"]:
        return "Ravenclaw"
    elif charac in ["ambition", "competitive", "leadership"]:
        return "Slytherin"
    else:
        return "No House"


def slct_grade(year):
    age = 2023 - int(year)
    grade = age - 5
    return "Grade " + str(grade)


if __name__ == "__main__":
    main()
