from qiskit import QuantumCircuit 
from qiskit_aer import AerSimulator 
def create_teleportation():   
    qc = QuantumCircuit(3,3)    
    qc.h(0)     
    qc.h(1)    
    qc.cx(1,2)   
    qc.cx(0,1)    
    qc.h(0)  
    qc.measure([0,1,2],[0,1,2])
    return qc

def run_teleportation(qc): 
    simulator = AerSimulator() 
    result = simulator.run(qc, shots=1024).result()
    return result.get_counts() 