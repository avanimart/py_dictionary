import json
from difflib import get_close_matches

# load the data 
data =  json.load(open("dictionary.json"))


def retrieve_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()] # return definitions of words that start with capital
    elif word.upper() in data:
        return data[word.upper()] # return definitions of words that are capital
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input('Did you mean {} instead? ["y" or "n"]: '.format(get_close_matches(word, data.keys())[0]))
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        return "We don't understand you search. Please try again later."

    return "That word does not exist. Please double check!"

# take input from user,
# retrieve the definition

user_input = input("Enter a word: ").lower()
# s = SequenceMatcher(None, user_in)

print(retrieve_definition(user_input))

