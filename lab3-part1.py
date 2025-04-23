#!/usr/bin/python3
from prime import *
import math

#prime.gen_prime(bits)

def main():

    public,private = make_key(int(sys.argv[1]))

    #public key = (n,e)
    print(f"public key is ({public[0]},{public[1]})")

    #private key = (n,d)
    print(f"private key is ({private[0]},{private[1]})")

    #message to encrypt
    msg = b'test,message'
    print ("\nmessage: ", msg)
    print("message as int: ", int.from_bytes(msg))



    #cipher with public key
    x = cipher(msg,public[1],public[0])
    print("\nencrypt w/ public: ",x)
    
    #cipher with private key
    x2 = cipher(msg,private[1],private[0])
    print("encrypt w/ private: ",x2)

    #decipher with private key
    y = dcipher(x, private[1], private[0])
    print("\ndecipher w/ private: ", y.to_bytes(len(msg))) #turning int back to string


def cipher(m,e,n):
    i = int.from_bytes(m)   #"casting" to int
    return pow(i,e,n)

def dcipher(c,d,n):
    #FINISH THIS FUNCTION
    return (pow(c,d,n))
"""
FINISH THIS FUNCTION
You'll need a function from prime.py
"""
def make_key(bit_len):
    # compute n and d
    p, q = gen_prime(bit_len), gen_prime(bit_len)
    print("p in make_key: ", p)
    n = p * q
    print(n)
    e = 65537
    # (n,e) is your public key
    lamda = math.lcm(p-1, q-1)
    d = modinv(e, lamda)
    # (n,d) is your private key
    # use 65537 as e


    return((n,e),(n,d))

#found this code somewhere
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

"""
function to find modular multiplicative inverse in RSA
must give e and totient
stole this code too :)
"""
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

if __name__ == "__main__":
    main()
