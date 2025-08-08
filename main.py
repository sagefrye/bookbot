import sys
import stats as s

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    num_words = s.get_num_words(book_text)
    num_chars = s.get_num_chars(book_text)
    list_of_chars = s.get_list_of_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for each in list_of_chars:
        char = each["char"]
        num = each["num"]

        print(f"{char}: {num}")

    print("============= END ===============")

main()
