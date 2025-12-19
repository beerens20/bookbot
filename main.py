from stats import get_num_words, get_character_count

def main():
    book_path = "books/frankenstein.txt" # provide the path to the book we want to analyze
    text = get_book_text(book_path) # call get_book_text and get back the contents of the book
    num_words = get_num_words(text) # push the contents of the book, split the content into a list, count the num of words
    print(f"Found {num_words} total words")
    get_character_count(text)

def get_book_text(path):
    with open(path) as f: # open the file
        return f.read() # return the contents of the file as a string

main()