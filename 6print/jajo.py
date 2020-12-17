def thor(a):
    for i in range(a):
        print(i)
        if i%5==0 and i%7==0:
            yield i
            print(i)

if __name__ == '__main__':
    thor(100)

