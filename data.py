

class Endpoints:
    LOGIN = "api/auth/login"
    REGISTER = "api/auth/register"
    LOGOUT = "api/auth/logout"
    CREATE_USER = "api/auth/user"
    DELETE_USER = "api/auth/user"
    PLACE_DATA = "api/auth/user"
    CREATE_ORDER = "api/orders"
    GET_ORDER = "api/orders"


class TextAnswer:
    TRUE = '"success":true'
    FALSE = '"success":false'
    ALREADY_EXISTS = 'User already exists'
    INCORRECT_DATA = 'email or password are incorrect'
    UNAUTHORIZED = 'You should be authorised'
    NOT_INGREDIENT = 'Ingredient ids must be provided'
    ORDER_INCORRECT_INGREDIENTS = 'Internal Server Error'
    ORDER_WITHOUT_AUTH = 'You should be authorised'
    INCORRECT_FIELDS = 'Email, password and name are required fields'


class Ingredients:
    SAUCE = '61c0c5a71d1f82001bdaaa72'
    BUN = "61c0c5a71d1f82001bdaaa6d"
    KOKLETA = '61c0c5a71d1f82001bdaaa71'
    MEAT = '61c0c5a71d1f82001bdaaa6f'
    ENIGMA = '00000000000000000000000000'
