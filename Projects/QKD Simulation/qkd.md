# 🛡️ Interactive BB84 QKD Simulator (Alice, Bob & Eve)

An interactive, educational dashboard designed to visualize the **BB84 Quantum Key Distribution (QKD)** protocol and experience quantum cryptography in action. 

This program simulates a secure key exchange between Alice and Bob, allowing you to intercept the channel as an eavesdropper (Eve) to see how quantum mechanics inherently protects information.

---

## 📂 File Structure

* **`qkd_simulation.py`**: Pure physics engine simulating qubits, measurement collapses, and Eve's intercept-resend attacks.
* **`qkd_visual.py`**: Main entry point that loads the interactive GUI dashboard using Matplotlib.

---

## 🚀 Quick Start

### 1. Install Dependencies
Ensure you have Python 3.8+ installed, then run:
```bash
pip install matplotlib numpy qiskit qiskit-aer
```

### 2. Run the Simulator
Launch the dashboard in your terminal:
```bash
python qkd_visual.py
```

---

## 🔬 How It Works (The Physics)

* **Superposition**: Alice encodes bits ($0$ or $1$) in Z bases ($|0\rangle, |1\rangle$) or X bases ($|+\rangle, |-\rangle$).
* **Measurement Collapse**: Qubits exist in superposition until measured, which immediately collapses them into classical states.
* **Eavesdrop Detection**: Eve cannot clone quantum states (No-Cloning Theorem). If Eve measures the qubit, she collapses it. Even if Alice and Bob's bases match later, Eve's interference introduces a **25% error rate (QBER)**, immediately exposing her presence and causing Alice and Bob to discard the key!
