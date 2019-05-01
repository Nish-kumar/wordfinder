# wordfinder
Search words in a matrix on all directions( not zig zag) and displays the output like a matrix with highlighted search words


**This is a fun project which I have taken to compete with my fellow developers**. 

The idea is to find the given words within a given matrix of characters and identify at which index the given words are in the matrix. 
The code in python takes the matrix of characters and no of words to search as an input. It is not basically new, but the algorithm which is 
used to search for the words is different, which is efficient in some cases. So, the approach is to concatenate all the characters from the matrix horizontally,
vertically and diagonally into list of strings along with their index values and then search for the words in the list and get the indices of the found words.
These indices are highlighted while displaying the output matrix
