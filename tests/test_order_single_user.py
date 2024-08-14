import allure

from data import Endpoints, TextAnswer, Ingredients


@allure.suite('Получение списка заказов')
@allure.title('Тестирование получения списка заказов')
class TestGetOrders:
    @allure.title('Тестирование получения заказа авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при получении заказа авторизованным пользователем')
    def test_take_order_auth_user(self, url_api, api_request_and_validate, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.SAUCE, Ingredients.BUN]}
        api_request_and_validate(f'{url_api}{Endpoints.CREATE_ORDER}',
                                 method='post',
                                 data=ingredients,
                                 headers=headers,
                                 expected_status_code=200)

        response = api_request_and_validate(f'{url_api}{Endpoints.GET_ORDER}',
                                            method='get',
                                            headers=headers,
                                            expected_status_code=200)

        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование получения заказа неавторизованным пользователем')
    @allure.description(
        'Возвращается корректный код и текст ответа, при получении заказа неавторизованным пользователем')
    def test_take_order_unauthorized_user(self, url_api, api_request_and_validate):
        response = api_request_and_validate(f'{url_api}{Endpoints.GET_ORDER}',
                                            method='get',
                                            expected_status_code=401)

        assert TextAnswer.ORDER_WITHOUT_AUTH in response.text