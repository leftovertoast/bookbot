def get_number_of_words(book_content):
    result = len(book_content.split())
    return result

def count_of_letters(book_content):
    lower_book = book_content.lower()
    alpha_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for char in lower_book: 
        if char in alpha_dict:
            alpha_dict[char] += 1
        elif char.isalpha():
            if char in alpha_dict:
                alpha_dict[char] += 1
            else:
                #print(f"Unexpected character found: {char}")
                alpha_dict[char] = 1 # Count unexpected characters as well
    return alpha_dict

def generate_report(count_dict):
    report = []
    for char, num in count_dict.items():
        report.append({"char": f"{char}", "num": num})
        report.sort(key=lambda item: item["num"], reverse=True)
    return report
   