import numpy as np

def word_search(matrix, word):
    se = []
    
    A = np.array(matrix)
    tmatrix = A.transpose()

    for i in range(4):
        p = matrix[i]
        q = ''.join(p)
        se.append(q)
        p1 = tmatrix[i]
        q1 = ''.join(p1)
        se.append(q1)

    for i in range(8):
        if se[i] == word:
             return True
        
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM'))
