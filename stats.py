def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

def get_book_words(file_contents):
    words = file_contents.split()
    return words

def count_characters(file_contents):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    lowercase = file_contents.lower()
    characters = list(lowercase)
    character_counts = {}
    for letter in letters:
        count = 0
        for character in characters:
            if letter == character:
                count += 1        
        character_counts[letter] = count
    return character_counts

def sort_on(items):
    return items["num"]

def sort_counts(character_counts):
    helper_list = []
    for k,v in character_counts.items():
        if k.isalpha():
            entry = dict(char = k, num = v)
            helper_list.append(entry)
    helper_list.sort(reverse=True, key=sort_on)
    return helper_list
