from datetime import datetime


class TestClass:
    def __init__(
        self,
        name,
        age,
        param1,
        param2,
        param3,
        param4,
        param5,
        param6,
        param7,
        param8,
        param9,
        param10,
        param11,
    ):

        self.name = name
        self.age = age

    def datetime_return(self):
        return datetime.now()

    def test_method(self):
        """This is a docstring."""

        return self.name + self.age

    def test_age(self):

        return "Trying to create a very long line to see if the linter is \
                going to complain, maybe it needs to be a little bit longer"

    def testing_long_dictionary(self):

        my_dict = {
            "this": "is",
            "a": "very",
            "long": "dictionary",
            "lets": "make",
            "it": "even",
            "_long": "er",
        }
        return my_dict

    def testing_long_list(self):

        my_list = [
            "this",
            "is",
            "a",
            "very",
            "long",
            "list",
            "lets",
            "make",
            "it",
            "longer",
        ]
        return my_list
