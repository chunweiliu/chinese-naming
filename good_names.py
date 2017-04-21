#!/usr/bin/python
#coding:utf-8
# Add/Change the good characters collection as you need.
from good_characters_for_goat import good_characters

# Change the family name as you need.
family_name = '劉'

# Do not modify the rest.
GOOD_PAIRS = [
    (1, 2), (2, 4), (3, 5), (2, 6), (1, 7), (10, 6), (9, 7), (2, 14),
    (1, 5), (10, 7), (3, 14), (2, 15), (1, 16), (3, 15), (2, 16),
    (1, 17), (20, 4), (18, 6), (10, 14), (9, 15), (8, 16), (1, 23),
    (18, 14), (9, 23), (8, 24), (18, 15), (10, 23), (9, 24),
    (22, 15), (20, 17)
]

with open('chinese-names.txt', 'w') as f:
    for first, second in GOOD_PAIRS:
        first_characters = good_characters[first]
        second_characters = good_characters[second]
        f.write('%d %d\n' % (first, second))
        for first_character in first_characters:
            for second_character in second_characters:
                f.write('%s\n' % (family_name + first_character + second_character))
