def count_words(string):
    string_array = string.split()
    return len(string_array)

def count_characters(string):
    character_dict = {}
    for char in string:
        lowercase_char = char.lower()
        if lowercase_char in character_dict:
            character_dict[lowercase_char] += 1
        else:
            character_dict[lowercase_char] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    sorted_list = []
    for key, value in dict.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


