import allure

from data import Endpoints, TextAnswer
from helpers import RandomUsers


@allure.suite('Создание пользователя')
@allure.title('Тестирование создания пользователя')
class TestCreateUser:
    @allure.title('Тестирование создание уникального пользователя')
    @allure.description('Возвращается корректный код и текст ответа')
    def test_create_user(self, url_api, api_request_and_validate):
        data = RandomUsers().generate_random_data()
        response = api_request_and_validate(url=f'{url_api}{Endpoints.REGISTER}',
                                            method='post',
                                            data=data,
                                            expected_status_code=200)

        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование создания пользователя с существующим email')
    @allure.description('Возвращается корректный код и текст ответа, при создании пользователя с существующим email')
    def test_create_user_already_registered(self, url_api, api_request_and_validate):
        existing_user_email = 'baba_jaga@example.com'
        data = RandomUsers().generate_random_data()
        data['email'] = existing_user_email
        response = api_request_and_validate(f'{url_api}{Endpoints.REGISTER}',
                                            method='post',
                                            data=data,
                                            expected_status_code=403)

        assert response.json()['message'] == TextAnswer.ALREADY_EXISTS

    @allure.title('Тестирование создания пользователя без обязательных полей')
    @allure.description('Отправка запроса на создание пользователя без обязательного поля - пароля')
    def test_create_user_missing_required_field(self, url_api, api_request_and_validate):
        data = RandomUsers().generate_random_data()
        del data["password"]
        response = api_request_and_validate(url=f'{url_api}{Endpoints.REGISTER}',
                                            method='post',
                                            data=data,
                                            expected_status_code=403)

        assert TextAnswer.FALSE in response.text
