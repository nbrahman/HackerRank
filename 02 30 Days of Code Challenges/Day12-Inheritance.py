'''
Objective
Today, we're delving into Inheritance. Check out the Tutorial tab for learning materials and an instructional video!

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

    A Student class constructor, which has 4 parameters:
        A string, firstName.
        A string, lastName.
        An integer, id.
        An integer array (or vector) of test scores, scores.
    A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

[Grading.png]
                        Grading Scale
                        Letter  Average(a)
                        O       90<=a<=100
                        E       80<=a<90
                        A       70<=a<80
                        P       55<=a<70
                        D       40<=a<55
                        T       a<40

Input Format

The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).

You are not responsible for reading the following input from stdin:
The first line contains firstName, lastName, and id, respectively. The second line contains the number of test scores. The third line of space-separated integers describes scores.

Constraints
4<=|firstName|,|lastName|<=10
|id|=7
0<=score, average<=100

Output Format

This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input

Heraldo Memelli 8135627
2
100 80

Sample Output

 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

Explanation

This student had 2 scores to average: 100 and 80. The student's average grade is (100+80)/2=90. An average grade of 90 corresponds to the letter grade O, so our calculate() method should return the character'O'.
'''


class Student(Person):

# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self, firstName, lastName, id, l):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.scores = l

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if 90 <= avg <= 100:
            print ('O')
        elif 80 <= avg < 90:
            print ('E')
        elif 70 <= avg < 80:
            print ('A')
        elif 55 <= avg < 70:
            print ('P')
        elif 40 <= avg < 55:
            print ('D')
        elif avg < 40:
            print ('T')

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())