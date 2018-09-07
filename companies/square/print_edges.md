"""
input is ASCII-art representation of graph
A graph has nodes (represented by letters) connected by edges (represented by hyphens or pipes)

example input:
A----B---C
|
|
D

possible chars in input: letters, hyphens, pipes, spaces
type of input: choose ONE (whichever is easier for you): either a list of strings (each is one line), OR a single string, with newlines inside it

output the edges of the graph:
AB
BC
AD
(order doesn't matter)
(OK to have both AB and BA)
    either AB BC AD (3 elements)
    or AB BA BC CB AD DA (6 elements)
    both of the above are acceptable outputs
    but AB BA BC AD would be inconsistent

possible input w/ spaces:
A----B---C
     |
     |
     D

example w/ verticals:

A
|
B
|
C

we want to be careful, do not want to output AC (only want AB and BC)


Feel free to:
* use the supported language you're most comfortable with.
* look up any standard libraries, etc. on the internet.
* tell me what you want to look up, I'm happy to help if I happen to know the answer, or I can help look up at the same time.
* run the code at any point and as often as you like; it doesn't have to be perfect the first time
"""
