
Here are **detailed notes** for **Chapter 1: “But what is a Neural Network?”** from the 3Blue1Brown deep learning series:

---

**Overview**

• The video introduces neural networks using the example of recognizing handwritten digits.

• Explains how neural networks are inspired by the human brain but operate using simple mathematical principles.

• Focuses on the **structure** of a neural network rather than training.

---

**1. Human Brain vs Computer**

• Recognizing a digit like “3” is easy for humans, even if it’s messy or pixelated.

• Writing a program to recognize digits from 28x28 pixel grids is hard without machine learning.

---

**2. Goal**

• Build a neural network that recognizes handwritten digits (0–9) from 28x28 pixel images (i.e., 784 pixels total).

• Each digit will be classified into 1 of 10 output categories.

---

**3. Neural Network Structure**

• **Input Layer:**

• 784 neurons (one for each pixel).

• Each holds a grayscale value (0 = black, 1 = white).

• **Output Layer:**

• 10 neurons (digits 0–9).

• Each neuron’s activation indicates the likelihood that the input image is that digit.

• **Hidden Layers:**

• Two hidden layers, each with 16 neurons (arbitrary choice for illustration).

• The purpose is to transform input features into useful patterns.

---

**4. Activations**

• Each neuron holds a number between 0 and 1, known as its **activation**.

• Higher activation = neuron is “lit up” or “firing.”

---

**5. Inspiration from the Brain**

• Neurons in biological brains fire to activate other neurons.

• Similarly, layers in a neural network pass activations forward.

---

**6. Understanding the Hidden Layers**

• The goal: intermediate layers recognize **sub-components** of digits (e.g., loops, lines).

• E.g., the digit “9” = loop on top + vertical line.

• Even subcomponents like loops are made from edges.

• Layer 2 might recognize edges.

• Layer 3 might recognize patterns like loops.

• Output layer combines these to classify digits.

---

**7. Weights and Biases**

• **Weights** define the strength of connection between neurons.

• Each neuron in a layer connects to **all** neurons in the previous layer.

• The input to each neuron = **weighted sum** of inputs + **bias**.

• Weights can be visualized as a grid: green (positive), red (negative).

---

**8. Activation Function**

• Weighted sums are passed through a **squashing function** (activation function) to normalize outputs.

• Common function: **Sigmoid** (squishes values to between 0 and 1).

• Other function mentioned: **ReLU (Rectified Linear Unit)** – modern alternative, easier to train.

• **Bias** shifts the input to the activation function to control when it activates.

---

**9. Mathematical Representation**

• All activations from a layer can be treated as a **vector**.

• All weights can be treated as a **matrix**.

• Transition from one layer to the next:

```
Output = sigmoid(Weights * Input + Bias)
```

  

• Matrix-vector multiplication is the core of forward propagation.

• Efficient implementations rely on linear algebra.

---

**10. Total Parameters**

• With 784 input neurons, 2 hidden layers (16 neurons each), and 10 output neurons:

• ≈ 13,000 **total weights and biases**.

• Each weight/bias is a “knob” that can be tuned during training.

---

**11. Interpretation**

• The entire neural network is essentially a **complicated function**:

• Takes in 784 numbers.

• Outputs 10 numbers representing prediction probabilities.

• Training = finding the right combination of weights and biases that minimize error.

---

**12. Visualizing and Debugging**

• Understanding what each neuron is doing helps in:

• Improving the model.

• Debugging unexpected behavior.

• “Opening the black box” provides insights into pattern recognition.

---

**13. Transition to Part 2**

• This video focused on **structure**.

• The next video will explore:

• **Training** the network.

• **How learning works**.

• Backpropagation and optimization.

---

**14. Expert Insight – Sigmoid vs ReLU**

• Guest: **Lisha Li** explains that:

• Sigmoid is inspired by biological neurons but has drawbacks (e.g., slow training).

• ReLU is now preferred due to better performance in deep networks.

---

Would you like similarly detailed notes for the next video in the series too?