def chop(t=[]):
    midlt = t.pop(0)
    midlt = t.pop(len(t)-1)
    return t
print(chop([0,1,2,3,4,5]))