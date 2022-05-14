from operator import add
from unittest import result
from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`


def shortest_names(countries):
    short_names = []
    for i in countries:
        if len(i) == len(min(countries, key=len)):
            short_names.append(i)
    return(short_names)


def most_vowels(countries):
    vowel = ["a", "e", "i", "o", "u"]
    count_per_country = []
    for country in countries:
        lowercase_country = country.lower()
        count = 0
        for char in lowercase_country:
            if char in vowel:
                count = count + 1
        count_per_country.append(count)

    countries_per_count = [i for _, i in sorted(zip(count_per_country, countries))]
    countries_per_count.reverse()
    return(countries_per_count[0:3])


def alphabet_set(countries):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    countries_alphabet_set = []
    countries_sorted = sorted(countries, key=len, reverse=True)
    for i in countries_sorted:
        i_lowercase = i.lower()
        for char in i_lowercase:
            if char in alphabet:
                alphabet.remove(char)
                if i not in countries_alphabet_set:
                    countries_alphabet_set.append(i)
        else:
            pass
    return(countries_alphabet_set)




""" Write the calls to your functions here. """


def main():
    shortest_names(countries)
    most_vowels(countries)
    alphabet_set(countries)


if __name__ == "__main__":
    countries = get_countries()
    main()
