from stats import get_number_of_words, count_of_letters

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)
    mynum = get_number_of_words(text)
    print(f"{mynum} words found in the document")
    lower_text = count_of_letters(text)
    print(lower_text)

main()
    