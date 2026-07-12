from qiskit.circuit.library import ZZFeatureMap 
from qiskit.circuit.library import RealAmplitudes 
from qiskit_machine_learning.algorithms import VQC
from qiskit_algorithms.optimizers import COBYLA 
from qiskit.primitives import StatevectorSampler 

feature_map = ZZFeatureMap(feature_dimension=2)  #converts classicla features to quantum information

ansatz = RealAmplitudes(2, reps=2) 

optimizer = COBYLA(maxiter=100) 


#quantum classifier
sampler = StatevectorSampler()
vqc = VQC(     sampler=sampler,     feature_map=feature_map,     ansatz=ansatz,     optimizer=optimizer ) 

vqc.fit(training_features, training_labels)

predictions = vqc.predict(test_features) 
print(predictions) 