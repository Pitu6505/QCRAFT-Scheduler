from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np

qreg_q = QuantumRegister(6, 'q')
creg_c = ClassicalRegister(6, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cx(qreg_q[0], qreg_q[3])
circuit.cx(qreg_q[1], qreg_q[3])
circuit.cx(qreg_q[1], qreg_q[4])
circuit.cx(qreg_q[2], qreg_q[4])
circuit.cx(qreg_q[0], qreg_q[5])
circuit.cx(qreg_q[2], qreg_q[5])
circuit.measure(qreg_q[3], creg_c[3])
circuit.measure(qreg_q[4], creg_c[4])
circuit.measure(qreg_q[5], creg_c[5])
circuit.x(qreg_q[0]).c_if(creg_c[3], 1)
circuit.x(qreg_q[1]).c_if(creg_c[4], 1)
circuit.x(qreg_q[2]).c_if(creg_c[5], 1)