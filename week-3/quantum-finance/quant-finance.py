from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(4, 4)
qc.h(range(4))

#paramterised rotations (to adjust the prob of selecting each investment)
qc.ry(0.8,0)
qc.ry(1.2,1) 
qc.ry(0.5,2) 
qc.ry(1.0,3) 

qc.measure(range(4), range(4))


sampler = StatevectorSampler() 
job = sampler.run([qc],shots=1024)  
result = job.result()  
counts = result[0].data.c.get_counts() 
print(counts)