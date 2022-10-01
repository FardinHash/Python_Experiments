print('Enter your marks:')  

#marks input
cour1= int(input('Course 1: '))
cour2= int(input('Course 2: '))
cour3= int(input('Course 3: '))
cour4= int(input('Course 4: '))


result= (cour1 + cour2 + cour3 + cour4)/4  #result calculated with average

#calculator
if result>= 90:
    print('Grade: A')
elif result>= 80:
    print('Grade: B')
elif result>= 70:
    print('Grade: C')
elif result>= 60:
    print('Grade: D')
else:
    print('Retake!')
