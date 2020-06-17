clean:
# Remove Python build artifacts
	find . -name 'dist' -type d -exec rm -rf {} +
	find . -name '*.egg-info' -type d -exec rm -rf {} +
	find . -name '*.pyc' -delete
	find . -name '*pycache*' -delete

format:
	black chess_analysis
	isort chess_analysis/*
	flake8 chess_analysis/

test:
# Create a Python environment and run tests
	tox --recreate -e py36
	.tox/py36/bin/pip freeze > dev_requirements.txt
	sed -i '/^chess-analysis/d' ./dev_requirements.txt

devenv:
# A Python 3.6 virtualenv should be activated before running this.
# Install all of our dependencies into the user's active Python virtualenv
	pip install -e .
	pip install -r dev_requirements.txt

qtest:
# The dev virtualenv should be activated, and then we can test quickly without using tox
# The '-s' argument tells pytest to show us all of the output instead of hiding it 
	pytest -s
