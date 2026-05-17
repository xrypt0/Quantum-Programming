# Quantum-Programming 💻
A repository aimed at exploring quantum states, their applications, and computational complexity through fundamental implementations using Qiskit.
---

## 🚀 How It Works (Quantum Physics - Simplified)

Unlike classical computers that use **Bits** (which can only be `0` or `1`), quantum computers leverage the bizarre properties of quantum mechanics to process information using **Qubits** (Quantum Bits). 

Here are the three fundamental pillars of quantum computing explained simply:

### 1. Superposition
A classical bit is like a light switch—it is either **OFF (0)** or **ON (1)**. A qubit is like a spinning coin—while it is spinning in the air, it is in a **superposition** of being both heads (0) and tails (1) at the exact same time.

In mathematics, applying a **Hadamard Gate ($H$)** transforms a definite state $|0\rangle$ into a superposition state:
$$|0\rangle \xrightarrow{H} |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$
This means the qubit now holds both possibilities simultaneously with equal probability amplitude.

### 2. Measurement & Collapse
You cannot observe a superposition directly. The moment you measure a qubit, the superposition **collapses** instantly into a definite classical state of either `0` or `1`. This is similar to stopping the spinning coin with your hand—it immediately collapses to either heads or tails.

### 3. Entanglement
Qubits can be linked together in a way that the state of one instantly dictates the state of another, no matter how far apart they are. Einstein famously called this *"spooky action at a distance"*. Applying a **CNOT gate** is a common way to entangle two qubits, forcing them to always collapse into correlated states (e.g., both `00` or both `11`).

---

## 🛠️ Features

* **True Quantum Randomness**: Leverages Qiskit and Aer quantum simulator.
* **Interactive CLI**: Prompts the user for the number of flips.
* **Quantum Circuit Visualizer**: Prints the ASCII circuit diagram directly to the terminal.
---

## 📊 Circuit Diagram

```text
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0
```
* **`q`**: Qubit line where the Hadamard gate ($H$) and Measurement ($M$) occur.
* **`c`**: Classical register where the measurement result drops down ($0$ for Heads, $1$ for Tails).

---

## 💻 Quick Start

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Install Dependencies
Install the required quantum computing libraries:
```bash
pip install qiskit qiskit-aer
```

### 3. Run the Game
Execute the script in your terminal:
```bash
python heads_or_tail_in_qiskit.py
```

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
