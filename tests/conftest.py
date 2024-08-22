import allure
import pytest
import requests

import helpers

from attach.allure_attach import response_attaching, response_logging
from data import Endpoints


@pytest.fixture
def currier_data():
    data_currier = helpers.RandomUsers()
    return data_currier.generate_random_data()


@pytest.fixture(scope='function')
def create_user(currier_data):
    response_post = requests.post(Endpoints.REGISTER, data=currier_data)
    token = response_post.json()['accessToken']

    headers = {
        "Content-type": "application/json",
        "Authorization": f'{token}'
        }

    yield response_post, currier_data

    requests.delete(Endpoints.DELETE_USER, headers=headers)


@pytest.fixture
def auth_headers(create_user):
    response_created, _ = create_user
    token = response_created.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    yield headers


@pytest.fixture
def auth_updated_email(create_user):
    response_created, _ = create_user
    new_email_value = 'f' + response_created.json()["user"]['email']
    new_email = {"email": new_email_value}
    yield new_email


@pytest.fixture
def auth_new_password(create_user):
    response_created, data = create_user
    new_password_value = 'x' + data["password"]
    new_password = {"password": new_password_value}
    yield new_password


@pytest.fixture
def auth_updated_name(create_user):
    response_created, _ = create_user
    new_name_value = 'f' + response_created.json()["user"]["name"]
    new_name = {"name": new_name_value}
    yield new_name


@pytest.fixture
def non_auth_headers():
    headers = {"Content-type": "application/json"}
    yield headers


@pytest.fixture
def non_auth_updated_name(create_user):
    response_created, _ = create_user
    new_name_value = 'f' + response_created.json()["user"]["name"]
    new_name = {"name": new_name_value}
    yield new_name

@pytest.fixture
def api_request_and_validate():
    def _api_request_and_validate(url,
                                  method=None,
                                  data=None,
                                  params=None,
                                  headers=None):
        if method == 'get':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'post':
            response = requests.post(url, json=data)
        elif method == 'patch':
            response = requests.patch(url, json=data, headers=headers)
        else:
            raise ValueError('Неизвестный метод запроса')
        response_logging(response)
        response_attaching(response)
        return response
    return _api_request_and_validate
