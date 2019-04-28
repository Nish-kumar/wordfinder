"""
Two arguments needed for this .py script.
1. Matrix with individual characters as csv file
2. File with search words
"""

import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install('colorama')
import csv
from colorama import init
init()

"""
This function reads a csv file and returns a the values as a matrix
"""


def get_matrix(filename):
    """ Read the CSV file """
    src_mat = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        val = []
        """ store the given values as 2D list src_mat """
        for row in csv_reader:
            val.clear()
            for ind in range(len(row)):
                val.append(row[ind])
            src_mat.append(val.copy())
        print('The given Matrix is: ')
        print(src_mat)
    return src_mat


""" This function concatenates the diagonal characters in the matrix from left to right and returns a list of strings
and the corresponding string indices as strings
EX:
mat = [ a,b,c
		d,e,f
		g,h,i]
result = [['a','db','gec','hf','i'],['0 0',  '1 0,0 1',  '2 0,1 1,0 2',  '2 1,1 2',  '2 2']]
 """


def LtoRcross(matrix, size):
    val = ''
    diagonal_string = []
    diagonal_string_indices = []
    previndex = []
    currindex = []
    derivedindex = []

    # print(diagonal_string)
    for n in range(size[0] + size[1] - 1):
        if n == 0:
            val = matrix[0][0]
            # print(val)
            currindex.append('00')
            derivedindex.append('0 0')
        preval = val
        if n > 0:
            previndex = derivedindex.copy()
            currindex.clear()
            derivedindex.clear()
            dum = 0
            val = ''
            for a in previndex:
                # print(matrix[int(a[0])]+matrix[int(a[1])])
                # previndex = str(indexfind(matrix,a))
                # print('previndex is :',previndex)
                indx = int(a.split(' ')[0])
                indy = int(a.split()[-1])
                # print(indx,indy)
                if dum == 0:
                    if indx + 1 != len(matrix) and indy + 1 != len(matrix[0]):
                        val = val + matrix[indx + 1][indy] + matrix[indx][indy + 1]
                        currindex.append(str(indx + 1) + str(indy))
                        currindex.append(str(indx) + str(indy + 1))
                        derivedindex.append(str(indx + 1) + str(' ') + str(indy))
                        derivedindex.append(str(indx) + str(' ') + str(indy + 1))
                    # print('hi:',val)
                    elif indy + 1 != len(matrix[0]):
                        val = val + matrix[indx][indy + 1]
                        currindex.append(str(indx) + str(indy + 1))
                        derivedindex.append(str(indx) + str(' ') + str(indy + 1))
                else:
                    if indy + 1 != len(matrix[0]):
                        val = val + matrix[indx][indy + 1]
                        currindex.append(str(indx) + str(indy + 1))
                        derivedindex.append(str(indx) + str(' ') + str(indy + 1))
                dum += 1
            # print('dum',dum)
        # print(val)
        str1 = ''
        for i in currindex:
            str1 += i
        str2 = ''
        for i in derivedindex:
            str2 = str2 + i + str(',')
        diagonal_string.append(val)
        diagonal_string_indices.append(str2)
    return diagonal_string, diagonal_string_indices

""" This function concatenates the diagonal characters in the matrix from right to left and returns a list of strings
and the corresponding string indices as strings
EX:
mat = [ a,b,c
		d,e,f
		g,h,i]
result = [['c','fb','iea','hd','g'],['0 2',  '1 2,0 1',  '2 2,1 1,0 0',  '2 1,1 2',  '2 0']]
 """


