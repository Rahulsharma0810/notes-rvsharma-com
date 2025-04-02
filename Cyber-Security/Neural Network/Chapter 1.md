# Chapter 1: But What is a Neural Network? — 3 Blue 1 Brown Deep Learning Series

## Overview
- Introduces neural networks using the classic problem of **digit recognition**.
- Demonstrates how **structure alone** (without training) can help in understanding what a neural network is.
- Goal: Classify handwritten digits (0–9) from 28 x 28 pixel images.

---

## 1. Human Brain vs Computer
- Humans recognize digits effortlessly even in low resolution.
- Computers struggle with this unless using **machine learning**.
- Challenge: Write a program that takes 784 grayscale values and returns a digit — hard to do manually.

---

## 2. Goal of the Video
- Build a neural network that learns to recognize handwritten digits.
- Use **simple structure** (no frills) to understand the **basic components** of neural networks.

---

## 3. Neural Network Structure
- **Input Layer**: 
  - 784 neurons (28×28 pixels).
  - Each holds a grayscale value from 0 (black) to 1 (white).
- **Output Layer**: 
  - 10 neurons (one for each digit 0–9).
  - Each neuron’s activation indicates the confidence level.
- **Hidden Layers**:
  - Two layers with 16 neurons each (arbitrary, for illustration).
  - Process features and subcomponents of digits.

---

## 4. Neuron Activation
- Each neuron holds a value between **0 and 1** (called **activation**).
- Neurons “light up” more as their activation increases.

---

## 5. Biological Analogy
- Neurons are inspired by those in the brain.
- In biology: groups of neurons trigger others to fire.
- In networks: activations in one layer trigger the next layer.

---

## 6. Interpreting Hidden Layers
- Hidden layers recognize **subcomponents**:
  - Example: "9" = loop on top + vertical line.
  - Lower layers detect **edges**, higher layers detect **shapes** or **patterns**.
- Helps generalize from pixels to concepts.

---

## 7. Weights and Biases
- **Weight**: Strength of connection between neurons.
- Each neuron in a layer has a **connection to every neuron** in the previous layer.
- **Bias**: Adjusts activation threshold.
- Total connections from input to hidden layer:
  - 784 (input neurons) × 16 (neurons in next layer) = **12,544 weights** + **16 biases**.

---

## 8. Activation Function
- After weighted sum, values are passed through a **squash function** to normalize.
- Common:
  - **Sigmoid**: Maps input to [0, 1].
  - **ReLU** (Rectified Linear Unit): Modern, easier to train.
- Bias shifts the curve to change sensitivity.

---

## 9. Matrix Representation
- Inputs → **Vector**
- Weights → **Matrix**
- Transformation:
  ```python
  output = sigmoid(W × input + b)
  ```

• Speeds up computation and code implementation.

• Matrix operations are at the core of forward propagation.

---

## **10. Parameter Count**

• Entire network ≈ **13,000 parameters**:
	• Weights + biases across layers.
• These are the **tunable knobs** of the model.

---

## **11. Network as a Function**

• A neural network is a **function**:
	• Input: 784 numbers (pixels).
	• Output: 10 numbers (digit probabilities).
• Internally:
	• Multiple matrix-vector products.
	• Non-linear activations (like sigmoid or ReLU).

---

## **12. Debugging the Network**

• Viewing neurons as components helps debug or improve networks.
• Encourages exploration beyond treating models as black boxes.

---

