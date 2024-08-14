import allure
import pytest
import requests

import helpers

from attach.allure_attach import response_attaching, response_logging
from data import Endpoints


@pytest.fixture
def url_api():
    return 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def currier_data():
    data_currier = helpers.RandomUsers()
    return data_currier.generate_random_data()


@pytest.fixture(scope='function')
def create_user(url_api):
    methods = helpers.RandomUsers()
    data = methods.generate_random_data()

    response_post = requests.post(url_api + Endpoints.REGISTER, data=data)
    token = response_post.json()['accessToken']

    headers = {
        "Content-type": "application/json",
        "Authorization": f'{token}'
        }

    yield response_post, data

    requests.delete(url_api + Endpoints.DELETE_USER, headers=headers)


@pytest.fixture()
def api_request_and_validate():
    def _api_request_and_validate(url,
                                  method=None,
                                  data=None,
                                  params=None,
                                  headers=None,
                                  expected_status_code=None):
        if method == 'get':
            response = requests.get(url, params=params, headers=headers)
        elif method == 'post':
            response = requests.post(url, json=data)
        elif method == 'patch':
            response = requests.patch(url, json=data, headers=headers)
        else:
            raise ValueError('Неизвестный метод запроса')
        with allure.step(f"Проверка, API возвращает ожидаемый код статус для {url}"):
            assert response.status_code == expected_status_code
        response_logging(response)
        response_attaching(response)
        return response
    return _api_request_and_validate
