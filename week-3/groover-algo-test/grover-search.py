from qiskit import QuantumCircuit 
from qiskit.primitives import StatevectorSampler 
from qiskit.circuit.library import GroverOperator 

oracle = QuantumCircuit(2)
oracle.cz(0, 1)  #flip phase only when both qubits are |11>
oracle.name = "Oracle"

#grover operator
grover = GroverOperator(oracle)

qc = QuantumCircuit(2, 2)
qc.h([0, 1])  #initialize in superposition

qc.append(grover, [0, 1])  #apply grover iteration

qc.measure([0, 1], [0, 1])  #measure the qubits 

sampler = StatevectorSampler() 
job = sampler.run([qc], shots=1024) 
result = job.result() 

result = job.result()

counts = result[0].data.c.get_counts()
print(counts) 