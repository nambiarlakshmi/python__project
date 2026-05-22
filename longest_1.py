def longest1(num):
    ones = 0
    count_ones = 0

    while (num):
        if(num & 1 == 1):
            ones+=1
            if ones > count_ones:
                count_ones = ones
        else:
            ones = 0
        num >>= 1

    print (count_ones)


longest_one = longest1(56)
        