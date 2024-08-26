import random
import string


class RandomUsers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_data():
        email = RandomUsers.generate_random_string(5) + "@gmail.com"
        password = RandomUsers.generate_random_string(10)
        name = RandomUsers.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name}

        return payload


class IngredientsNone:

    ingredients_none = {"ingredients":
                        {"ingredients": ['']}
                        }

