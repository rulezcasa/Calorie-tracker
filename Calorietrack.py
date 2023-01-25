import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
con=mysql.connector.connect(user='root', password='harish12345678',host='Localhost',database='calorietracker')
cursor=con.cursor()
print("You are hands on with a basic meal and calorie tracker, stay fit!")
weight=float(input("Please input youre weight in KG"))
height=float(input("Please enter youre height in metres"))
bmi=(weight/height**2)
print("Your BMI is",round(bmi,1),"compare it with the chart below")
cursor.execute("select * from bmi")
data=cursor.fetchall()
for row in data:
    print(row)
ibmi=float(input("Enter a BMI in which you would like to see yourself in"))
dbmi=bmi-ibmi
print("You are",round(dbmi,1),"points away from your ideal BMI")
target=int(input("Enter your daily calorie target"))
print("Here is your available food database:")
cursor.execute("select * from meal")
data=cursor.fetchall()
for row in data:
    print (row)
flag1=1
while(flag1==1):
    print("If you wish to add more items, type yes")
    print("If you wish to delete existing item, type delete")
    print("If you wish to make no changes, type no")
    ch=str(input(" "))
    if((ch!='yes') and (ch!='no') and (ch!='delete')):
        print("Wrong input, try again")
        continue
    elif(ch=='no'):
        break
    elif(ch=='yes'):
        meal=str(input("Enter food name"))
        cal=int(input("Enter calories"))
        sql = "INSERT INTO meal(name,calories) VALUES (%s, %s)"
        val = (meal,cal)
        cursor.execute(sql, val)
        con.commit()
        print("Food added!")
        ch2=str(input("Type yes to make more changes. Type no to stop"))
        if((ch2!='yes') and (ch2!='no')):
            print("Wrong input, exiting")
            break
        elif(ch2=='yes'):
            flag1=1
        else:
            flag1=0
    else:
        delete=str(input("Enter name of meal you want to delete"))
        name=delete
        sql="delete from meal where name=%s"
        cursor.execute(sql,(name,))
        con.commit()
        print("Food deleted!")
bfcal=0
luncal=0
snacal=0
dincal=0
totalcal=0
print("Let's start your entries")
print("press n if this is a new day")
print("Press anything to continue")
new=str(input(""))
if(new=='n'):
    cursor.execute("delete from breakfast");
    cursor.execute("delete from lunch");
    cursor.execute("delete from dinner");
    cursor.execute("delete from snacks");
flag2=1
while(flag2==1):
    cursor.execute("select * from meal")
    data=cursor.fetchall()
    for row in data:
        print (row)
    bf=str(input("Enter food item"))
    sql1="select name from meal where name=%s"
    sql2="select calories from meal where name=%s"
    cursor.execute(sql1,(bf,))
    data1=cursor.fetchone()
    cursor.execute(sql2,(bf,))
    data2=cursor.fetchone()
    print("press 1 to add to breakfast")
    print("press 2 to add to lunch")
    print("press 3 to add to snacks")
    print("press 4 to add to dinner")
    ch3=int(input(" "))
    if(ch3==1):
        sql = "INSERT INTO breakfast(food,calories) VALUES (%s, %s)"
        val = (data1[0],data2[0])
        cursor.execute(sql, val)
        con.commit()
        bfcal=bfcal+data2[0]
        totalcal=totalcal+data2[0]
        print("calories left for the day:",(target-totalcal))
    elif(ch3==2):
        sql = "INSERT INTO lunch(food,calories) VALUES (%s, %s)"
        val = (data1[0],data2[0])
        cursor.execute(sql, val)
        con.commit()
        luncal=luncal+data2[0]
        totalcal=totalcal+data2[0]
        print("calories left for the day:",(target-totalcal))
    elif(ch3==3):
        sql = "INSERT INTO snacks(food,calories) VALUES (%s, %s)"
        val = (data1[0],data2[0])
        cursor.execute(sql, val)
        con.commit()
        snacal=snacal+data2[0]
        totalcal=totalcal+data2[0]
        print("calories left for the day:",(target-totalcal))
    elif(ch3==4):
        sql = "INSERT INTO dinner(food,calories) VALUES (%s, %s)"
        val = (data1[0],data2[0])
        cursor.execute(sql, val)
        con.commit()
        dincal=dincal+data2[0]
        totalcal=totalcal+data2[0]
        print("calories left for the day:",(target-totalcal))
    else:
        print("Wrong input")
    print("Type yes to continue adding")
    print("Type anything to stop")
    ch4=str(input(" "))
    if(ch4=='yes'):
        flag2=1
    else:
        flag2=0
print("Calories consumed for breakfast:",bfcal)
print("Calories consumed for lunch:",luncal)
print("Calories consumed for snacks:",snacal)
print("Calories consumed for dinner:",dincal)
y=np.array([bfcal,luncal,snacal,dincal])
mylabels = ["Breakfast", "Lunch", "Snacks", "Dinner"]
plt.pie(y, labels=mylabels, autopct='%1.1f%%', explode=[0,0,0,0], shadow=True, startangle=90)
plt.axis('equal')
plt.show()
        
    
    
    



    
    

               


