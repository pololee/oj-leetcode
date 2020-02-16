# Reservior Sampling
## Definition
Reservoir sampling is a family of randomized algorithms for randomly choosing a sample of k items from a list S containing n items, where n is either a very large or unknown number. Typically n is large enough that the list doesn't fit into main memory.

## Algorithm R
```
(*
  S has items to sample, R will contain the result
  assuming k < n and using one-based array indexing
 *)
ReservoirSample(S[1..n], R[1..k])
  // fill the reservoir array
  for i = 1 to k
      R[i] := S[i]

  // replace elements with gradually decreasing probability
  for i = k+1 to n
    j := random(1, i)   // important: inclusive range
    if j <= k
        R[j] := S[i]
```

## Explanation

At the i-th element of S, the algorithm generates a random number j between 1 and i inclusive.

If j <= k, the j-th element of the reservior array R is replaced with S[i].

The probability of j <= k is k/i.
So for all i, the i-th element of S is chosen to be included in the reservior with probability k/i.

So at each iteration, the j-th element of R is chosen to be kicked off with probability
k/i * 1/k, which is equal to 1/i

It can be shown that when the algorithm has finished executing, each item in S has equal probability k/length(S) of being chosen for the reservoir.

## Proof by Induction
prob = k / length(S)

Assume after (i-1) iteration, the probability of a number being in reservior is k/(i-1)
At i-th iteration,
the probability of an element in the reservior being replaced is 1/i
So the probability it survives is (1 - 1/i) = (i-1)/i
So the probability that a given number is still in the reservior after i-th iteration is
the probability of being in the reservior after (i-1) iteration * surviving replacement in i-th iteration.
k/(i-1) * (i-1)/i = k/i

So the result holds for i, and is therefore true by induction
