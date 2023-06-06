from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(x):
    unique_koala_facts = []
    i = 0
    while i < 1000 and len(unique_koala_facts) < x:
        koala_fact = random_koala_fact()
        if koala_fact not in unique_koala_facts:
            unique_koala_facts.append(koala_fact)
        i += 1
    return unique_koala_facts


def num_joey_facts():
    joey_facts = []
    fact_0 = random_koala_fact()
    i = 0
    while i < 10:
        koala_fact = random_koala_fact()
        if koala_fact == fact_0:
            i += 1
        if (koala_fact not in joey_facts and
                ('joey' in koala_fact or 'Joey' in koala_fact)):
            joey_facts.append(koala_fact)
    return len(joey_facts)


def koala_weight():
    while True:
        koala_fact = random_koala_fact()
        if 'kg' in koala_fact:
            # 'A koala blah blah... <num>kg'
            koala_fact = koala_fact[:koala_fact.rfind('kg')]
            # '<num>'
            return int(koala_fact[koala_fact.rfind(' ')+1:])


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(koala_weight())
