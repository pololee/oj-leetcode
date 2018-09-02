https://secweb.cs.odu.edu/~zeil/cs361/web/website/Lectures/styles/pages/editdistance.html

E.g
Convert "Zeil" => "trials"

1. If we knew how to convert "Zeil" => "trial", we could just `add` "s", done.
2. If we knew how to convert "Zei" => "trials", then we would actually have "trialsl", and we could just `remove` "l", done
3. If we know how to convert "Zei" => "trial", then we would actually have "triall", and we could just `replace` "l" => "s", done

See the recursive pattern,
Eventually, we will get down to subproblems involing empty string, such as convert "" => "abc". Then 3 `add` operations get us the result
