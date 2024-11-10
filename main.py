def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    nmb_words = get_number_of_words(text)
    print(f"Number of words: {nmb_words}")
    char_count = count_characters(text)
    print(f"Character counts:\n {char_count}")


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


main()
