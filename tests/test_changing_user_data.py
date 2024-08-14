import allure
import requests

from data import Endpoints, TextAnswer


@allure.suite('Изменение данных пользователя')
@allure.title('Тестирование изменения авторизованным и не неавторизованным пользователем')
class TestChangingDataUsers:
    @allure.title('Тестирование изменения емейла авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении емейла авторизованным пользователем')
    def test_auth_replacing_email_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_email_value = 'f' + response_created.json()["user"]['email']
        new_email = {"email": new_email_value}
        response = api_request_and_validate(f'{url_api}{Endpoints.PLACE_DATA}',
                                            method='patch',
                                            data=new_email,
                                            headers=headers,
                                            expected_status_code=200)

        assert response.json()['user']['email'] == new_email['email']

    @allure.title('Тестирование изменения пароля авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении пароля авторизованным пользователем')
    def test_auth_replacing_password_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_password_value = 'x' + data["password"]
        new_password = {"password": new_password_value}
        response = api_request_and_validate(f'{url_api}{Endpoints.PLACE_DATA}',
                                            method='patch',
                                            data=new_password,
                                            headers=headers,
                                            expected_status_code=200)

        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование изменения имени авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении имени авторизованным пользователем')
    def test_auth_replacing_name_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_name_value = 'f' + response_created.json()["user"]["name"]
        new_name = {"name": new_name_value}
        response = api_request_and_validate(f'{url_api}{Endpoints.PLACE_DATA}',
                                            method='patch',
                                            data=new_name,
                                            headers=headers,
                                            expected_status_code=200)

        assert response.json()['user']['name'] == new_name['name']

    @allure.title('Тестирование изменения имени неавторизованным пользователем')
    @allure.description(
        'Возвращается корректный код и текст ответа, при изменении имени неавторизованным пользователем')
    def test_not_auth_replacing_date_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        requests.post(url_api + Endpoints.CREATE_USER, data=data)
        headers = {"Content-type": "application/json"}
        new_name_value = 'f' + response_created.json()["user"]["name"]
        new_name = {"name": new_name_value}
        response = api_request_and_validate(f'{url_api}{Endpoints.PLACE_DATA}',
                                            method='patch',
                                            data=new_name,
                                            headers=headers,
                                            expected_status_code=401)

        assert TextAnswer.UNAUTHORIZED in response.text