# Rapyuta Robotics QA Automation Assignment

This repo is a sample automated test framework using pytest, for the demo website https://tmdb-discover.surge.sh/.
As the API is not documented, this repo *does not implement any actual test*. However, it is a complete framework that simply needs the technical knowledge about the product to be fully functionnal (which I assume is the relevant part of the assignment).

## Structure
Documentation :
- `testcase_description.md` documents the list of all planned test cases
- `test_results.md` lists the defects found while working on this framework
- `CI.md` explains an approach to integrating these tests on a CI environment

Test framework :
- `tests/` contains the code of the actual test cases
- As well as some individual files needed for the test framework : `conftest.py`, `pytest.ini`, `Jenkinsfile`, `requirements.txt`, `requirements_frozen.txt`


## How to run tests

### Setup a virtual environment
```
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements_frozen.txt
```

### Run all tests
```
pytest -s
```

### Run a specific test
```
pytest -s <path to test file or test function>
```