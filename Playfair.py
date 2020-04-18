key  = [[ord("L"),ord("G"),ord("D"),ord("B"),ord("A")],
        [ord("Q"),ord("M"),ord("H"),ord("E"),ord("C")],
        [ord("U"),ord("R"),ord("N"),ord("I"),ord("F")],
        [ord("X"),ord("V"),ord("S"),ord("O"),ord("K")],
        [ord("Z"),ord("Y"),ord("W"),ord("T"),ord("P")]]


plaintext = input("Enter Plaintext:- ").replace(" ","").upper()

plaintext = (plaintext.replace("J","I"))

length = len(plaintext)
for i in range (0,length-1):
    if plaintext[i] == plaintext[i+1]:
        plaintext = plaintext[:i+1] + "X" +plaintext[i+1:]
if len(plaintext)%2 == 1:
    plaintext = plaintext+"X"
arr = [0 for q in range (0,len(plaintext))]
for c in range (0,len(plaintext)):
    for j in range (0,len(key)):
           for k in range(0, len(key)):
               if ord(plaintext[c]) == key[j][k]:
                   arr[c] = j,k
arr2 = [0 for q1 in range(0,len(plaintext))]
#Rules
for t in range(0,len(plaintext),2):
    a1 = arr[t]
    a2 = arr[t+1]
    if a1[0] == a2[0]:
        if a1[1] == 4:
            a1 = a1[0],0
            arr2[t] = a1
        else:
            a1 = a1[0], a1[1] + 1
            arr2[t]= a1

        if a2[1] == 4:
            a2 = a2[0],0
            arr2[t+1] = a2
        else:
            a2 = a2[0],a2[1]+1
            arr2[t+1] = a2

    elif a1[1] == a2[1]:
        if a1[0] == 4:
            a1 = 4,a1[1]
            arr2[t] = a1
        else:
            a1 = a1[0] + 1, a1[1]
            arr2[t] = a1

        if a2[0]==4:
            a2= 0,a2[1]
            arr2[t+1] = a2
        else:
            a2 = a2[0]+1,a2[1]
            arr2[t+1] = a2
    else:
        c5 = a1
        a1 = a1[0],a2[1]
        a2 = a2[0],c5[1]
        arr2[t] = a1
        arr2[t+1] = a2
enc = ""

for qt in range (0, len(arr2)):
    q1 = arr2[qt]
    enc = enc+(chr(key[q1[0]][q1[1]]))

print(enc.lower())
