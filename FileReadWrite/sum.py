def sum(filename):
    f = open(filename, "r")
    sum = 0
    for l in f.readlines():
        sum += int(l)
    f.close()
    f = open(filename, "a")
    f.write("\n")
    f.write(str(sum))
    f.close()
    return int(sum)


sum("test_sum.txt")