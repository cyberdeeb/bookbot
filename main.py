def main():
    path = 'books/frankenstein.txt'
    book = get_book(path)
    num_words = get_num_words(book)
    num_characters = get_num_characters(book)
    generate_report(num_words, num_characters, path)
    

def sort_on(dict):
    return dict["num"]


def generate_report(word_report, character_report, path):
    character_report_list = []
    for character in character_report:
        character_report_list.append({"ch" : character, "num" : character_report[character]})
    character_report_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f'{word_report} words found in the documnet')
    print()

    for letter in character_report_list:
        print(f"The '{letter['ch']}' character was found {letter['num']} times")

    print("--- End report ---")
    
    

def get_num_characters(book):
    character_dict = {}
    lower_book = book.lower()
    
    for character in lower_book:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return character_dict

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        book = f.read()
        return book
    
main()