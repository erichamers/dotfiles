from datetime import datetime


def my_function(param1: str, param2: str, param3: int):

    my_dict = {
        "test": param1,
        "test2": param2,
        "test3": param3,
    }

    var1 = param1 + param2
    print(my_dict)

    return var1 * param3


my_function("test", "test2", 3)
