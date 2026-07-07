from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
def create_entanglement():
    qc = QuantumCircuit(2,2)   
    qc.h(0)      
    qc.cx(0,1)  
    qc.measure([0,1],[0,1])
    run_entanglement(qc)
    return qc

def run_entanglement(qc):
    simulator = AerSimulator() 
    result = simulator.run(qc, shots=1024).result()
    return result.get_counts() 

create_entanglement()