#!/usr/bin/python3

from matplotlib import pyplot as plt
import qiskit
from qiskit import Aer
from qiskit.tools.visualization import plot_histogram

# Create a register of 2 qubits
myQRegister = qiskit.QuantumRegister(2, '\psi')

# Create a register of 2 classical bits
myCRegister = qiskit.ClassicalRegister(2,'Classical Bits')

# Create a quantum circuit with using myRegister
myCircuit = qiskit.QuantumCircuit(myQRegister, myCRegister)

# Hadamard gates on first qubit
myCircuit.h(0)
# CNOT gate controlled by first qubit on second qubit
myCircuit.cnot(0,1)

# Measure all the qubits in myQRegister and store state in myCRegister
myCircuit.measure(myQRegister,myCRegister)


# Simulate the circuit
mySimulator = Aer.get_backend('aer_simulator')
result = mySimulator.run(myCircuit,shots=5120).result()

# Plot a bar chart of all the results
plot_histogram(result.get_counts(), title='Bell State')

plt.show()