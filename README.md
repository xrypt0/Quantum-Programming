# 🪙 Schrödinger's Coin: Quantum Heads or Tails

A repository aimed at exploring quantum states, their applications, and computational complexity through fundamental implementations using Qiskit.

This project implements a **Quantum Random Number Generator (QRNG)** specifically designed as a **True Random Coin Flip Game**. Unlike classical pseudo-randomness, this uses the fundamental laws of quantum mechanics (superposition and measurement collapse) to achieve absolute, hilesiz (unbiased) randomness.

---

## 🚀 How It Works (The Quantum Physics)

A classical coin flip is deterministic (if you knew the exact force, wind, and angle, you could predict the outcome). A quantum coin flip is **inherently probabilistic**.

1. **Initialization**: We prepare a single qubit in the $|0\rangle$ state.
2. **Superposition (Hadamard Gate)**: We apply the Hadamard gate ($H$) to put the qubit in an equal superposition of $|0\rangle$ and $|1\rangle$:
   $$|0\rangle \xrightarrow{H} |+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$$
   At this stage, the coin is spinning in the air—it is **both heads and tails at the same time**.
3. **Measurement**: When we measure the qubit, the wave function collapses to a classical state:
   * **50% probability** of collapsing to $|0\rangle$ $\rightarrow$ **Heads** 🪙
   * **50% probability** of collapsing to $|1\rangle$ $\rightarrow$ **Tails** 👤

---

## 🛠️ Features

* **True Quantum Randomness**: Leverages Qiskit and Aer quantum simulator.
* **Interactive CLI**: Prompts the user for the number of flips.
* **Quantum Circuit Visualizer**: Prints the ASCII circuit diagram directly to the terminal.
* **Cross-Platform UTF-8 Support**: Out-of-the-box support for Windows Terminal encoding.

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

## 🖥️ Demo Terminal Output

```text
Enter how many times you want to flip the coin: 5

Flipping the quantum coin 5 times:
Flip #1: heads
Flip #2: tails
Flip #3: heads
Flip #4: heads
Flip #5: tails

Quantum Circuit Diagram:
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0
```

---

## 📂 Project Structure

* **`heads_or_tail_in_qiskit.py`**: The main quantum coin flip implementation script.
* **`README.md`**: Explanatory documentation of the project.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
