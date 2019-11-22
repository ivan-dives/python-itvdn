n = 6
for row in range(n):
   for column in range(n):
       print('*' if column+row >= n-1 else '', end = '')
   print()