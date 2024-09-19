def pairs(s):
    distance = 0
    ones_count=0
    ones_index=0

    for i in range (0,len(s)):

        if s[i] == '1':
            distance+= ones_count*i-ones_index
            ones_count+=1
            ones_index+=i
     

    return distance

if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71
