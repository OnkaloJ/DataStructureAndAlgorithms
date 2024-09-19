def split(T):

    count=0

    left_max=0
    right_min=0

    #right_min[0]=T[0]
    #for i in range (1,len(T)):
    #    right_min[i]=max(right_min[i-1],T[i])
    #print (right_min)


    for i in range(1,len(T)):

        right_side=T[i:]
        right_min=min(right_side)

        if T[i-1]>left_max:
            left_max=T[i-1]

        if left_max<right_min:

            count+=1
            


    return count

if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))
    print(split([5, 4, 3, 2, 1]))
    print(split([2, 1, 2, 5, 7, 6, 9]))
    print(split([1, 2, 3, 1]))