user_input = "a"

# try:
#     int(user_input)
# except Exception as error:
#     print("Error", error)


class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value: {value}"
        super().__init__(message)


# my_val = 999
# if my_val > 998:
#     raise IncorrectValueError(my_val)


class MyError(Exception):
    def __init__(self, message):
        new_message = f"ERROR {message}"
        super().__init__(new_message)


raise MyError("test error")
