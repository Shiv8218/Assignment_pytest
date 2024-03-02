import pytest


@pytest.mark.sanity
def test_login():
    print("Hello world!")


@pytest.mark.smoke
def test_login1():
    print("Hello world!")