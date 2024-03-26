
# Take The Input From The User
a = float(input("Enter The Price Of The Item "))
print('You Have Entered ',(a))
result = (a-(a*0.2))
print("The Net Price Of The Item After 20% Discount is ")
print(result)


#Floating point division and Integer division
#Floating point division /
#integer Division //

a=7
b=2
flot=float(a/b)
integer=a//b
print('Floating point division',flot)
print('Integer division',integer)


#Program to calculate Commulative Grade Point Average test score
pit_score=float(input("Enter Your PIT Marks "))
dsa_score=float(input("Enter Your DSA Marks "))
java_score=float(input("Enter Your Java Marks "))
comp_score=float(input("Enter Your COMP Marks "))
dadc_score=float(input("Enter Your DADC Marks "))
average = (pit_score*3+dsa_score*3+java_score*4+comp_score*4+dadc_score*3+28)/20
print('Your Average Score Is',average,'Your gpa is',average/4)

#Usage Of Exponent Operator
a=2**3
print(a)

#Usage of mod % operator
a=22%7
print(a)

#Program to convert the given input [in seconds] to appropriate hours , minutes , seconds
r=float(input("Enter The Time In Seconds "))

hrs_=r//3600
min_=r%3600//60
sec_=r%3600%60
print("The Value Of " +str(r) + " Seconds In HMS Is ")
print(str(hrs_)+" Hours")
print(str(min_)+" Minutes")
print(str(sec_)+" Seconds")
