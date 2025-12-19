def get_num_words(text):
    words = text.split() # split the contents of the file into a list
    return len(words) # return the number of items in the list

def get_character_count(text):
    lower_text = text.lower()
    characters = {}
    for ch in lower_text:
        characters[ch] = characters.get(ch, 0) + 1
    print(characters)
