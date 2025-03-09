def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    lowercase_text = text.lower()
    char_list = list(lowercase_text)
    for char in char_list:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 