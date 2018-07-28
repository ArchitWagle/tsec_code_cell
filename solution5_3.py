def game(n):
    if(n%3==0):
        return 2
    else:
        return 1
    
print(game(22)+game(45)+game(26)+game(75))
