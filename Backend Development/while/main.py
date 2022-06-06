from itertools import count
from re import I
from turtle import begin_fill
from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

    
    
# function unique_koala_facts 
    # integer --> parameter, iteration limit of 1000
    # Return unique facts in the dataset
def unique_koala_facts(x):
    i = 0
    unique_facts = []
    while i < 1000:
            all_facts = random_koala_fact()
            i += 1
            if all_facts not in unique_facts:
                if len(unique_facts) != x:
                    unique_facts.append(all_facts)
                else:
                    break
    return(unique_facts) 

#Function num_joey_facts
    # count joeys in unique facts in facts dataset
    # if you seen some particular fact 10 times, then return how many unique joey facts you counted in dataset


def num_joey_facts():
    random_fact = (random_koala_fact())
    times_seen_random_fact = 0
    joey_fact_counter = 0
    unique_facts = []
    
    while times_seen_random_fact < 10:
        new_facts = random_koala_fact()
        if new_facts == random_fact:
                times_seen_random_fact += 1
        if new_facts not in unique_facts:
                unique_facts.append(new_facts)
                if "joey" in new_facts:
                 joey_fact_counter += 1

    return joey_fact_counter
# function koala_weight 
    # how heavy koala is. should return that weigt in kilogram as integer


def koala_weight():
    fact = random_koala_fact()
    while 'kg' not in fact:
        fact = random_koala_fact()
        name = fact[-5:-3]
    return int(name)

def main():
    num_joey_facts()
    print(koala_weight())
    unique_koala_facts(0)

if __name__ == "__main__":
    print(random_koala_fact())
    main()
