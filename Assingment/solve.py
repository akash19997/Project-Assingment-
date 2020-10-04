# Name: Akash Kanojya

import json

with open("roles.txt") as f: 
    data = f.read()
with open("user.txt") as f: 
    data1 = f.read()

roles = json.loads(data)
user= json.loads(data1)
user_1=user["User_1"]
user_2=user["User_2"]
user1=[]
user2=[]
orphan={}

for key1,value1 in user.items():
    for key,value in roles.items():
        for i in range(len(roles[key])):
            if roles[key][i] in user_1:
                user1.append(key)
            else:
                orphan[key1]=value[i]
            if roles[key][i] in user_2:
                user2.append(key)
            else:
                orphan[key1]=value[i] 
suggested_roles={"User_1":list(set(user1)),"User_2":list(set(user2))}
with open("Suggested_Roles.txt", 'w') as file:
     file.write(json.dumps(suggested_roles))
    
with open("orphan.txt", 'w') as file:
     file.write(json.dumps(orphan))
     
     
print("\nOutput written to file name:\nSuggested_Roles.txt")
with open('Suggested_Roles.txt', 'r') as f:
    print(f.read())
print("\nOutput written to file name:\nroles.txt")
with open('roles.txt', 'r') as f:
    
    print(f.read())