def RtoLcross(matrix, size):
    val = ''
    diagonal_string = []
    previndex = []
    currindex = []
    derivedindex = []
    diagonal_string_indices = []
    # print(diagonal_string)
    for n in range(size[0] + size[1] - 1):
        if n == 0:
            val = matrix[0][len(matrix[0]) - 1]
            # print(val)
            currindex.append('0' + str(len(matrix[0]) - 1))
            derivedindex.append('0' + str(' ') + str(len(matrix[0]) - 1))
        preval = val
        if n > 0:
            previndex = derivedindex.copy()
            currindex.clear()
            derivedindex.clear()
            dum = 0
            val = ''
            for a in previndex:
                # print(matrix[int(a[0])]+matrix[int(a[1])])
                # previndex = str(indexfind(matrix,a))
                # print('previndex is :',previndex)
                indx = int(a.split(' ')[0])
                indy = int(a.split(' ')[-1])
                # print(indx,indy)
                if dum == 0:
                    if indx + 1 < len(matrix) and indy - 1 >= 0:
                        val = val + matrix[indx + 1][indy] + matrix[indx][indy - 1]
                        currindex.append(str(indx + 1) + str(indy))
                        currindex.append(str(indx) + str(indy - 1))
                        derivedindex.append(str(indx + 1) + str(' ') + str(indy))
                        derivedindex.append(str(indx) + str(' ') + str(indy - 1))
                        # print('hi:',val)
                    elif indy - 1 >= 0:
                        val = val + matrix[indx][indy - 1]
                        currindex.append(str(indx) + str(indy - 1))
                        derivedindex.append(str(indx) + str(' ') + str(indy - 1))
                else:
                    if indy - 1 >= 0:
                        val = val + matrix[indx][indy - 1]
                        currindex.append(str(indx) + str(indy - 1))
                        derivedindex.append(str(indx) + str(' ') + str(indy - 1))
                dum += 1
                # print('dum',dum)
            # print(val)
        str1 = ''
        str2 = ''
        for i in currindex:
            str1 = str1 + i
        for i in derivedindex:
            str2 = str2 + i + str(',')
        diagonal_string.append(val)
        diagonal_string_indices.append(str2)
    return diagonal_string, diagonal_string_indices


""" This function concatenates the row characters in the matrix and returns a list of strings
and the corresponding string indices as strings
EX:
mat = [ a,b,c
		d,e,f
		g,h,i]
result = [['abc','def','ghi'],['0 0,0 1,0 2',  '1 0,1 1,1 2',  '2 0,2 1,2 2']]
 """


def LtoRrow(matrix, size):
    row_string = []
    row_string_indices = []
    for i in range(size[1]):
        str2 = ''
        str_row = ''
        str_row_ind = ''
        str_ind = ''
        for j in range(size[0]):
            str1 = matrix[i][j]
            str2 = str2 + str1
            ind1 = str(i) + str(' ') + str(j) + str(',')
            str_ind = str_ind + ind1
        # print(str2)
        str_row = str_row + str2
        str_row_ind = str_row_ind + str_ind
        row_string.append(str_row)
        row_string_indices.append(str_row_ind)
    return row_string, row_string_indices


""" This function concatenates the column characters in the matrix and returns a list of strings
and the corresponding string indices as strings
EX:
mat = [ a,b,c
		d,e,f
		g,h,i]
result = [['adg','beh','cfi'],['0 0,1 0,2 0',  '0 1,1 1,2 1',  '0 2,1 2,2 2']]
 """


def TtoBCol(matrix, size):
    column_string = []
    column_string_indices = []
    for j in range(size[0]):
        str2 = ''
        str_row = ''
        str_row_ind = ''
        str_ind = ''
        for i in range(size[1]):
            str1 = matrix[i][j]
            str2 = str2 + str1
            ind1 = str(i) + str(' ') + str(j) + str(',')
            str_ind = str_ind + ind1
        # print(str2)
        str_row = str_row + str2
        str_row_ind = str_row_ind + str_ind
        column_string.append(str_row)
        column_string_indices.append(str_row_ind)
    return column_string, column_string_indices


"""
This function searches for the given string in the list and returns the corresponding index value of the string from the matrix
EX:
source_list = [['bcatr'],['0 0,0 1,0 2,0 3,0 4']]
search_word = 'cat'
result = ['0 1','0 2','0 3']
"""


