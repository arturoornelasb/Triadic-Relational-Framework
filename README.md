# A Rigorous Triadic Framework for Neurosymbolic Reasoning

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) 

[[![DOI](https://zenodo.org/badge/17613664.svg)](https://doi.org/10.5281/zenodo.17613664)](https://zenodo.org/badge/DOI/10.5281/zenodo.17613664.svg)


TL;DR: A formal, integer-based (GCD) framework for neurosymbolic logic to replace floating-point vector addition.
This repository contains the official Python implementation and paper materials for "A Rigorous Triadic Framework for Neurosymbolic Reasoning".

## Abstract

[source: A Rigorous Triadic Framework for Neurosymbolic Reasoning.pdf] Current Large Language Models (LLMs) excel at statistical pattern matching but struggle with verifiable symbolic logic. This paper proposes a formal, integer-based relational framework as a candidate model for the underlying logic of emergent "sparse circuits". The framework is built on dual functions: a generative function ($\Phi_G$) for predicting new relations and a discovery function ($\Phi_D$) for inferring balancing rules from existing data. It uses integer balancing and normalization via the Greatest Common Divisor (GCD) to compute relational transformations, moving beyond floating-point vector addition to a ratio-based, symbolic logic. We first define the formal mathematics. We then validate its descriptive power by modeling the laws of classical mechanics. Finally, we discuss its implementation in Python using exact rational arithmetic (fractions) and graph libraries (networkx) for building hybrid neurosymbolic architectures. We provide a Python implementation to validate the framework's computational viability.

## DOI / Citation
)


This work is permanently archived and can be cited using the Zenodo DOI.
Title: A Rigorous Triadic Framework for Neurosymbolic Reasoning (v1.0.0)
Author: Ornelas Brand,. josé A.
Year: 2025
Published in: Zenodo
DOI: 10.5281/zenodo.17613664
Link: https://doi.org/10.5281/zenodo.17613664

## Key Concepts from the Paper
This framework introduces a formal, integer-based method for relational reasoning, diverging from traditional floating-point vector arithmetic.
Dual Functions: The core of the framework is built on two complementary functions:
Generative Function ($\Phi_G$): Predicts a new concept $C_4$ from three inputs $(C_1, C_2, C_3)$ and a known balancing rule $(a, b)$.
Discovery Function ($\Phi_D$): Operates in reverse. Given a known set of four concepts $(C_1, C_2, C_3, C_4)$, it infers the minimal, co-prime balancing rule $(a, b)$ that governs their relationship.
Integer-Based Logic: Instead of vector addition (e.g., $\vec{King} - \vec{Man} + \vec{Woman}$), this framework uses ratio-based balancing (e.g., $b \cdot C_1' \cdot C_4' = a \cdot C_2' \cdot C_3'$). All concepts are normalized to their integer base using the Greatest Common Divisor (GCD), ensuring computations are symbolic, exact, and verifiable.
Case Studies:
Classical Mechanics: The framework is shown to be capable of modeling deterministic, formula-based laws (like Kinetic Energy, $KE = \frac{1}{2}mv^2$) by discovering the integer balancing coefficients ($a=1, b=2$).
AI Interpretability: It is proposed as a formal language for "sparse circuits" and provides a symbolic, integer-based method for solving analogies (like King-Queen) using prime factor mapping.

## How to Use the Code

This repository provides the reference implementation. The scripts are designed to be used as a library or run directly to test the paper's examples.
1. Environment Setup
Clone the repository:
git clone [https://github.com/arturoornelasb/Triadic-Relational-Framework.git](https://github.com/arturoornelasb/Triadic-Relational-Framework.git)
cd Triadic-Relational-Framework


#Install the dependencies:
pip install -r requirements.txt


(Note: requirements.txt should contain networkx. The math and fractions libraries are part of the Python standard library).
2. Key Functions
[source: TriadicRelationalFramework.py] The file src/TriadicRelationalFramework.py contains the TriadicRelationalFramework class, which provides the main functions described in the paper:
compute_triad(C1, C2, C3, a, b): The generative function ($\Phi_G$).
check_static_balance(C1, C2, C3, C4): The discovery function ($\Phi_D$).
analogy_variant(C1, C2, C3): The variant for "A is to B as C is to D" analogies.
chain_triads(...): For chaining multiple triadic operations.
3. Running the Example
[source: TriadicRelationalFramework.py] The script src/TriadicRelationalFramework.py includes example usage and tests at the end of the file that validate the examples from the paper. You can run the script directly to see the output:
python src/TriadicRelationalFramework.py


## Example Usage (Test 1 from the paper, inside the script)

framework = TriadicRelationalFramework()
C4, K, steps = framework.compute_triad(18, 6, 8, 3, 4)
print("Abstract Example:")
print(f"C4: {C4}, K: {K}")
# Output: C4: 2, K: 1/12


##Repository Structure

```text

Triadic-Relational-Framework/
├── src/
│   └── TriadicRelationalFramework.py
├── paper/
│   ├── A Rigorous Triadic Framework for Neurosymbolic Reasoning.pdf
│   └── A Rigorous Triadic Framework for Neurosymbolic Reasoning.tex
├── README.md
├── requirements.txt
└── LICENSE

```

## License
This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc/4.0/

Copyright (c) 2025 José Arturo Ornelas Brand
