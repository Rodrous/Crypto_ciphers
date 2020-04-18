import random,math,sympy,os
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def e_val(euler_n):
    return random.randint(0,euler_n)

def rsa(p,q):
    a = is_prime(p)
    b = is_prime(q)

    if a is True and b is True:
        n = p * q

        euler_n = (p-1) * (q-1)
        e = e_val(euler_n)

        #inverse of e in euler_n

        z = True

        while z != False:
            gc = math.gcd(e, euler_n)
            if gc == 1 and (e % n)!= 0:
                z = False


            else:
                print(f"Current value of e is {e}, it is either a factor or inverse is not possible")
                e = e_val(euler_n)
                print(f"Changing this value to {e}")

        inverse = sympy.mod_inverse(e,euler_n)

        return e,inverse,n

    else:
        raise ValueError("a or b are not prime, change them")


def encrypt(plain):

    try:
        x, n = rsa(p, q)[0], rsa(p, q)[2]
        return plain ** x % n


    except Exception as ex:
        print(ex)


def decrypt(cypher):
   try:
       x, n = rsa(p, q)[1], rsa(p, q)[2]

       return cypher ** x % n
   except Exception as ex:
       print(ex)

def main():
    global p,q
    p = int(input("Enter one number:- "))
    q = int(input("Enter second number:- "))

    print("-".ljust(104, "-"))
    print('\n')
    choice = int(input("Encrypt (0), Decrypt(1) :- \n"))
    if choice == 0:
        plain = int(input("Enter Plain int:- "))
        print(f"Encrypted text is {plain}")



    elif choice == 1:
        cipher = int(input("Enter cipher:- "))
        print(f"Decrypted cipher is {decrypt(cipher)}")

    else:
        raise ValueError("404 brain not found")


main()
