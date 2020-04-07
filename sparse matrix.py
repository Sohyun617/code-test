#(1) 배열 representation
sparseMatrix = [[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]]  #하나의 희소행렬을 가정

print(sparseMatrix)

 
size = 0
  
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            size += 1
  
rows, cols = (3, size) # compactMatrix = row,column,value 로 구성됨. ex) 0행 2열의 값은 3이다.
compactMatrix = [[0 for i in range(cols)] for j in range(rows)] 
  
k = 0
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            compactMatrix[0][k] = i 
            compactMatrix[1][k] = j 
            compactMatrix[2][k] = sparseMatrix[i][j] 
            k += 1
  
for i in compactMatrix: 
    print(i) 
    
# 이외에도 Linked Lists, List of Lists, Dictionary of Keys 을 이용한 방법들이 있음.
