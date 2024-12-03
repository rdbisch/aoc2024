import sys
import numpy as np

if __name__ == "__main__": 
    filename = sys.argv[1]
    results = []

    with open(filename) as file:
        contents = file.read()

        state = 0
        part2 = True
        enabled = True   #part 2
        for c in contents:
            print(f"{state=} {c=} {enabled=}")
            if state == 0:
                if c == 'm':
                    if part2 and not enabled: state = 0
                    else: state = 1
                elif part2 and c == 'd':
                    state = 100
                else:
                    pass
            elif state == 1:
                if c == 'u': state = 2
                else: state = 0
            elif state == 2:
                if c == 'l': state = 3
                else: state = 0
            elif state == 3:
                if c == '(':
                    state = 4
                    arg1 = ""
                else: state = 0
            elif state == 4:
                if c >= '0' and c <= '9':
                    arg1 = arg1 + c
                elif c == ',':
                    state = 5
                    arg2 = ""
                else: state = 0
            elif state == 5:
                if c >= '0' and c <= '9':
                    arg2 = arg2 + c
                elif c == ')':
                    results.append((int(arg1), int(arg2)))
                    state = 0
                else: state = 0
            elif state == 100:
                if c == 'o': state = 101
                else: state = 0
            elif state == 101:
                if c == 'n': state = 102
                elif c == '(': state = 103
                else: state = 0
            elif state == 102:
                if c == "'": state = 104
                else: state = 0
            elif state == 103:
                if c == ')':
                    print("Toggle")
                    enabled = True
                    state = 0
                else: state = 0
            elif state == 104:
                if c == 't': state = 105
                else: state = 0
            elif state == 105:
                if c == '(': state = 106
                else: state = 0
            elif state == 106:
                if c == ')':
                    print("Toggle")
                    enabled = False
                state = 0                
            else:
                raise RuntimeError("invalid state")
    
    print(results)
    sum = 0
    for x, y in results:
        sum += x*y
    print(sum)