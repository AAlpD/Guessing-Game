import random
while True:
    ul = input("\n\nInterval: 1 - ")
    if ul == "":
        break
    ts = random.randint(1, int(ul))
    while True:
        t = int(input("\nGuess >> "))
        if t == ts:
            print("\nCongratulations you know!")
            break
        elif t < ts:
            print("\nBigger than your guess!")
        elif t > ts:
            print("\nSmaller than your guess!")
