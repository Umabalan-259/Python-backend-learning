#Basic print method
print("Hello")
print(123)
print(3.14)
#Multiple arguments default separator=space sep-->between two strings
print("Hello","World","123")
#Custom separater "sep" is used
print("Apple","Banana","Grapes",sep='-')
print("Apple","Red",sep=':')
#Custom end character "end" is used
print("Hello",end='!')
print("World",end="***\n")
#Combing sep and end
print(1,2,3,sep="s",end="%\n")
#F-strings
name="Uma"
age="20"
print(f"I am {name} and I'm {age} years old")
#.format() method
print("Hello {},you are {}".format("Uma",20))
print("Numbers:{1} and {0}".format(10,20))

#Challenge set1: Print variations
user_id=1001
user_name="uma_balan"
email="umanithin2006@gmail.com"
signup_date="2026-08-30"
print(user_id,user_name,email,signup_date,sep=" | ")
#challenge set2:API request progress
print("Fetching data",end='')
print(".",end="")
print(".",end="")
print(".",end="")
#challenge 3:Task display table using f-strings
task_id=101
title="Learn Python"
status="Progress"
assigned_to="Uma"
print(f"\n{task_id}|{title}|{status}|{assigned_to}")
#challenge 4:Error Log Message
error_code="DB_TIMEOUT"
timestamp="2026-08-30 15:45:30"
message="Connection refused"
retry_attempt=2
print(f"{error_code}",f"{timestamp}",f"{message}",f"{retry_attempt}",sep=" | ")
#Challenge 5:CSV Export
tasks=[(101,"Setup database","Completed"),(102,"Build API","In progress"),(103,"Write tests","Pending")]
print("ID","Title","Status")
for task in tasks:
    print(task[0],task[1],task[2])
#Challenge 6:API response message
user_count=42
active_users=38
inactive_users=4
percentage_active=(active_users/user_count)*100
print(f"Total Users: {user_count}",f"Active: {active_users}({percentage_active})%",f"Inactive:{inactive_users}",sep="|")
#Challenge 7:Real-time server log
request_count=3
print("Processing requests",end="",flush=True)
for i in range(request_count):
    print(".",end="",flush=True)
print("Complete!")
