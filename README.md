# New Hogwarts students into their houses.
## Description:
#### Basically, I have created an automatic system, which takes user input in the form of Name, Characteristics & Year of Birth and categorizes the student into the 4 houses.
#### The project.py document has 3 main functions: **check_crct_args**, **slct_house** and **slct_grade**.
#### The **check_crct_args** is a function that checks if the command line arguments entered in the terminal are correct or not. It has three filters:
1. If the no. of arguments are less than 3, then it displays "Too Few Command Line Arguments".
2. If the no. of arguments are more than 3, then it displays "Too Many Command Line Arguments".
3. And lastly is there is no ".csv" file in the arguments, then it displays "Not a .csv file".
#### Now, if the arguments are correct, then the programs finds if there is the ".csv" file that the user has entered.
#### If there is a csv file, then the program, collects the rows, and appends them in the list, "list".
#### The **slct_house** function works like this:
1. It finds the characteristics of the new student from the rows of the ".csv" file.
2. Then, if the particular "characteristic" shortened as "charac" is present, and is related to a particular house, then they are linked. Characteristics of the houses are:
**Gryffindor = Courage, Loyalty and Adventure |**
**Hufflepuff = Dedication, Patience and Honesty |**
**Ravenclaw = Wisdom, Creativity and Perfectionism |**
**Slytherin = Ambition, Competitive and Leadership |**
3. If for example, the new student has a characteristic not related a particular house, then the program categorizes it into the "No House" category.
#### The **slct_grade** function works like this:
1. In the ".csv" file the year of birth is already given, I have implemented a simple arithmentic argument, the "age" is determined by the year of birth being subtacted from the current year (2023).
2. Next, the grade, is determined by subtracting 5 from the age.
3. The program then returns the grade as, "Grade 9" for example.
#### Now, the most interesting work of the program is to enter the new found values into the "after.csv" file.
#### It is done like this:
1. The house is determined by using the "slct_house" function.
2. The grade is determined by using the "slct_grade" function.
3. Then they are appended on the output list along with the name.
4. Next, using the DictReader command, the fieldnames are added **["name", "house", "grade"]**.
5. Then, under the fieldnames, the names, houses & gardes of all the students are added.
#### This was a simple walkthrough of my project.
## THANK YOU
