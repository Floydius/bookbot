from stats import get_word_count
from stats import get_sorted_chars
import sys

def main():
    print(f'============ BOOKBOT ============\nAnalyzing book found at {book}...')
    num_words = get_word_count(book)
    print(f'----------- Word Count ----------\nFound {num_words} total words')
    print('--------- Character Count -------')
    sorted_chars = get_sorted_chars(book)
    for dict in sorted_chars:
        print(f'{dict["char"]}: {dict["num"]}')
    print('============= END ===============')

if len(sys.argv) < 2:
    print(f'Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    book = sys.argv[1]
    main()