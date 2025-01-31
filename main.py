import sys


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)


def word_count(text):
    words = text.split()
    return len(words)


def alphabet_frequency_dict(text):
    char_dict = {}
    for character in text:
        if character.lower() not in char_dict:
            char_dict[character.lower()] = 1
        else:
            char_dict[character.lower()] += 1
    sorted_list = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_list)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_only_dict = {}
    for key, value in sorted_dict.items():
        if key in alphabet:
            alphabet_only_dict[key] = value
    return alphabet_only_dict


def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document\n")
    alphabet_only_dict = alphabet_frequency_dict(text)
    for key, value in alphabet_only_dict.items():
        print(f"The '{key}' character was found '{value}' times")
    print("--- End report ---")


if __name__ == '__main__':
    sys.exit(main())