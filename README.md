# Saucedemo.com E2E UI Test

This project contains an E2E UI test for saucedemo.com using Selenium and Python.

## Prerequisites

- Python 3.8+
- Chrome browser
- ChromeDriver (make sure it's in your PATH)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/ILLnar-Nizami/saucedemo-e2e-test.git
   cd saucedemo-e2e-test
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the test

To run the E2E UI test for saucedemo.com:

```
pytest tests/test_saucedemo.py
```

## Notes

- Make sure you have the latest version of ChromeDriver installed and it's in your system PATH.
- The test uses the standard test account for saucedemo.com. If the credentials change, update them in the test file.
