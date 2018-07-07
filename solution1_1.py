S = "Just finished the TSEC CodeCell Challenge".replace(" ","").lower()
C = "CodeCell".lower()

def decode(S,C):
    C = C*(len(S)//len(C)+1)
    Decode = []
    print(C)
    print(S)
    for i in range(len(S)):
        Decode.append(chr(ord('a')+(ord(S[i])+ord(C[i])-ord('a'))%26))
    print("".join(Decode))
decode(S,C)
