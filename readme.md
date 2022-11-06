## How to run tests

# Run all tests
- pytest tests

# Run pytest-bdd tests
- pytest tests/test_pytest_bdd/step_defs/test_api.py 
- pytest tests/test_pytest_bdd/step_defs/test_ui.py  
- pytest -m API
- pytest -m UI
- pytest -m 'API or UI'
