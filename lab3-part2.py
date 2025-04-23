#!/usr/bin/python3
from prime import *
import math

# find d
# n = p * q
# d = modular mult. inverse of e mod lcm(p-1, q-1)
#   C = 768916070269816102747332979141020881585
#   public key = (2056441770226766373907588738676247006587,65537)
#   private key = (2056441770226766373907588738676247006587, d)
# p = 40822754178477882469
# q = 50374890465154864223

def main():
    c = 768916070269816102747332979141020881585
    n = 2056441770226766373907588738676247006587
        
        #factors from wolframalpha
    p = 40822754178477882469    
    q = 50374890465154864223
    lamda = math.lcm(p-1,q-1)
    e = 65537
    d = modinv(e, lamda)

    # returns the deciphered message as an int
    m = pow(c,d,n)  
    print("M as a int:",m)

    # convert the (int)M into bytes
    m_bytes = m.to_bytes(50)   #guess of 50 bytes needed
    print("\nM as bytes: ", m_bytes)

# Copied from practiceRSA.py
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

"""
Copied from praticeRSA.py
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

