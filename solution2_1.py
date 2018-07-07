def keyb(s):
    sum =0
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            sum = sum
        else:
            sum = sum+ abs(ord(s[i]) - ord(s[i+1]))-1
    return(sum)

print(keyb("supercalifragilisticexpialidocious")*keyb("antidisestablishmentarianism"))