def search(string_list, search_string):
    dum = 0
    index_in_matrix = []
    for val in string_list[0]:
        for tgtval in search_string:
            if (val.find(tgtval) != -1):
                print("YES")
                print(tgtval)
                #print(dum)
                start = val.find(tgtval)
                #print(start)
                # t = string_list[1][dum].split(',')
                # print(t[11])
                # print(t)
                print(string_list[0][dum][start:start + len(tgtval)])
                res = string_list[1][dum].split(',')[start:start + len(tgtval)]
                print(res)
                index_in_matrix.append(res)
        dum += 1
    return index_in_matrix


"""
This function get all the values from a 2d list and creates a 1D list
"""


def twoDtoD(src_list):
    Dlist = []
    for a in range(len(src_list)):
        for r in range(len(src_list[a])):
            Dlist.append(src_list[a][r])
    return (Dlist)


""" This function converts the indices of a value in a matrix to the index of a string which has each row seperated by a \n characters
EX:
matrix = [a b c
		  d e f
		  g h i]
Index of e = 1,1(input)
matrix as string = 'abc\ndef\nghi'
index of e = 5(result)
 """


def convert_index(ind_row, ind_col, matrix):
    if ind_row > 0:
        pos = len(matrix[0]) * (ind_row) + ind_row
        return pos + ind_col
    else:
        return ind_row + ind_col


"""
Main function
"""
def main(file, searchword):
    src_mat = get_matrix(file)
    matrix_size = []
    matrix_size.append(len(src_mat[0]))
    matrix_size.append(len(src_mat))
    print('The Size of the given Matrix is : ')
    print(matrix_size)

    """ read the search words file """
    with open(searchword, 'r') as f:
        x = f.readlines()
    """ get the search words in a list along with its reverse value """
    searchstr = []
    for line in x:
        searchstr.append(line.rstrip('\n'))
        searchstr.append(line.rstrip('\n')[::-1])
    print('The Search words are :')
    print(searchstr)
    """ Get all the concatenated caharcters from the matrix in all directions"""
    diagonal_string1 = LtoRcross(src_mat, matrix_size)
    diagonal_string2 = RtoLcross(src_mat, matrix_size)
    row_string = LtoRrow(src_mat, matrix_size)
    column_string = TtoBCol(src_mat, matrix_size)

    """ Search the words in the above strings and get the corresponding index  values if they matched """
    diag_res1 = search(diagonal_string1, searchstr)
    diag_res2 = search(diagonal_string2, searchstr)
    row_res = search(row_string, searchstr)
    Column_res = search(column_string, searchstr)
    """ Get all the indices which matched in to a single list"""
    allind = []
    if (len(diag_res1)) > 0:
        allind.append(twoDtoD(diag_res1))
    if (len(diag_res2)) > 0:
        allind.append(twoDtoD(diag_res2))
    if (len(row_res)) > 0:
        allind.append(twoDtoD(row_res))
    if (len(Column_res)) > 0:
        allind.append(twoDtoD(Column_res))
    #print(allind)

    final_all_indices = twoDtoD(allind)
    print(final_all_indices)

    """ Convert the matrix into a single string by adding \n at each row"""
    onedstring = '\n'.join([''.join([str(cell) for cell in row]) for row in src_mat])
    print(onedstring)

    """ Convert the indices of 2D Matrix into the index of the string from the above result """
    finalindexonedstring = []
    for a in final_all_indices:
        ci = a.split(' ')
        cr = a.split(' ')
        #print(ci[0], cr[-1])
        f = convert_index(int(ci[0]), int(cr[-1]), src_mat)
        finalindexonedstring.append(f)

    finalindexonedstring.sort()

    print(finalindexonedstring)

    """ Highlight the identified index values while printing the string """
    string_to_display = ''
    for a in range(len(onedstring)):
        if a in finalindexonedstring:
            string_to_display = string_to_display + "\033[1;34;40m" + str(onedstring[a] + ' ')
        else:
            string_to_display = string_to_display + "\033[0;31;40m" + str(onedstring[a] + ' ')

    print(string_to_display)


if __name__ == '__main__':
    main(str(sys.argv[1]),str(sys.argv[2]))
