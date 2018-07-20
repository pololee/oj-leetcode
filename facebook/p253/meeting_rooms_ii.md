Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.


### Solution 1:
The idea is to constuct a timeline.
We check every interval.
At the start time of the interval, on the timeline, we use +1 to represent allocate a room
At the end time of the interval, on the timeline, we use -1 to represent release a room.

So we can use a map. The key is timestamp. The value is the number of rooms after we allocate and release room at that timestamp
