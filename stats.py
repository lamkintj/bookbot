def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return(file_contents)

def get_book_words(file_contents):
    words = file_contents.split()
    return words