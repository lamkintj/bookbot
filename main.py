from stats import get_book_text
from stats import get_book_words
from stats import count_characters

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    words = get_book_words(file_contents)
    num_words = len(words)
    print(f"Found {num_words} total words")
    character_counts = count_characters(file_contents)
    print(character_counts)

main()