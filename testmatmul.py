from matmul import readm,matmul

A = readm('A.csv')
b = readm('b.csv')
c = matmul(A,b)
print(c)