def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    lower_phrase = phrase.lower()
    return lower_phrase.count(letter.lower())

print(count_occurrences('CHOPPER', 'P'))