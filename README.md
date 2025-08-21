# Laptop Price Prediction QA Testing

This repo contains **manual + automated testing** for the Laptop Price Prediction app (Streamlit)
Developed a Streamlit-based web app to predict laptop prices using machine learning (trained regression model with preprocessing pipeline).

Implemented UI features allowing users to select hardware/software configurations (Brand, CPU, RAM, GPU, OS, etc.) to get price predictions.

Extended the project by adding a QA Testing Suite with Playwright + Pytest, ensuring app reliability through:

Automated UI testing (dropdowns, inputs, button clicks).

Parameterized test cases from CSV files for multiple laptop configurations.

Invalid input tests to verify application stability.

Integrated CI-ready test reports in HTML format for quick debugging and transparency.

Tools & Tech: Python, Streamlit, Scikit-learn, Playwright, Pytest, GitHub.

## Features
- Manual test cases (`docs/test-cases.csv`)
- Automated Playwright tests (`tests/test_laptop_price_app.py`)
- Pytest + HTML report support
