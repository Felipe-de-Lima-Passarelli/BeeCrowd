X = int(input())
Y = int(input())

if X > Y:
    for i in range(Y+1, X):
        if i%5 == 2 or i%5 == 3:
            print(i)
else:
    for i in range(X+1 , Y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
