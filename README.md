# Basic PyTest Framework

# Setup

```
# Clone the repo to your local machine
git clone https://github.com/EricDalrymple91/basic-pytest-framework.git
cd basic-pytest-framework

# Create a virtual environment
pip install virtualenv
python3 -m venv venv
source venv/bin/activate

# Install the necessary python packages
pip install -r requirements.txt
```

# Usage

```
# Default usage
pytest

# Run a particular input
pytest --t "Here we are" --n "10"

# Run a particular mark
pytest -m text

# Run all but a particular category
pytest -m "not number"
```

# Docker Usage

```
docker build --tag thisimg .
docker run thisimg:latest
```