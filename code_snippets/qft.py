#!/usr/bin/python3

from matplotlib import pyplot as plt
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit import Aer
from qiskit.tools.visualization import plot_histogram

beforeFT = QuantumCircuit(5)
# Initialize state in uniform superposition
beforeFT.h([0,1,2,3,4])

# Measure all qubits
beforeFT.measure_all()

# Simulate the circuit
mySimulator = Aer.get_backend('aer_simulator')
result = mySimulator.run(beforeFT,shots=2**20).result()

# Plot a bar chart of all the results
plot_histogram(result.get_counts(),bar_labels=False,title='Before QFT')

afterFT = QuantumCircuit(5)
# Initialize qubits
afterFT.h([0,1,2,3,4])

# Add Fourier transform operation
qft = QFT(num_qubits=5,do_swaps=False).to_gate()
afterFT.append(qft, qargs=[0,1,2,3,4])

# Measure all qubits
afterFT.measure_all()

# Decompose Fourier transform operation into gates for simulator
afterFT = afterFT.decompose(reps=2)

# Simulate the circuit
result = mySimulator.run(afterFT,shots=2**20).result()

# Plot a bar chart of all the results
plot_histogram(result.get_counts(),bar_labels=False,title='After QFT')

plt.show()