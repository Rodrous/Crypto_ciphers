import numpy as np
matrix1 = [['0101', '1100', '1010', '1101'],['0000', '0110', '1011', '1111'],['0100', '0111', '1110', '1001'],['1000', '0011', '0001', '0010']]

matrix2 = [['0100','1110','1111','1101'], ['1000','0000','0101','1001'],['1100','1011','0010','0110'],['0001','0011','1010','0111']]

def dict_mapping(string):
    dict1 = {'00': 0,'01': 1,'10': 2,'11': 3}
    map1 = dict1[string[:2]]
    map2 = dict1[string[2:]]
    print(map1,map2)
    return map1,map2


def invertibleOrNot(first, second):
    if np.shape(first) == np.shape(second):
        for i in range(len(first)):
            for j in range(len(first)):
                temp = first[i][j]
                x, y = dict_mapping(temp)
                a, b = dict_mapping(second[x][y])
                if (a == i) and (b == j):
                    pass
                else:
                    return 'Not invertible'
        return 'Invertible!'
    else:
        return 'Not Invertible'

print(invertibleOrNot(matrix1,matrix2))