def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    count = get_num_words(file_contents)
    print(f"Found {count} total words")
    characters = count_characters(file_contents)
    print(characters)

from stats import get_num_words, count_characters, create_report, sort_on

main()