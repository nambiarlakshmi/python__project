def reverse_bits(a):
    result = 0

    while a > 0:
        bit = a & 1          
        result = (result << 1) | bit
        a = a >> 1           

    print(result)

reverse_bits(11)

        
