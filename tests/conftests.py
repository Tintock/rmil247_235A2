import os
import pytest

from wsgi import create_app
from memory_repo import memory_repository


TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'user', 'OneDrive', 'UNI', 'CS235', 'repo 02.07.2020',
                              'A2MOVIE', 'tests', 'data')


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False                       # test_client will not send a CSRF token, so disable validation.
    })

    return my_app.test_client()