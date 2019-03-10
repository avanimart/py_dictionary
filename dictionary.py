import json

# load the data 
data =  json.load(open("dictionary.json"))


def retrieve_definition(word):
    if word in data:
        return data[word]
    return "That word does not exist. Please double check!"

# take input from user,
# retrieve the definition

user_input = input("Enter a word: ")

print(retrieve_definition(user_input))

