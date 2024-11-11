def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    nmb_words = get_number_of_words(text)
    char_count = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words: {nmb_words}\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(text):
    return len(text.split())


def count_characters(text):
    lower_text = text.lower()
    chartocount = {}

    for char in lower_text:
        if char in chartocount:
            chartocount[char] += 1
        else:
            chartocount[char] = 1
    return chartocount

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
