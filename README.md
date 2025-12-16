# Fuzzy Logic Medical Dose Calculator 🌡️💊

A Python-based **Fuzzy Inference System (FIS)** designed to calculate the appropriate pharmaceutical dosage based on a patient's body temperature. This project demonstrates the core principles of Fuzzy Logic control, including fuzzification, rule evaluation, and defuzzification, implemented from scratch without external libraries.

## 🧠 Key Features

* **Custom Fuzzy Sets:** Defines linguistic variables for Temperature (`LOW`, `HIGH`) and Dose (`LOW`, `HIGH`) with configurable membership functions.
* **Dual Inference Methods:** Supports user selection between two standard implication methods:
    * **MIN (Mamdani):** Truncates the output fuzzy set.
    * **PRODUCT (Larsen):** Scales the output fuzzy set.
* **Linear Interpolation:** Implements a custom algorithm to calculate membership degrees for continuous input values.
* **Defuzzification:** Uses the **Center of Gravity (CoG)** method to convert the aggregated fuzzy result into a crisp numerical output (Dose).
* **Configurable Scenarios:** Allows switching between "Default" and "Alternative" fuzzy set definitions to observe system behavior changes.

## ⚙️ How It Works

The system follows the standard Fuzzy Logic pipeline:

1.  **Fuzzification:** The crisp input (Temperature, e.g., 38.5°C) is mapped to fuzzy membership degrees (e.g., 0.5 LOW, 0.5 HIGH).
2.  **Rule Evaluation:** Applies logical rules:
    * *Rule 1:* IF Temperature is **HIGH** THEN Dose is **HIGH**.
    * *Rule 2:* IF Temperature is **LOW** THEN Dose is **LOW**.
3.  **Aggregation:** Combines the results of the rules using the MAX operator.
4.  **Defuzzification:** Calculates the weighted average (Centroid) to determine the final dosage.

## 🚀 How to Run

1.  Ensure you have Python installed.
2.  Download the script (e.g., `main.py`).
3.  Run the program via terminal:
    ```bash
    python main.py
    ```
4.  Follow the interactive prompts to select the inference method and input the patient's temperature.

## 📝 Usage Example

```text
Fuzzy Logic System for Dose Calculation
--------------------------------------------------------
Select fuzzy sets (1: Default, 2: Alternative): 1
Select inference method (1: MIN, 2: PRODUCT): 2

Enter patient temperature (37-40°C): 38.5

Recommended dose (PRODUCT method): 5.00 units
```
---
*Developed for the University of Piraeus*
