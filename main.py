from stats import get_book_text_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_book_text_count(book_text)
    print(f"{word_count} words found in the document")
    char_count = character_count(book_text)
    print(char_count)
    

main()