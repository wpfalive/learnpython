numbers = []

def array_append(max, step):
    i = 0
    if 0:
        while i < max:
            print "At the top i is %d" % i
            numbers.append(i)

            i += step
            print "Numbers now: ", numbers
            print "At the bottom i is %d" % i

    for i in range(0, max, step):
        #print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers


array_append(int(raw_input("input a max number: ")), 1)

print "The numbers: "

for num in numbers:
    print num
