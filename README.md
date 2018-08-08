## Requirements
Python 3.6.5

python-pip

Mozilla Firefox 61.0.1

geckodriver 0.21.0

Install dependencies:
```sh
pip install -r requrements.txt
```
Data for tests should be provided in files (specify type and path in config.py: csv, xml or sqlite)

##Run test
```sh
py.test --resultlog=logs/result.log tests.py
```

Test execution info can be found in /logs:
- pytest.log (detailed log)
- result.log (execution result)
- screenshots