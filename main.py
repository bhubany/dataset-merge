import csv

word_list = ['district','Kathmandu','Dhanusha','Kavrepalanchowk']
def spellingCorrector(word, word_list = word_list):
    word = word.replace(" ", "")
    for w in word_list:
        if(w == word):
            return w
        else:
            count = 0
            length =len(w) if(len(w) < len(word)) else len(word)
            for i in range(0, length):
                if(w[i] == word[i]):
                    count+=1

            if (count >= len(word)/2):
                return w

with open ("sample.txt" , "r") as f1:
    data = f1.read().strip().splitlines()


dict1={}
dict2={}
i=0

while i in range(0, len(data)):
    if (data[i] != " " and i <= 4):
        dict1[spellingCorrector(data[i].split("|")[0])] =data[i].split("|")[1]

    elif (data[i] != " " and i > 4):
        dict2[spellingCorrector(data[i].split("|")[0])] =data[i].split("|")[1]
    i+=1

f = open('output.csv', 'w')
writer = csv.writer(f)

for key in dict1:
    list1 = [key , dict1[key], dict2[key]]
    writer.writerow(list1)