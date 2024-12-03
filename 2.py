import numpy as np

# Returns True if it is possible to remove a single report to get a valid ordering
# Else False
def naivePartTwo(alist):
    print(f"naivePartTwo {alist=}")
    result = partOne(alist)
    i = 0
    print(result)
    while (result > 0) and i < len(alist):
        # Remove element i and try again.
        newlist = None
        if i == 0: newlist = alist[1:]
        elif i + 1 == len(alist): newlist = alist[:-1]
        else:
            newlist = alist[0:i] + alist[(i+1):]

        result = partOne(newlist)
        print(f"{alist=} {i=} {newlist=} {result=}")
        i = i + 1

    return (result == 0)

# Returns 0 if there were no unsafe reports found
# and a 1 if there was at least 1 found (there may be more)
def partOne(alist):
    print(f"partOne {alist=}")

    i = 0
    unsafe = 0
    direction = None
    while i < (len(alist) - 1):
        s = abs(alist[i+1] - alist[i])
        t = (alist[i+1] - alist[i]) > 0

        # The first time we go through we wont know the direction
        if direction is None: direction = t

        if (t != direction):
            #print(f"\t{alist=} {direction=} {i=} {s=} {t=}")
            #print(f"\tRejecting series {L=} because it switched direction at {i=}")
            unsafe = unsafe + 1
            break
        elif (s == 0 or s > 3):
            #print(f"\t{alist=} {direction=} {i=} {s=} {t=}")
            #print(f"\tRejecting series because it neither increased or decreased or too much. {s=}")
            unsafe = unsafe + 1
            break
        i = i + 1
    return unsafe

with open("2.input") as file:
    lines = file.read().split('\n')
    unsafe = 0
    total = 0
    for L in lines:
        if L == "": continue
        total = total + 1
        try:
            line = [ int(x) for x in L.split(' ') ]            
        except:
            print("error parsing", L)
            break

        x = naivePartTwo(line)
        #print(f"{line=} {x=}")
        if not x: unsafe += 1
    print(f"{unsafe=}, {total=}, safe={total-unsafe}")


"""part 1
          
            i = 0
            direction = None
            while i < (len(line) - 1):
                s = abs(line[i+1] - line[i])
                t = (line[i+1] - line[i]) > 0

                # The first time we go through we wont know the direction
                if direction is None: direction = t

                if (t != direction):
                    #print(f"{line=} {direction=} {i=} {s=} {t=}")
                    print(f"Rejecting series {L=} because it switched direction at {i=}")
                    unsafe = unsafe + 1
                    break
                elif (s == 0 or s > 3):
                    #print(f"{line=} {direction=} {i=} {s=} {t=}")
                    print(f"Rejecting series because it neither increased or decreased or too much. {s=}")
                    unsafe = unsafe + 1
                    break
                i = i + 1
"""
