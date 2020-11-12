#We take from the user the hypotenuse's size
hyp=int(input("What is hypotenuse's size?"))
#We take from the user the opposite side's size
oppos=int(input("What is opposite side's size?"))
#We take from the user the adjacent side's size
adjacent=int(input("What is adjacent side's size?"))
if hyp == oppos == adjacent:
    type_of_triangle='equilateral triangle'
elif oppos != adjacent and oppos == hyp:
    type_of_triangle ='isosceles triangle'
else:
    type_of_triangle = 'scalene triangle'
print('The triangle is', type_of_triangle)
