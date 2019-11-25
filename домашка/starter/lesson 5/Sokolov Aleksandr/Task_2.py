def function(x):
   if x < 0:
       return x -10
   else:
       return x + 10
   print(x)


def main():
    for i in range(-5, 5):
        i /= 2
        y = function(i)
        print('function(', i, ') =', y, sep='')
main()

