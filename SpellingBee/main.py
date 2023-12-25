import argparse
import csv


def find_possible_words(letters, center_letter):
    possible_words = []

    with open("all_words.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            word = row[0]
            word_letters = set(word)
            if word_letters.issubset(set(letters)) and center_letter in word_letters:
                possible_words.append(word)

    return possible_words


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--letters", nargs="+")
    argparse.add_argument("--center_letter", nargs=1)

    args = argparse.parse_args()

    possible_words = find_possible_words(args.letters, args.center_letter[0])

    print(possible_words)
