R=int(input("Enter the number of Rows:"))
C=int(input("Enter the number of Columns:"))
matrix=[]
# creating a matrix using nested lists.
for i in range(R):
    print("Enter the elements of row ", i+1)
    a =[]
    for j in range(C):
        a.append(int(input(f"enter the value at {i+1}th row and {j+1}th column:")))
    matrix.append(a)
K=int(input("Enter the integer you would like to check presence of:\n"))
presence =0 # variable to store presence of number
i1=0 # variable to store index 1
i2=0 # variable to store index 2
# running through each element of matrix to find presence
for i in range(R):
    for j in range(C):
        if matrix[i][j] == K:
            i1=i
            i2=j
            presence=1
            break
if presence ==1:
    print(f"True,The value {K} is present in the matrix")
    print(f"The index of the element is {i1},{i2}")

else:
    print(f"False,The value {K} is not present in the matrix")