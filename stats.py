def get_num_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def count_characters(file_contents):
    characters_dict = {}
    file_contents = file_contents.lower()
    for character in file_contents:
        if character not in characters_dict:
            characters_dict[character] =1
        else:
            characters_dict[character] +=1
        print(characters_dict)
    return characters_dict

def create_report(characters_dict):
    characters_list = []
    for ch in characters_dict:
        characters_list.append({"char": ch, "num": characters_dict[ch]})
    characters_dict.sort(reverse=True, key=sort_on)
    return characters_list

def sort_on(item):
    return item["num"]


    