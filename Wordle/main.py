import re


def prune_correct_letters(words: set) -> set:
    correct_letters = input("Please enter letters that are correct and their place: ")

    # an empty string is ok to have. If we do have it though, exit out early
    if not correct_letters:
        return words

    correct_guess = correct_letters.split(",")
    remove_words = set()
    print(correct_guess)
    for letter in correct_guess:
        letter = letter.strip()
        letter, index = letter.split(" ")
        index = int(index) - 1

        for word in words:
            if word[index] != letter:
                if word == "malts":
                    print(letter, index)
                remove_words.add(word)

    for word in remove_words:
        words.remove(word)

    return words


def prune_contain_letters(words: set) -> set:
    """
    Removed words that do not contain the letters in the guess.

    Args:
        words (set): valid words to select

    Returns:
        set: new set of valid words
    """
    contain_letters = input("Please enter letters that are in the word: ")

    if not contain_letters:
        return words

    remove_words = set()
    contain_letters = contain_letters.strip().split(" ")
    for letter in contain_letters:
        for word in words:
            if letter not in word:
                remove_words.add(word)

    for word in remove_words:
        words.remove(word)

    return words


def get_feedback(words: set) -> set:
    """
    Get user feedback on their guess. Enter in the format, letter SPACE word index. If multiple,
    then separate with commas.

    Args:
        None

    Returns:
        Pruned list of words
    """

    words_prune = prune_correct_letters(words)
    words = prune_contain_letters(words_prune)

    return words


def main():
    with open("five_letter_words.csv") as f:
        words = f.read().splitlines()

        # make set of words
        words = set(words)

    guesses = 1

    while guesses < 6:
        words = get_feedback(words)
        guesses += 1
        print(f"{len(words)} words left.")
        print(words)

    print("Guesses are exhausted. I hope you got it.")


if __name__ == "__main__":
    main()
