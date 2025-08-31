def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_char_counts(filepath):
    with open(filepath)as f:
        file_contents = f.read()
    char_dict = {}
    for c in file_contents.lower():
        try:
            char_dict[c] = char_dict[c]+1
        except:
            char_dict[c] = 1
    return char_dict

def get_sorted_chars(filepath):
    with open(filepath)as f:
        file_contents = f.read()
    char_dict = {}
    for c in file_contents.lower():
        if c.isalpha() == True:
            try:
                char_dict[c] = char_dict[c]+1
            except:
                char_dict[c] = 1
    dict_list = []
    for dict_key in char_dict:
        dict_list.append({"char":dict_key, "num":char_dict[dict_key]})
    def sort_on(my_dict_list):
        return my_dict_list["num"]
    dict_list.sort(reverse=True,key=sort_on)
    return dict_list