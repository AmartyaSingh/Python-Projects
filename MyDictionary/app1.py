import json
from difflib import get_close_matches

#to load json file into usable variable.
data = json.load(open("data.json"))

#function to find the meaning of the User Entry(UE).
def meaning(w):

    w = w.lower() #to convert UE into all lowercase.
    p = w[0].upper() + w[1:] #to rectify bug of "Delhi", by making the index 0 as capital.
    y = w.upper()

    #return meaning when all lowercase.
    if w in data:
        return data[w] #

    #return meaning when element at index 0 is uppercase.
    if p in data:
        return data[p]

    if y in data:
        return data[y]

    #to adjust for incorrect but close UEs 
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did you mean %s instead? Y/N" % get_close_matches(w, data.keys())[0])
        choice = input("")
        if choice == 'Y' or choice == 'y':
            return(data[get_close_matches(w, data.keys())[0]])
        else:
            return("God Help You :P")

    else:
        return "No Data! :P"

#UE 
word = input("Enter Word: ")
output = meaning(word)

#to print meaning without brackets.
if type(output) == list:
    for i in output:
        print (i)
else:
    print(output)
