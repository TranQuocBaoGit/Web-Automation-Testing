# Web-Automation-Testing

## Installation

Prepare as follow

```bash
# Clone project
git clone https://github.com/TranQuocBaoGit/Web-Automation-Testing.git
cd Web-Automation-Testing

# Install global package
pip install -U pytest
python3 -m pip install openpyxl

# Create virtual environment and install package
python -m venv venv
venv\Scripts\Activate
pip install selenium
pip install Pillow
```

To deactivate virtual environment

```bash
deactivate
```

## Run test

To run tests, run the following command

```bash
pytest [-option] [file]      # perform test
  -option:
      [-v]: give more detail
      [-s]: show print statement
      [-k keyword]: execute test with name match certain keyword
   file: execute certain file (test all if not specified)
```

## Note

All testcase file must be `test_[something].py`
