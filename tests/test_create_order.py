import allure

from data import Endpoints, Ingredients, TextAnswer


@allure.suite("Создание заказа")
@allure.title("Тестирование создания заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_auth_create_order(self, create_user, api_request_and_validate):
        user_response, user_data = create_user
        del user_data["name"]
        api_request_and_validate(Endpoints.LOGIN,
                                 method='post',
                                 data=user_data)

        ingredients = [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.SAUCE, Ingredients.BUN]
        response = api_request_and_validate(Endpoints.CREATE_ORDER,
                                            method='post',
                                            data={"ingredients": ingredients})

        assert response.status_code == 200
        assert TextAnswer.TRUE in response.text

    @allure.title("Создание заказа без авторизации")
    def test_no_auth_create_order(self, api_request_and_validate):
        ingredients = [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.SAUCE, Ingredients.BUN]
        response = api_request_and_validate(Endpoints.CREATE_ORDER,
                                            method='post',
                                            data={"ingredients": ingredients})

        assert response.status_code == 200
        assert TextAnswer.TRUE in response.text

    @allure.title("Создание заказа без ингредиентов")
    def test_auth_create_order_without_ingredients(self, create_user, api_request_and_validate):
        user_response, user_data = create_user
        del user_data["name"]
        api_request_and_validate(Endpoints.LOGIN,
                                 method='post',
                                 data=user_data)

        ingredients = {"ingredients": ['']}
        response = api_request_and_validate(Endpoints.CREATE_ORDER,
                                            method='post',
                                            data={"ingredients": ingredients})

        assert response.status_code == 400
        assert TextAnswer.NOT_INGREDIENT in response.text

    @allure.title("Создание заказа с некорректным хэшем")
    def test_no_auth_create_order_incorrect_hash(self, api_request_and_validate):
        ingredients = [Ingredients.ENIGMA, Ingredients.KOKLETA]
        response = api_request_and_validate(Endpoints.CREATE_ORDER,
                                            method='post',
                                            data={"ingredients": ingredients})

        assert response.status_code == 500
        assert TextAnswer.ORDER_INCORRECT_INGREDIENTS in response.text
