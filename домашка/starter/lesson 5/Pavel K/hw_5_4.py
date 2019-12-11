def am(a,b,c):
    return (a+b+c)/3

while True:
    a,b,c = map(int,input('a = _, b = _, c = _').split())
    print(am(a,b,c))