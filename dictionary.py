import json

# load the data 
data =  json.load(open("dictionary.json"))


def retrieve_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()] # return definitions of words that start with capital
    elif word.upper() in data:
        return data[word.upper()] # return definitions of words that are capital

    return "That word does not exist. Please double check!"

# take input from user,
# retrieve the definition

user_input = input("Enter a word: ").lower()

print(retrieve_definition(user_input))

