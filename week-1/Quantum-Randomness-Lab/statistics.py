from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

#creating the simulator, applying hadamard and measuring
simulator = AerSimulator() 
qc = QuantumCircuit(1,1)
qc.h(0) 
qc.measure(0,0)


#running it 1000 times and obtaining the results
job = simulator.run(qc, shots=1000)
result = job.result() 

counts = result.get_counts() 

zeros = counts.get("0",0)
ones = counts.get("1",0) 

#printing outputs
print("Zeros:", zeros)
print("Ones:", ones) 
#calculating mean and standard deviation
print("Mean:", np.mean([zeros,ones]))
print("Standard Deviation:", np.std([zeros,ones])) 