import json


with open ("sample.txt" , "r") as f1:
    data = f1.read().strip().splitlines()

merged_data=[]
header = []
col1=[]
i=0

while i in range(0, len(data)):
    if (data[i] != " " and i <= 4):
        header.append(data[i].split("|")[0])
        col1.append(data[i].split("|")[1])

    elif (data[i] != " " and i > 4):
        col1.append(data[i].split("|")[1])

    if(i==4):
        merged_data.append(header)

    if(i%4 == 0 and i != 0):
        merged_data.append(col1)
        col1=[]
    i+=1

with open("output.json", "w") as file:
    json.dump(merged_data, file , indent=2)