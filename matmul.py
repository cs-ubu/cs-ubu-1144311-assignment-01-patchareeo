import numpy as np 
import csv 

'''def csv2math(filename):
    return np.array(list(csv.reader(open(filename,"rt"),delimiter=",")))
A=csv2math('A.csv') #อ่านไฟล์
b=csv2math('b.csv')'''
def readm(fname='A.csv'):
    f = open(fname,'r')#w,b
    A = []
    for line in f.readlines():
        A.append([float(x) for x in line.strip().split(',')])
        #print(A)
    f.close()
    return A
#A=readm('A.csv')
#b=readm('b.csv')

#print(A)
#print(b)
def matmul(A,b):
    m,n= len(A), len(b[0])
    J = len(A[0]) 
    if len(A[0])==len(b):
        C=[[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                # A[0][0]*b[0][0]+A[0][1]*b[1][0]+A[0][2]*b[2][0]
                C[r][c] = sum([float(A[r][j])*float(b[j][c]) for j in range(J)])

        return C
    return [] #ไม่สามารถคูณได้
#print(matmul(A,b))