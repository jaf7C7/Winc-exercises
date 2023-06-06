from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(countries):
    shortest = len(countries[0])
    for country in countries:
        if len(country) < shortest:
            shortest = len(country)
    return [c for c in countries if len(c) <= shortest]


def most_vowels(countries):
    def vowel_count(string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return len([s for s in string if s.lower() in vowels])
    return sorted(countries, key=vowel_count, reverse=True)[:3]


def alphabet_set(countries):
    # Returns a sorted list of all chars from list 'chars' contained in
    # 'string'
    def unique_chars(chars, string):
        return sorted([c for c in chars if c in string.lower()])

    # Returns the amount of unique chars of list 'chars' contained in 'string'
    def unique_char_count(chars, string):
        return len(unique_chars(chars, string))

    # Returns the string in list 'strings' which contains the most unique chars
    # of the list 'chars'
    def most_unique_chars(chars, strings):
        return sorted(
            strings,
            key=lambda s: unique_char_count(chars, s),
            reverse=True
        )[0]

    # Returns the shortest (hopefully!) list of items from list 'strings' whose
    # items contain all characters in the list 'chars'
    def complete_set(chars, strings, result=[]):
        if chars == []:
            return result
        selection = most_unique_chars(chars, strings)
        result.append(selection)
        strings.remove(selection)
        for c in unique_chars(chars, selection):
            chars.remove(c)
        return complete_set(chars, strings, result)

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    return complete_set(alphabet, countries)


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
