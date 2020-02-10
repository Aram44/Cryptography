import random
def rande(f):
 k = 0
 for i in range(2, f+1):
  for j in range(2, i):
   if i % j == 0:
    k = k + 1
  if k == 0 and f%i!=0:
    return i
  else:
   k = 0
def intd(e, fi):
	i = (fi+1)/e
	d = 1
	while not i.is_integer():
	    d += 1
	    i = ((fi+1)/e)*d
	return d
def gcd (a, b):
 if b == 0:
  return a
 else:
  return gcd (b, a % b);
p = 3
q = 7
n = p * q
fi=(p-1)*(q-1)
e = rande(fi)
d = intd(e,fi)
s = 19
enc = (s ** e) % n
dec = (enc ** d) % n
print(enc, dec)
n = input()
