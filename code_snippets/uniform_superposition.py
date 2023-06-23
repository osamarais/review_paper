#!/usr/bin/python3

import qiskit
from qiskit import Aer
from qiskit.tools.visualization import plot_histogram

# Create a register of 3 qubits
myQRegister = qiskit.QuantumRegister(3, '\psi')

# Create a register of 3 classical bits
myCRegister = qiskit.ClassicalRegister(3,'Classical Bits')

# Create a quantum circuit with using myRegister
myCircuit = qiskit.QuantumCircuit(myQRegister, myCRegister)

# Hadamard gates on al qubits
myCircuit.h(myQRegister)

# Measure all the qubits in myQRegister and store state in myCRegister
myCircuit.measure(myQRegister,myCRegister)


# Simulate the circuit
mySimulator = Aer.get_backend('aer_simulator')
result = mySimulator.run(myCircuit,shots=5120).result()

# Plot a bar chart of all the results
plot_histogram(result.get_counts(), title='Uniform Superposition')