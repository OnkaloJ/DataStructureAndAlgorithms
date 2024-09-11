def primes(N: int) -> int:
    # TODO
    #best way to do it is use erathosten algorithm

    prime_numbers = [True] * (N+1)

    prime_numbers[0]=False  #because 0 and 1 is not primenumbers
    prime_numbers[1]=False

    i = 2

    while i*i<=N:
        if prime_numbers[i]:
            for multiple in range (i*i, N+1, i): # Delete every numbers what is i multiply
                prime_numbers[multiple]=False
        i+=1 # Work because there is deleted every numbers multiply what is not primary number

    return sum(prime_numbers) #Calculate how many true is left
        

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15
