https://secweb.cs.odu.edu/~zeil/cs361/web/website/Lectures/styles/pages/editdistance.html

E.g
Convert "Zeil" => "trials"

1. If we knew how to convert "Zeil" => "trial", we could just `add` "s", done.
2. If we knew how to convert "Zei" => "trials", then we would actually have "trialsl", and we could just `remove` "l", done
3. If we know how to convert "Zei" => "trial", then we would actually have "triall", and we could just `replace` "l" => "s", done

See the recursive pattern,
Eventually, we will get down to subproblems involing empty string, such as convert "" => "abc". Then 3 `add` operations get us the result


Assume len(x) = 3, len(y) = 3
minEditDistance(3, 3)
 -> minEditDistance(3, 2)
   -> minEditDistance(3, 1)
   -> minEditDistance(2, 2)
   -> minEditDistance(2, 1)
 -> minEditDistance(2, 3)
   -> minEditDistance(2, 2)
   -> minEditDistance(1, 3)
   -> minEditDistance(1, 2)
 -> minEditDistance(2, 2)
   -> minEditDistance(2, 1)
   -> minEditDistance(1, 2)
   -> minEditDistance(1, 1)

You see we recompute the result for the same input. So we could think about DP

DP[i][j] represents the min edit number of convert the first i chars in x to the first j chars in y

x = "Zeil"
y = "trials"

     "" "t" "r"  "i"  "a"  "l"  "s"
""   0   1   2    3    4    5    6
"Z"  1   1   2    3    4    5    6
