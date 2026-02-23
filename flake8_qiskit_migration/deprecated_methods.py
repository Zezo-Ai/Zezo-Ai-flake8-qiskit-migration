### This file contains deprecated/removed method names for Qiskit 1.0 and 2.0.
### Dictionaries are in the form:
###     "method_name": "{} advice to user"
### where `{}` will be replaced with `.method_name()`.
###
### These are only flagged when the file imports from `qiskit`.
### Without type inference we can't know the receiver type, so we
### restrict to method names specific enough to avoid false positives.

DEPRECATED_METHODS_V1 = {
    # QuantumCircuit / Instruction / Register .qasm() removed
    "qasm": "QuantumCircuit{} has been removed in Qiskit 1.0; use `qiskit.qasm2.dumps(circuit)` instead",
    # QuantumCircuit.bind_parameters → .assign_parameters()
    "bind_parameters": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.assign_parameters()` instead",
    # Removed QC gate aliases
    "cnot": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.cx()` instead",
    "toffoli": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.ccx()` instead",
    "fredkin": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.cswap()` instead",
    "mct": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.mcx()` instead",
    # Removed QC methods (from qiskit.extensions removal)
    "snapshot": "QuantumCircuit{} has been removed in Qiskit 1.0; use Aer save instructions instead",
    "squ": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(UnitaryGate(...))` instead",
    "diagonal": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(DiagonalGate(...))` instead",
    "hamiltonian": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(HamiltonianGate(...))` instead",
    "isometry": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(Isometry(...))` instead",
    "iso": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(Isometry(...))` instead",
    "uc": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(UCGate(...))` instead",
    "ucrx": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(UCRXGate(...))` instead",
    "ucry": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(UCRYGate(...))` instead",
    "ucrz": "QuantumCircuit{} has been removed in Qiskit 1.0; use `.append(UCRZGate(...))` instead",
}

DEPRECATED_METHODS_V2 = {
    # Instruction / InstructionSet .c_if() → if_test context manager
    "c_if": "Instruction{} has been removed in Qiskit 2.0; use the `if_test` context manager instead",
    # Instruction.condition_bits() removed with c_if
    "condition_bits": "Instruction{} has been removed in Qiskit 2.0; use `IfElseOp` instead",
    # QuantumCircuit / DAGCircuit calibration methods (Pulse removal)
    "add_calibration": "QuantumCircuit{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "has_calibration_for": "QuantumCircuit{} has been removed in Qiskit 2.0 as part of Pulse removal",
    # BackendV2 channel methods (Pulse removal)
    "instruction_schedule_map": "BackendV2{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "drive_channel": "BackendV2{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "measure_channel": "BackendV2{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "acquire_channel": "BackendV2{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "control_channel": "BackendV2{} has been removed in Qiskit 2.0 as part of Pulse removal",
    # Target methods (Pulse removal)
    "has_calibration": "Target{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "get_calibration": "Target{} has been removed in Qiskit 2.0 as part of Pulse removal",
    "update_from_instruction_schedule_map": "Target{} has been removed in Qiskit 2.0 as part of Pulse removal",
    # Target.target_to_backend_properties()
    "target_to_backend_properties": "Target{} has been removed in Qiskit 2.0",
}
