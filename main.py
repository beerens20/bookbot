from stats import get_num_words, get_character_count, sorted_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] # provide the path to the book we want to analyze
    
    text = get_book_text(book_path) # call get_book_text and get back the contents of the book
    num_words = get_num_words(text) # push the contents of the book, split the content into a list, count the num of words
    
    raw_dict = get_character_count(text)
    sorted_list = sorted_dict(raw_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")
    print("============= END ===============")

    

def get_book_text(path):
    with open(path) as f: # open the file
        return f.read() # return the contents of the file as a string
    

main()