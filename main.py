import sys

from stats import get_book_text_count, character_count, chars_dict_to_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
    return file_contents
    
def main():
    book_text = get_book_text(sys.argv[1])
    word_count = get_book_text_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count_dict = character_count(book_text)
    print("--------- Character Count -------")
    sorted_char_count_dict = chars_dict_to_sorted_list(char_count_dict)
    for item in sorted_char_count_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

main()