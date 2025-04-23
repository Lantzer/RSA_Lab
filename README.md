# CSCD434 Network Security – RSA Encryption Lab

I implemented an RSA encryption algorithm, demonstrating how increasing the size of the prime factors used to compute `n` (where `n = p * q`) exponentially increases the difficulty of factoring `n`, and thereby enhances the security of the encryption.

To implement RSA encryption, I followed these steps:
- Generated two large prime numbers, `p` and `q`
- Calculated `n = p * q`
- Computed the least common multiple (LCM) of `(p - 1)` and `(q - 1)`, denoted as `λ`
- Selected `e = 65537`, a commonly used public exponent
- Calculated `d`, the modular multiplicative inverse of `e` modulo `λ`

The values of `n` and `e` together form the **public key**.

The value of `d` is kept secret as part of the **private key**.

To decrypt a message encrypted with the public key, I used the formula:

`M = C^(d) % n`

Where:
- `M` is the plaintext message
- `C` is the ciphertext

---

In this lab we found that with smaller values for `p` and `q`, the easier it was to find the value of `d`. The value of RSA encryption comes from the computational difficulty of factoring the product of two large prime numbers.
