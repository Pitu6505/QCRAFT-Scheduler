OPENQASM 2.0;
include "qelib1.inc";

qreg q[7];  
creg c[1];  

h q[0];

cx q[0], q[1];
cx q[1], q[2];
cx q[2], q[3];
cx q[3], q[4];
cx q[4], q[5];
cx q[5], q[6];

rz(pi/2) q[6];

h q[0];
measure q[0] -> c[0];