def main():
    book_path = "/Users/jdpearson/workspace/github.com/Riatasthan/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_letters = count_letters(text)
    print(f"The are {num_words} words found in document")
    for key, value in num_letters.items():
        print(f'There are {value} of "{key}" in this document')
    return text

def word_count(text):
    words = text.split()
    return(len(words))

def count_letters(text):
    letter_count = {}

    for key in text:
        if key.isalpha():
            key = key.lower()
            letter_count[key] = letter_count.get(key, 0) + 1

    sorted_dict_by_keys = {k: letter_count[k] for k in sorted(letter_count)}
    sorted_dict_by_values = {k: v for k, v in sorted(letter_count.items(), key=lambda item: item[1], reverse=True)}

    #list_keys = list(letter_count.keys())
    #list_values = list(letter_count.values())
    return sorted_dict_by_values

def get_book_text(path):
    with open(path) as f:
        return f.read()    
main()
