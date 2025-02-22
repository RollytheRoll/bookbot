from stats import count_words
from stats import count_charakters
from stats import sorted_charakters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    words = count_words(get_book_text(sys.argv[1]))
    charakters = count_charakters(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    sorted_list = sorted_charakters(charakters)
    for charakter in sorted_list:
        counter = sorted_list[charakter]
        print(f"{charakter}: {counter}")
    print("============= END ===============")

    
main()