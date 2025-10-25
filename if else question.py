
## Electricity Bill calculator 
u=int(input("Enter electricity unit consymed:")) 
if u<=100:
    bill=u*5
elif u<=200:
    bill=(100*5)+(u-100)*7 
else:
    bill=(100*5)+(100*7)+(u-200)*10
print("Total bill",bill) 
## traffic Light signal 
c=input("Enter the color(red/green/yellow):")
if c=="red":
    print("stop") 
elif c=="yellow":
    print("get ready")
elif c=="green":
    print("go") 
else:
    print("invalid color")
## check Eligible to vote or not
age=int(input("Enter your age:")) 
if age >=18:
    print("you are eligible to vote") 
else:
    print("you are not eligible to vote") 
## Movie ticket price based on age 
age=int(input("Enter your age:"))
if age<5:
    print("free entry")  
elif age<=18:
    print("ticket price is 100") 
elif age<=60:
    print("Ticket price is 170") 
else:
    print("Ticket price is 120")  
## Leep year or not leep year 
y=int(input("Enter year:")) 
if (y%4==0 and y%100!=0 or y%400==0):
    print("leep year")
else:
    print("Not leep year") 
## Mini Quiz 
score=0 
q1=input("Capital of India ?") 
if q1=="delhi":
    score +=1
q2=input("5+7=?")
if q2=="12":
    score+=1 
q3=input("python is a ?")
if q3=="language":
    score+=1 
if score==3:
    print("Excellent!") 
elif score==2:
    print("Good!") 
elif score==1:
    print("Trry again") 
else:
    print("Batter luck next time") 