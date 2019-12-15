# basic-pytest-demo
This project demonstrates the basic usage of `pytest` - a tool
for performing unit testing in python. This project
uses the example of a simple function to test for primality. Unit
tests are added to test edge cases and a number of examples of prime
and non-prime numbers.

### Setup
Python 3.6 or should be used for this project. 
Package install using base python install:
```shell script
pip3 install -r requirements.txt
```

Alternatively, if using a virtual environment use:
```shell script
python -m pip install -r requirements.txt
```

### Command line usage (linux only)

```shell script
./is_prime.py <positive_integer>
```

### Running the tests
The unit tests are defined in the `test_is_prime.py` file. To run the
unit tests use:
```shell script
pytest .
```
