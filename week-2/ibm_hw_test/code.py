from qiskit import QuantumCircuit #build quantum program
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 #connects program  to IBM Quantum services
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# QiskitRuntimeService.save_account(
#     channel="ibm_quantum_platform",
#     plans_preference=["open"],
#     token="...",
#     overwrite=True,
#     instance=".."
# )
service = QiskitRuntimeService() #creates connection to ibm quantum acc to allow access to simulators and stuff

# List all backends you actually have access to
available_backends = service.backends()
print("Your available backends are:", [b.name for b in available_backends])

# Force-select one of your available real hardware backends
try:
    backend = service.backend("ibm_marrakesh")
    print(f"Successfully locked onto real quantum hardware: {backend.name}")
except Exception as e:
    # Fallback to another one just in case ibm_kingston is under maintenance
    backend = service.backend("ibm_fez")
    print(f"Locked onto alternative real quantum hardware: {backend.name}")

sampler = SamplerV2(mode=backend)

# backend = service.least_busy(
#     operational=True,
#     simulator=False
# ) #selects least busy hardware

sampler = SamplerV2(mode=backend)

#create circuit ->
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()

# 3. Transpile the circuit for the physical hardware (Crucial Step!)
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(qc)

# 4. Initialize SamplerV2 and run the ISA circuit
sampler = SamplerV2(mode=backend)
job = sampler.run([isa_circuit]) 

print(f"Job submitted successfully! Job ID: {job.job_id()}")

# 5. Fetch the results (Note: This will pause execution until the hardware queue clears)
print("Waiting...")
result = job.result()
print("finished, results:")
print(result)