import allure

import helpers
from data import Endpoints, TextAnswer


@allure.suite('Авторизация')
@allure.title('Тестирование логина пользователя')
class TestLogInUser:
    @allure.title('Тестирование логина под существующим пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при логине под существующим пользователем')
    def test_login_existing_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        del data["name"]
        response = api_request_and_validate(f'{url_api}{Endpoints.LOGIN}',
                                            method='post',
                                            data=data,
                                            expected_status_code=200)

        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование логина с неверным логином и паролем')
    @allure.description('Возвращается код и текст ответа, при логине с неверным логином и паролем')
    def test_login_with_incorrect_data(self, url_api, api_request_and_validate):
        methods = helpers.RandomUsers()
        data = methods.generate_random_data()
        del data["name"]
        response = api_request_and_validate(f'{url_api}{Endpoints.LOGIN}',
                                            method='post',
                                            data=data,
                                            expected_status_code=401)

        assert TextAnswer.INCORRECT_DATA in response.text

    @allure.title('Тестирование логина с неверным паролем')
    @allure.description('Возвращается корректный код и текст ответа, при логине с неверным паролем')
    def test_login_with_incorrect_pass(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        del data["name"]
        data['password'] = ''
        response = api_request_and_validate(f'{url_api}{Endpoints.LOGIN}',
                                            method='post',
                                            data=data,
                                            expected_status_code=401)

        assert TextAnswer.INCORRECT_DATA in response.text

    @allure.title('Тестирование логина с неверным логином')
    @allure.description('Возвращается корректный код и текст ответа, при логине с неверным логином')
    def test_login_with_incorrect_login(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        del data["name"]
        data['email'] = ''
        response = api_request_and_validate(f'{url_api}{Endpoints.LOGIN}',
                                            method='post',
                                            data=data,
                                            expected_status_code=401)

        assert TextAnswer.INCORRECT_DATA in response.text
