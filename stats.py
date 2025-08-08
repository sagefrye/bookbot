def get_num_words(text):
    words = text.split()
    num_words = len(words)

    return num_words

def get_num_chars(text):
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_dict:
            char_dict[char_lower] = char_dict[char_lower] + 1
        else:
            char_dict[char_lower] = 1

    return char_dict

def clean_list(list):
    new_list = []
    for each in list:
        if each["char"].isalpha():
            new_list.append(each)

    return new_list

def sort_on(list):
    return list["num"]

def get_list_of_chars(dict_of_chars):
    list_of_chars = []
    for k, v in dict_of_chars.items():
        new_dict = {}
        new_dict["char"] = k
        new_dict["num"] = v
        list_of_chars.append(new_dict)

    new_list = clean_list(list_of_chars)

    new_list.sort(reverse = True, key=sort_on)

    return new_list
