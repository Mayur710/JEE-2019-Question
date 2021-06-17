"""
Q)In a class of 140 students numbered from 1 to 140. 
All even number student opted maths course. All multiple of 3
numbered students opted physics course. And all multiple of 5 numbered 
students opted chemistry course.
Find the no. of students who did not opted any of three course."""

U = set(range(1, 141))
l_of_U = len(U)  # Lenght of the universal set.
li_of_U = list(U)  # Typecast universal set into list.


def maths(p):
    Math = []  # Empty list where the elemnets will be filled after the scan from for loop
    for n in li_of_U:
        if n % 2 == 0:
            Math.append(n)
    return Math

def physics(p):
    physics = []
    for n in li_of_U:
        if n % 3 == 0:
            physics.append(n)
    return physics

def chemistry(p):
    chemistry = []
    for n in li_of_U:
        if n % 5 == 0:
            chemistry.append(n)
    return chemistry

Chemistry_course = chemistry(li_of_U)# List of all the students who took chemistry.
Physics_course = physics(li_of_U) # List of all the students who took physics.
Maths_course = maths(li_of_U) # List of all the students who took maths
s_of_Maths = set(Maths_course) # Set of all the students who took maths.
s_of_Physics = set(Physics_course)# Set of all the students who took physics
s_of_Chemistry = set(Chemistry_course)# Set of all the students who tokk chemistry.
mUpUc = set.union(s_of_Maths, s_of_Physics, s_of_Chemistry)
# Let students who did not opted any course be x
x = U - mUpUc
# Let no.of students who did not opted any course be y
y = len(x)
print(y)