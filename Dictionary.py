import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def tran(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s " %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes and n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            print("You have wrong input "+word+" does not exist in dictionary.")
        else:
            print("You have enter wrong input please just enter y or n.")
    else:
        print("This word does not exist in dictionary.")

word = input("Enter the word you want to search:")
output = tran(word)
if type(output) == list:
    for iteam in output:
        print(iteam)

