import json


with open ("sample.txt" , "r") as f1:
    data = f1.read().strip().splitlines()

merged_data=[]
i=0
dict ={}

while i in range(0, len(data)):
    if data[i] != " ":
        dict[data[i].split("|")[0]] = data[i].split("|")[1]
    
    if(i%4 == 0 and i != 0):
        merged_data.append(dict)
        dict={}
    i+=1

with open("output.json", "w") as file:
    json.dump(merged_data, file , indent=2)