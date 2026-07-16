import random
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler #simulate measurements


#generate random bits and bases
alice_bits = [random.randint(0,1) for _ in range(8)] 
alice_bases = [random.randint(0,1) for _ in range(8)] 
bob_bases = [random.randint(0,1) for _ in range(8)] 


#encode alice's qubits
circuits = [] 
for bit, basis in zip(alice_bits, alice_bases):
    qc = QuantumCircuit(1,1)
    if bit == 1: qc.x(0) 
    if basis == 1:
        qc.h(0)
        
    circuits.append(qc) 
    
#measure bob's qubits
for qc, basis in zip(circuits, bob_bases):
    if basis == 1:
        qc.h(0)
    qc.measure(0,0)
    
#simulate the measurements  
sampler = StatevectorSampler()
job = sampler.run(circuits, shots=1)
result = job.result()

#printing results
print("Alice Bits :", alice_bits)
print("Alice Bases:", alice_bases) 
print("Bob Bases  :", bob_bases) 
print("Simulation Complete") 