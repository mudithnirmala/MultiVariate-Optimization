INPUT FORMAT OF THE CSV FILE

N <total number of dimensions/axes>
<comma seperated intersections of planes with the first axis>
....
....
<comma seperated intersections of planes with the Nth axis>

If the longest row has x elements every other row which has y (<=x) elements should be followed by (x-y) commas

Ex1:

2,,
0,2,4
0,5,10

Ex2:

3,,,
0,2,4,
0,5,10,
0 100 200 1000

Ex3:
5,,,,,
1,100,,,,
1,1000,,,,
1,2,3,4,5,100
1,10,100,1000,,
1,100,,,,