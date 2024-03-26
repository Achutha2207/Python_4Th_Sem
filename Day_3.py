#Program to calculate the simple interest
#Input Variables - p , r , n , t
#Principle amount , rate of intererst , no of times compounded , Time interval

p = float(input("Enter The Principle Amount "))
r = float(input("Enter The Interest Recieved Per Annum "))
n = float(input("Enter Number Of Times The Interest Is Compounded Annually "))
t = float(input("Enter Number Of Years You Want To Recieve Interest "))

a = p*((1+(r/n))**(n*t))
print("You Will Have Final Amount Of " +str(a))


#What if I know How Much Amount I need In 10years?

a = float(input("Enter The Amount You Want To Recieve "))
r = float(input("Enter The Interest Recieved Per Annum "))
n = float(input("Enter Number Of Times The Interest Is Compounded Annually "))
t = float(input("Enter Number Of Years You Want TO Lock In "))

p = a/((1+(r/n))**(n*t))
print("You Should Have Invested  " +str(p) + "$ To Recieve " +str(a) + "$ Before " + str(t)+ " Years At An Interest Of " +str(r)+"%")
