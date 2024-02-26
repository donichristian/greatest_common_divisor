
  <div align="center">
  <h1 align="center">Greatest Common Divisor</h1>
  <h3>Codebase for the Greates Common Divisor platform</h3>
  <h3>◦ Developed with the software and tools below.</h3>
  <p align="center"><img src="https://img.shields.io/badge/-Python-004E89?logo=Python&style=flat-square" alt='Python\' />
  </p>
  </div>
  
  ---
  ## 📚 Table of Contents
  - [📚 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [🌟 Features](#-features)
  - [📁 Repository Structure](#-repository-structure)
  - [💻 Code Summary](#-code-summary)
  - [🚀 Getting Started](#-getting-started)
  
  ---
  
  
  ## 🔍 Overview

 The project contains a Python file named gcd.py and another file named unit_test.py

---

## 🌟 Features

 gcd.py, unit_test.py

---

## 📁 Repository Structure

```sh
├── gcd.py
└── unit_test.py

```

---

## 💻 Code Summary

<details><summary>Root</summary>

| File | Summary |
| ---- | ------- |
| gcd.py |  The code defines a function called `gcd` that calculates the greatest common divisor (GCD) of two numbers using Euclid's algorithm, and another function called `calculate_gcd` that recursively calculates the GCD using the same algorithm. The `gcd` function prompts the user to enter two numbers, calls the `calculate_gcd` function with those numbers, and prints the result. The time complexity of the `calculate_gcd` function is O(log min(a, b)), and the step-by-step flow for the `calculate_gcd` function for the input `48` and `18` is as follows:* Initial call: `calculate_gcd(48, 18)`* Since `b` (18) is not 0, we proceed to the else block.* Next call: `calculate_gcd(18, 48 % 18) => calculate_gcd(18, 12)`* Since `b` (12) is not 0, we proceed to the else block.* Next call: `calculate_gcd(12, 18 % 12) => calculate_gcd(12, 6)`* Since `b` (6) is not 0, we proceed to |
| unit_test.py |  The code defines a function `gcd` to calculate the greatest common divisor (GCD) of two numbers, and also defines a class `TestGCDFunction` for unit testing the `gcd` function. |

</details>

---

## 🚀 Getting Started

 To get started with this project, follow these steps:<br>
1. Open the \\gcd.py\\ file in your preferred text editor or IDE.
2. Read through the code to understand the implementation of the GCD (Greatest Common Divisor) function.
3. Run the \\unit_test.py\\ file to execute the unit tests for the GCD function.
4. Modify the \\gcd.py\\ file to implement your own version of the GCD function.
5. Test your implementation by running the \\unit_test.py\\ file again.
6. Once you are satisfied with your implementation, you can use it in your own projects or share it with others.

---

Generated with ❤️ by [ReadMeAI](https://www.readmeai.co/).
