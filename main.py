from stats import get_number_of_words 

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    mynum = len(text.split())
    print(f"{mynum} words found in the document")


main()
    