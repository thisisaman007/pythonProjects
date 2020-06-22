import json
from difflib import get_close_matches

#load JSON data
data = json.load(open("dict_data.json"))


word = input('Enter word: ')

def getMeaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

meaning = getMeaning(word)


if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)