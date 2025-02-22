from stats import count_words
from stats import count_charakters

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")
    charakters = count_charakters(get_book_text("books/frankenstein.txt"))
    print(charakters)
    
main()