<div align="center">

  <h1>AKTU OneView Roll Number Validator</h1>
  <p>
    <strong>Fast & Simple tool to check valid AKTU roll numbers using response length heuristic</strong>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Status-Working-brightgreen?style=for-the-badge" alt="Status">
  </p>

</div>

## Features
- Single roll number check
- Bulk range check (very fast with delay to avoid blocking)
- Saves valid roll numbers automatically to `valid.txt`
- Beautiful colored terminal output
- No length spoilers in output 😉

## Demo / Screenshot

<img width="394" height="179" alt="image" src="https://github.com/user-attachments/assets/b199ecbf-7fe3-4f00-a519-51059c26c4a2" />
<img width="363" height="307" alt="image" src="https://github.com/user-attachments/assets/282d04a0-31d3-4bab-8bdc-9dd7815c433f" />
<img width="341" height="272" alt="image" src="https://github.com/user-attachments/assets/734446b0-4141-47c1-85a6-b93922009262" />


## Installation

```bash
# 1. Clone repo
git clone https://github.com/Rekhansh/aktu-roll-checker.git
cd aktu-roll-checker

# 2. Install dependencies (recommended in virtual environment)
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt

python main.py

```


Disclaimer

- For educational & personal use only.
- Respect AKTU server – don't spam / run very large ranges without delay.
- Use at your own risk.



