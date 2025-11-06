# Medical Diagnosis Expert System

## Overview
The Medical Diagnosis Expert System is designed to assist users in diagnosing potential medical conditions based on their reported symptoms. The system utilizes a Prolog knowledge base to define relationships between various symptoms and diseases, and a Python interface to interact with users.

## Project Structure
```
medical-diagnosis-expert-system
├── src
│   ├── prolog
│   │   └── knowledge_base.pl
│   └── python
│       └── interactive_diagnosis.py
├── tests
│   └── test_integration.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd medical-diagnosis-expert-system
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prolog Setup**
   Make sure you have a Prolog interpreter installed on your system to run the knowledge base.

## Usage
To use the Medical Diagnosis Expert System, run the Python interactive diagnosis script:
```bash
python src/python/interactive_diagnosis.py
```
Follow the prompts to input your symptoms, and the system will provide a potential diagnosis based on the Prolog knowledge base.

## Testing
Integration tests are provided to ensure the system works as expected. To run the tests, execute:
```bash
python -m unittest tests/test_integration.py
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.