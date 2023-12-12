def main():
    book_path = "/Users/jdpearson/workspace/github.com/Riatasthan/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in document")
    print(character_count(text))
    return text

def word_count(text):
    words = text.split()
    return(len(words))

def character_count(text):
    character = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k' : 0,
        'l' : 0,
        'm' : 0,
        'n' : 0,
        'o' : 0,
        'p' : 0,
        'q' : 0,
        'r' : 0,
        's' : 0,
        't' : 0,
        'u' : 0,
        'v' : 0,
        'w' : 0,
        'x' : 0,
        'y' : 0,
        'z' : 0
    }
    for i in text:
        if i in character:
            character[i] += 1
        else:
            character[i] = 1
    return character


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()
