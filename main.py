from stats import get_book_text
from stats import get_book_words
from stats import count_characters
from stats import sort_counts

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    words = get_book_words(file_contents)
    num_words = len(words)
    character_counts = count_characters(file_contents)

    # Printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_list = sort_counts(character_counts)
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")

main()