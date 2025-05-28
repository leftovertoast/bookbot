from stats import get_number_of_words, count_of_letters, generate_report

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    #print(text)
    mynum = get_number_of_words(text)
    #print(f"{mynum} words found in the document")
    lower_text = count_of_letters(text)
    #print(lower_text)
    report = generate_report(lower_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {mynum} total words")
    print("--------- Character Count -------")
    for item in report:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()
    