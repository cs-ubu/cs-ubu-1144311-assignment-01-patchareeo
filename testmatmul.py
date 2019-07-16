'''from matmul import readm,matmul

A = readm('A.csv')
b = readm('b.csv')
c = matmul(A,b)
print(c)'''

from matmul import readm,matmul
AA = 'A.csv'
BB = 'b.csv'
print(matmul(readm(AA),readm(BB)))
