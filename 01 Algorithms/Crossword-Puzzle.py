'''
A 10 X 10 Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid.
The cells in the grid are initially, either + signs or - signs.
Cells marked with a + have to be left as they are. Cells marked with a - need to be filled up with an appropriate character.

Input Format

The input contains 10 lines, each with 10 characters (which will be either + or - signs).
After this follows a set of words (typically nouns and names of places), separated by semi-colons (;).

Constraints

There will be no more than ten words. Words will only be composed of upper-case A-Z characters. There will be no punctuation (hyphen, dot, etc.) in the words.

Output Format

Position the words appropriately in the 10 X 10 grid, and then display the 10 X 10 grid as the output. So, your output will consist of 10 lines with 10 characters each.

Sample Input 0

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

Sample Output 0

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++

Sample Input 1

+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR

Sample Output 1

+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++


'''