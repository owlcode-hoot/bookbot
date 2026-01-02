from stats import get_num_words, count_characters, create_report, sort_on


def main():
    path_to_file = "books/frankenstein.txt"
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



main()