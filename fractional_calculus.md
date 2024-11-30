# Introduction to Fractional Calculus

## What is Fractional Calculus?
Fractional calculus is a branch of mathematics that extends the concept of derivatives and integrals to non-integer (fractional) orders. Unlike traditional calculus, fractional derivatives account for long-term dependencies and memory effects, making them suitable for modelling complex systems.

### Fractional Derivatives
A fractional derivative of order \(\alpha\) can be expressed as:

\[D^\alpha f(t) = \frac{1}{\Gamma(1 - \alpha)} \int_0^t \frac{f'(\tau)}{(t - \tau)^\alpha} d\tau\]

Where:
- \(\Gamma(x)\) is the gamma function.
- \(\alpha\) determines the order of the derivative.

### Why Use Fractional Dynamics?
Traditional models assume that systems only depend on their current state. Fractional dynamics allow for **memory effects**, where past states influence current behaviour. This is crucial for:
- Modeling **anomalous diffusion** in physical and biological systems.
- Simulating **rare events** and **critical transitions**.

---

## Applications
1. **Astrophysics**: Modeling black holes and galaxy formation.
2. **Biophysics**: Investigating molecular diffusion in crowded environments.
3. **Finance**: Simulating long-term market trends and crashes.

Learn more about the results and findings in [Results and Findings](results.md).
