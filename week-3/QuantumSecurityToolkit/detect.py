alice_key = [1,0,1,1,0,1,0,0]
bob_key = [1,0,0,1,0,1,1,1]

errors = 0
for i in range(len(alice_key)):
    if alice_key[i] != bob_key[i]:
        errors += 1
        
#calculate error rate
error_rate = (errors / len(alice_key))*100

print("error rate:", error_rate, "%")

if( error_rate > 10):
    print("eve detected.")
    
else:
    print("no eve detected.")