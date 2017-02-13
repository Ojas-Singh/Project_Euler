#Simple Prime testing program!

def is_prime(n):
    a=True
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            a=False
    return a
