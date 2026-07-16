import random #generate random bits and bases

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.randint(0, 1) for _ in range(n)]

#selecting random bases(bob)
bob_bases = generate_bases(8)

#generate alice data
n = 8
alice_bits = generate_bits(n)
alice_bases = generate_bases(n)
bob_bases = generate_bases(n)

#compare bases & print shared key
shared_key=[]
for i in range(n):
    if alice_bases[i] == bob_bases[i]:
        shared_key.append(alice_bits[i])
print("shared secret key")
print (shared_key)
