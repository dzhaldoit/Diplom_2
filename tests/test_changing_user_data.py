import allure
import requests

from data import Endpoints, TextAnswer


@allure.suite('Изменение данных пользователя')
@allure.title('Тестирование изменения авторизованным и не неавторизованным пользователем')
class TestChangingDataUsers:
    @allure.title('Тестирование изменения емейла авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении емейла авторизованным пользователем')
    def test_auth_replacing_email_user(self, api_request_and_validate, auth_updated_email, auth_headers):
        response = api_request_and_validate(Endpoints.PLACE_DATA,
                                            method='patch',
                                            data=auth_updated_email,
                                            headers=auth_headers)

        assert response.status_code == 200
        assert response.json()['user']['email'] == auth_updated_email['email']

    @allure.title('Тестирование изменения пароля авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении пароля авторизованным пользователем')
    def test_auth_replacing_password_user(self, api_request_and_validate, auth_headers, auth_new_password):
        response = api_request_and_validate(Endpoints.PLACE_DATA,
                                            method='patch',
                                            data=auth_new_password,
                                            headers=auth_headers)

        assert response.status_code == 200
        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование изменения имени авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при изменении имени авторизованным пользователем')
    def test_auth_replacing_name_user(self, api_request_and_validate, auth_headers, auth_updated_name):
        response = api_request_and_validate(Endpoints.PLACE_DATA,
                                            method='patch',
                                            data=auth_updated_name,
                                            headers=auth_headers)

        assert response.status_code == 200
        assert response.json()['user']['name'] == auth_updated_name['name']

    @allure.title('Тестирование изменения имени неавторизованным пользователем')
    @allure.description(
        'Возвращается корректный код и текст ответа, при изменении имени неавторизованным пользователем')
    def test_not_auth_replacing_date_user(self, api_request_and_validate, non_auth_headers, non_auth_updated_name):
        response = api_request_and_validate(url=Endpoints.PLACE_DATA,
                                            method='patch',
                                            data=non_auth_updated_name,
                                            headers=non_auth_headers)

        assert response.status_code == 401
        assert TextAnswer.UNAUTHORIZED in response.text
