def dupli(l):
    p=list(set(l))
    return p

h=[12,24,35,24,88,120,155,88,120,155]
dup=dupli(h)
print('original is', h)
print('after removing duplicates',dup)
