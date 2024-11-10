def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    nmb_words = get_number_of_words(text)
    print(f"Number of words: {nmb_words}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(text):
    return len(text.split())


main()
