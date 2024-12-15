with open("books/frankenstein.txt") as f:
    book_text = f.read() 
print(len(book_text.split()))
