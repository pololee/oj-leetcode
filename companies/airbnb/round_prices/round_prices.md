Given A = [x1, x2, ..., xn]
Sum T = Round(x1+x2+... +xn)

floors of all AFloors = [f1, f2, ..., fn]
ceilings of all ACeilings = [c1, c2, ..., cn]
so sum(AFloors) <= T <= sum(ACeilings)

assume:
floorSum = sum(AFloors)

diff = T - floorSum
if diff > 0: 
sorted A by absCeilDiff, the first diff number of element in sorted A,
we pick the ceiling, others we pick floor

[1.2, 1.4]
floorSum = 2
T = round(2.6) = 3
3 - 2 = 1

sorted [(1.4, 0.6), (1.2, 0.8)]

so the final result is [1, 2]
