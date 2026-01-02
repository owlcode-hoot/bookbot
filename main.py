from stats import get_num_words, count_characters, create_report, sort_on
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
    count = get_num_words(file_contents)
    characters = count_characters(file_contents)
    ch_list = create_report(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"Found {count} total words ")
    print("--------- Character Count -------")
    for ch in ch_list:
        entry = ch["char"]
        if entry.isalpha():
            print(f"{ch['char']}: {ch['num']}")
    print("============= END ===============")
    print(sys.argv)



main()