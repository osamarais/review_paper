#!/usr/bin/python3

from matplotlib import pyplot as plt
import qiskit

# Create a register of 3 qubits, with a label myQubits
myRegister = qiskit.QuantumRegister(3, 'myQubits')