from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def coin_flip(num_bits=1):
    """
    Simulates a quantum coin flip using a Hadamard gate.
    Returns the string outcome ('heads' or 'tails') and the QuantumCircuit object.
    """
    qc = QuantumCircuit(num_bits, num_bits)
    
    # Apply Hadamard gate to put the qubit in superposition
    for i in range(num_bits):
        qc.h(i)
        
    # Measure the qubit
    qc.measure(range(num_bits), range(num_bits))
    
    # Run the simulation on the Aer simulator for 1 shot
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts(compiled_circuit)
    
    # Get the raw binary string outcome
    binary_string = list(counts.keys())[0]
    
    # Convert binary to decimal integer
    decimal_number = int(binary_string, 2)
    
    # Map 0 to 'heads' and 1 to 'tails'
    if decimal_number == 0:
        return "heads", qc
    else:
        return "tails", qc

# Get user input for the number of coin flips
try:
    num_flips = int(input("Enter how many times you want to flip the coin: "))
except ValueError:
    print("Invalid input. Defaulting to 1 flip.")
    num_flips = 1

print(f"\nFlipping the quantum coin {num_flips} times:")

# Loop to execute the coin flip the specified number of times
latest_circuit = None
for i in range(num_flips):
    outcome, latest_circuit = coin_flip(1)
    print(f"Flip #{i+1}: {outcome}")

# Draw the quantum circuit diagram at the end
if latest_circuit is not None:
    print("\nQuantum Circuit Diagram:")
    print(latest_circuit)
