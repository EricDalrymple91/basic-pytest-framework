FROM python:3

RUN python -m venv venv2

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY conftest.py /conftest.py
COPY pytest.ini /pytest.ini
COPY setup.py /setup.py
COPY . /tests

ENTRYPOINT [ "pytest" ]
