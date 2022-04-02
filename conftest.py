# -*- coding: utf-8 -*-
import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", default="200")


@pytest.fixture
def url_and_code(request):
    return {"url": request.config.getoption("--url"),
            "status_code": request.config.getoption("--status_code")
            }
