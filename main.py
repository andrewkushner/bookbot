def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    chars_dict_sorted = sorted(chars_dict)

    print(f"The {book_path} contains {num_words} words.")
    
    for item in chars_dict_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]

def sorted(dict):
    sorted_dict = []
    for c in dict:
        sorted_dict.append({"char": c, "num": dict[c]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return(len(words))

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
