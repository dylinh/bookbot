from stats import count_words, count_characters, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted_list(count_characters(book_text))
    for obj in sorted_chars:
        if obj["char"].isalpha():
            print(f"{obj["char"]}: {obj["num"]}")
    print("============= END ===============")
main()