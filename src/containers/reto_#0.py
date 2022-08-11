multDeTres = "fizz"
multDeCinco = "buzz"
multDeTresyCinco = "fizzbuzz"

for i in range(1, 101):

    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print(multDeTresyCinco)
        elif i % 3 == 0:
            print(multDeTres)
        else:
            print(multDeCinco)
    else:
        print(i)        
    print("-------------------------")        