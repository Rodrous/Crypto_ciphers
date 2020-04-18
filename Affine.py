import string
def encrypt(initial, a, b):

    initial = initial.lower()
    mylist = []
    for character in initial:
        mylist.append(ord(character) - 97)
    output = ""
    key = ""

    alphabet = dict(zip(range(0, 26), string.ascii_lowercase))
    for i in range(len(mylist)):
        image = str(alphabet[int(mylist[i] * a + b) % 26])
        output += image

        div = str(int(mylist[i] * a + b) // 26)
        if i == 0:
            divtem = div
        else:
            divtem = "-" + div

        key += divtem

    return output, key



def main():
    plain = input("Plaintext :- ")
    a = input("key1:- ")
    b = input("key2:- ")

    print(encrypt(plain, a, b)[0])
    print(encrypt(plain,a,b)[1])

main()