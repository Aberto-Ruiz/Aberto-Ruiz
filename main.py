import requests
import json
import time

print ("solicitando información de Internet")
URL= "https://jsonplaceholder.typicode.com/posts"
i=0
data = requests.get(URL).json()
#userId', 'id', 'title', 'body'

for i in range(0,100,10):
    time.sleep(10)
    old_list=data[i:i+10]
    #print(old_list)
    new_list={}
    for item in old_list:
        if item["userId"] not in new_list:
            new_list[item["userId"]]={}
            new_list[item["userId"]]["records"]=[]
            rec={}
            rec["id"]=item["id"]
            rec["title"]=item["title"]
            rec["body"]=item["body"]
            new_list[item["userId"]]["records"].append(rec)
        else:
            rec={}
            rec["id"]=item["id"]
            rec["title"]=item["title"]
            rec["body"]=item["body"]
            new_list[item["userId"]]["records"].append(rec)
    #print(new_list)
    new_list = json.dumps(new_list, indent=3)
    print(new_list)
