1. Given an array of strings `words` and a string `name`, find one substring of `name` that matches any word in `words`.
Put brackets around the matching substring in `name` and capitalize the first letter.

Sample input:
    words = ['B', 'Ar', 'O']
    name = 'aaron'

Output:
    a[Ar]on



1. Followup. Find all possible ways of breaking bad.

Sample input:
    words = ['B', 'Ar', 'O']
    name = 'aaron'


Output:
    ['a[Ar][O]n', 'aaron', 'a[Ar]on', 'aar[O]n']
