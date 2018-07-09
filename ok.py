def fin():
    g = (input("enter the grade"))
    n = 0
    S = 0
    L = []
    while g != "" :
        g = eval(g)
        L.append(g)
        g = input("enter another grade (hit enter to exit)")

    for i in range(len[L]) :
        S = S+len[L]
    if len[L] != 0 :
        t = S/len[L]
        print("the average id:", S)
    else :
         print("you didn't enter a valisd number")
                
    
