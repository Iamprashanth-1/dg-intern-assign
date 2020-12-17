def rid(a,b,c,n):
    p=[[[n for i in range(a)]for j in range(b) ] for k in range(c)]
    return p
if __name__ == "__main__":
    f=rid(3,5,8,0)
    print(f)
