#simulate attack
import random #simulate eve random measurement decisions
original_key = [random.randint(0, 1) for _ in range(8)]

modified_key = []
for bit in original_key:
    if random.random() < 0.3: #simulate eve measuring in the wrong basis
        modified_key.append(1-bit)
    else:
        modified_key.append(bit)
        
#compare the keys
errors = 0
for i in range(len(original_key)):
    if original_key[i] != modified_key[i]:
        errors += 1
        
#detect attack
if errors > 0:
    print(f"Attack detected! {errors} errors found in the key.")
else:
    print("No attack detected. The key is secure.")