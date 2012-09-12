#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------


# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

#def collatz_eval (i, j) :
def collatz_eval (i, j, a) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
# Dumb Algorithm
##    cycleMax = 0
##    for x in range(i, j+1):
##        count = 1
##        while (x != 1):
##            count += 1
##            if x % 2 == 0:
##                x /= 2
##            else:
##                x = (3*x) + 1
##        cycleMax = max(count, cycleMax)
##    assert cycleMax > 0
##    return cycleMax

# Pre-Comp Array    
    cycleMax = 0
    c = max(i,j)
    b = min(i,j)
    for x in range(b,c+1):
        assert x > 0
        
        count = 1
        if x <= 100000:
            cycleMax = max(cycleMax, a[x-1])
        else:
            while (x != 1 and x > 100000):
                #count += 1
                if x % 2 == 0:
                    x /= 2
                else:
                    x = (3*x) + 1
                    
            if x <= 100000:
                count += a[x-1]
            else:
                count += 1
            cycleMax = max(cycleMax, count)
                

    assert cycleMax > 0
    return cycleMax
##    
##    cycleMax = 0
##    for x in range(i, j+1):
##        count = 1
##        while (x != 1):
##            count += 1
##            # Even
##            if x % 2 == 0:
##                x = (3*x) + 1
##            # Odd
##            else:
##                x /= 2
##        cycleMax = max(count, cycleMax)
##    assert cycleMax > 0
##    return cycleMax

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
# Pre Comp Array
    n = 100000
    preCompArray = [0]*n
    for ind in range(n):
        findNum = ind + 1
        count = 1
        while (findNum != 1 and ((findNum-1) >= n or preCompArray[findNum - 1] == 0)):
            if (findNum % 2) == 0:
                findNum /= 2
            else:
                findNum = (3*findNum) + 1
            if ((findNum-1) >= n or ((findNum - 1) < n and preCompArray[findNum-1] == 0)):
                count += 1
        if(preCompArray[findNum - 1] != 0):
            count += preCompArray[findNum - 1]
        preCompArray[ind] = count
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1], preCompArray)
        collatz_print(w, a[0], a[1], v)


##    a = [0, 0]
##    while collatz_read(r, a) :
##        v = collatz_eval(a[0], a[1])
##        collatz_print(w, a[0], a[1], v)
