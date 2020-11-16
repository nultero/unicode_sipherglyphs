import json

# this print of all the cipher chars is just to format them to where I could delete the ones I didn't want
# ironically, I just wanted to pick out all the 'cool-looking' unicode nuggets

with open('cipher.json') as data_file:    
    data = json.load(data_file)
    
for i in data:
    print(f"{i} : {data.get(i)}")