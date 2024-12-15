

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def logger():
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document\n\n")
    for i in chars_dict:
        if(i.isalpha()):
            print(f"The '{i}' character was found {chars_dict[i]} times\n")

book_path = "books/frankenstein.txt"
text = get_book_text(book_path)
num_words = get_num_words(text)
chars_dict = get_chars_dict(text)

def main():
    logger()

main()

