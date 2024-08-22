import allure

from data import Endpoints, TextAnswer, Ingredients


@allure.suite('Получение списка заказов')
@allure.title('Тестирование получения списка заказов')
class TestGetOrders:
    @allure.title('Тестирование получения заказа авторизованным пользователем')
    @allure.description('Возвращается корректный код и текст ответа, при получении заказа авторизованным пользователем')
    def test_take_order_auth_user(self, api_request_and_validate, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.SAUCE, Ingredients.BUN]}
        api_request_and_validate(Endpoints.CREATE_ORDER,
                                 method='post',
                                 data=ingredients,
                                 headers=headers)

        response = api_request_and_validate(Endpoints.GET_ORDER,
                                            method='get',
                                            headers=headers)

        assert response.status_code == 200
        assert TextAnswer.TRUE in response.text

    @allure.title('Тестирование получения заказа неавторизованным пользователем')
    @allure.description(
        'Возвращается корректный код и текст ответа, при получении заказа неавторизованным пользователем')
    def test_take_order_unauthorized_user(self, api_request_and_validate):
        response = api_request_and_validate(Endpoints.GET_ORDER,
                                            method='get')

        assert response.status_code == 401
        assert TextAnswer.ORDER_WITHOUT_AUTH in response.text