def get_num_words(text):
    words = text.split() # split the contents of the file into a list
    return len(words) # return the number of items in the list

def get_character_count(text):
    lower_text = text.lower()
    characters = {}
    for ch in lower_text:
        characters[ch] = characters.get(ch, 0) + 1
    return characters

def sort_on(d):
    return d["num"]

def sorted_dict(raw_dict):
    sorted_list = []
    for ch in raw_dict:
        sorted_list.append({"char": ch, "num": raw_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
