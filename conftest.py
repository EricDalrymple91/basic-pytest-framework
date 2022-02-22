def pytest_addoption(parser):
    parser.addoption("--n", action="store", default='5')
    parser.addoption("--t", action="store", default='Hello')
