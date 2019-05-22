
def sum_of_multiples(factors, below):
    sum = 0
    for i in range(1, below):
        for f in factors:
            if i%f == 0:
                #print i
                sum += i
                continue
    return sum


if __name__ == "__main__":
    print sum_of_multiples([3, 5], 1000)
