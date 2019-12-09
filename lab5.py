#udl computational tools for problem solving lab5
#humakal
#'19
import math

def repInBinary(e): 
    eBin = []
    while(e != 0 ):
        eBin.append(e%2)
        e = int(e/2)
    eBin.reverse()
    return eBin

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return x, y

def rabin_encrypt(m, n):
    return (m*m) % n   

def rabin_decrypt(c, p, q):
    n = p * q
    mp = c**((p+1)/4) % p   
    mq = c**((q+1)/4) % q   
    yp, yq = egcd(p, q)

    m1 = ( yp*p*mq + yq*q*mp ) % n
    m2 = n - m1
    m3 = ( yp*p*mq - yq*q*mp ) % n
    m4 = n - m3
    return m1, m2, m3, m4

def rabins_cryptosystem(m, p, q):
    n = p * q
    c = rabin_encrypt(m, n)
    print("encrypted....")
    print("c: ",c)
    m1, m2, m3, m4 = rabin_decrypt(c, p, q)
    print("decrypted....")
    print("m1: ",m1)
    print("m2: ",m2)
    print("m3: ",m3)
    print("m4: ",m4)

def main():
    m=3
    p=7
    q=11
    print("m:",m,"p:",p,"q:",q)
    rabins_cryptosystem(m, p, q)

    
if __name__== "__main__":
  main()


