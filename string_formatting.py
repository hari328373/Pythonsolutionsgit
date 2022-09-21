def print_formatted(number):
    w=bin(number)
    w1=len(w[2:])
    for i in range(1,number+1):
        o=oct(i)
        b=bin(i)
        print(str(i).rjust(w1," "),o[2:].rjust(w1," "),format(i,'X').rjust(w1," "),format(i,'b').rjust(w1," "))
    print()