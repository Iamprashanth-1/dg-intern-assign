def comp(s):
    p=s.index('@')
    q=s.index('.')
    return s[p+1:q]

if __name__ == '__main__':
    print(comp('username@companyname.com'))
