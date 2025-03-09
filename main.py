import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counting = character_count(text)
    sorted = chars_dict_to_sorted_list(character_counting)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")      
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
from stats import character_count
from stats import chars_dict_to_sorted_list

main()