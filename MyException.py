class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("Это мое собственное исключение!")
except MyCustomException as e:

    print("Поймано мое собственное исключение:", e)

