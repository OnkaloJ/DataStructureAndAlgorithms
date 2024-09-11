def triangle(a, b, c):
    # TODO

    #triangle largest side need to be shorter than two other side combine

    largest = max(a,b,c)

    sum_of_two_smaler = a + b + c - largest

    """if largest < sum_of_two_smaler:
        print("True")
    else:
        print("False")"""
    
    return largest < sum_of_two_smaler


if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True
