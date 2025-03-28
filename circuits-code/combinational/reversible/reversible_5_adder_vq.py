from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import numpy as np

qreg_q = QuantumRegister(11, 'q')
creg_c = ClassicalRegister(11, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.cx(qreg_q[3], qreg_q[2])
circuit.cx(qreg_q[5], qreg_q[4])
circuit.cx(qreg_q[7], qreg_q[6])
circuit.cx(qreg_q[9], qreg_q[8])
circuit.cx(qreg_q[9], qreg_q[10])
circuit.cx(qreg_q[7], qreg_q[9])
circuit.cx(qreg_q[5], qreg_q[7])
circuit.cx(qreg_q[3], qreg_q[5])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[3])
circuit.ccx(qreg_q[2], qreg_q[3], qreg_q[5])
circuit.ccx(qreg_q[4], qreg_q[5], qreg_q[7])
circuit.ccx(qreg_q[6], qreg_q[7], qreg_q[9])
circuit.ccx(qreg_q[8], qreg_q[9], qreg_q[10])
circuit.cx(qreg_q[9], qreg_q[8])
circuit.ccx(qreg_q[6], qreg_q[7], qreg_q[9])
circuit.cx(qreg_q[7], qreg_q[6])
circuit.ccx(qreg_q[4], qreg_q[5], qreg_q[7])
circuit.cx(qreg_q[5], qreg_q[4])
circuit.ccx(qreg_q[2], qreg_q[3], qreg_q[5])
circuit.cx(qreg_q[3], qreg_q[2])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[3])
circuit.cx(qreg_q[3], qreg_q[5])
circuit.cx(qreg_q[5], qreg_q[7])
circuit.cx(qreg_q[7], qreg_q[9])
circuit.cx(qreg_q[1], qreg_q[0])
circuit.cx(qreg_q[3], qreg_q[2])
circuit.cx(qreg_q[5], qreg_q[4])
circuit.cx(qreg_q[7], qreg_q[6])
circuit.cx(qreg_q[9], qreg_q[8])
circuit.measure(qreg_q[0], creg_c[0])
circuit.measure(qreg_q[1], creg_c[1])
circuit.measure(qreg_q[2], creg_c[2])
circuit.measure(qreg_q[3], creg_c[4])
circuit.measure(qreg_q[5], creg_c[5])
circuit.measure(qreg_q[6], creg_c[6])
circuit.measure(qreg_q[7], creg_c[7])
circuit.measure(qreg_q[8], creg_c[8])
circuit.measure(qreg_q[9], creg_c[9])
circuit.measure(qreg_q[10], creg_c[10])