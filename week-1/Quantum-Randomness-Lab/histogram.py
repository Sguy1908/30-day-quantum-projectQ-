from qiskit import QuantumCircuit 
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram 
import matplotlib.pyplot as plt 

#creating the simulator
simulator = AerSimulator() 
qc = QuantumCircuit(1,1) 


#applying superposition and measuring 
qc.h(0)
qc.measure(0,0) 

job = simulator.run(qc, shots=1000)

#obtaining the results
result = job.result() 
counts = result.get_counts() 

#generating the histogram
plot_histogram(counts) 
plt.show() 