def fun() :
    n=15
    a=3
    print("welcome to the game")
    while a != 0 :
         g = eval(input("guess the number"))
         if g<n:
             print("the number you entred in less")
             a = a-1
         elif g>n :
            print("the number you entred in greater")
            a = a-1
         else :
            print("YOU WON")
            a = 0
    print("Game is over")
    
