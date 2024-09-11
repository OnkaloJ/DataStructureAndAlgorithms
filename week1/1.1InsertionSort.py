def isort(A):
    for i in range (1 ,len(A)):
        j=i-1

        while j>=0 and A[j]>A[j+1]: #While loop goes trough the terms and changes them in size order
            A[j+1],A[j]=A[j],A[j+1] #Changes terms plazes if they are disorder
            j-=1


if __name__ == "__main__": 
    A = [4, 3, 6, 65, 2, 9, 7, 1, 8, 5, 78]
    isort(A)
    print(A)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
