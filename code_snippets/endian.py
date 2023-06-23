#!/usr/bin/python3

import qiskit

# Create a register of 3 qubits
myQRegister = qiskit.QuantumRegister(3, '\psi')

# Create a register of 3 classical bits
myCRegister = qiskit.ClassicalRegister(3,'Classical Bits')

# Create a quantum circuit with using myRegister
myCircuit = qiskit.QuantumCircuit(myQRegister, myCRegister)

# Start working in big-endian order

# Add the gates in order of operation
myCircuit.h(0)
myCircuit.x(2)
myCircuit.cnot(0,1,ctrl_state='1')

# Insert a barrier to keep circuit organized
myCircuit.barrier()

# Measure all the qubits in myQRegister and store state in myCRegister
myCircuit.measure(myQRegister,myCRegister)

# Convert from big-endian to little-endian by reversing bits
myCircuit = myCircuit.reverse_bits()

# Draw the circuit
myCircuit.draw('latex')
