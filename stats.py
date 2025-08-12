def get_book_text_count(book_string):
    words = book_string.split()
    return len(words)

def character_count(book_string):
    char_dict = {}
    for i in book_string:
        lower_letter = i.lower()
        if lower_letter not in char_dict:
            char_dict[lower_letter] = 1
        else:
            updated_count = char_dict[lower_letter] + 1
            char_dict[lower_letter] = updated_count
    return char_dict
            
            