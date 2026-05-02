import pytest

@pytest.fixture(scope='function',autouse=True)
def setup():
    print('Starting...')
    yield
    print('Ending....')