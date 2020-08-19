A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input Description:
First line contains, Row and Col.(1<Row,Col<100)

Output Description:
Print the super meeting point.(minimize the total travel distance)

Sample Input:
5 3
1 0 0 0 1 0 0 0 0 0 0 0 1 0 0

Sample Output:
6

Explanation:
Given three people living at (0,0), (0,4), and (2,2):
The point (0,2) is an ideal meeting point, as the total travel distance 
of 2+2+2=6 is minimal. So return 6.

Sample Input:
2 3
1 0 1 0 0 1

Sample Output:
3

Sample Input:
3 4
1 1 1 0 0 0 0 0 1 0 1 0

Sample Output:
8

Sample Input:
3 3
0 0 1 1 1 0 1 1 1

Sample Output:
8

Sample Input:
4 2
0 0 0 0 1 1 1 1

Sample Output:
4

Sample Input:
5 5
1 0 0 1 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 0 0 1 1 1 0

Sample Output:
30
