def changes(A):
    
    count=0

    for i in range (1, len(A)):

        if A[i] == A[i-1]:
            A[i] = A[i-1] + 7839208
            count+=1
    
    return count


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2