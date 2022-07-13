import time


def decorator_with_time_sleep(call_count, start_sleep_time, factor, border_sleep_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Кол-во запусков =", call_count)
            print("Начало работы")
            t = start_sleep_time
            for i in range(call_count):
                print("Запуск номер", i + 1, "Ожидание:", t, "секунд")
                time.sleep(t)
                res = func(*args, **kwargs)
                print("Результат декорируемой функций =", res)
                t *= factor
                if t > border_sleep_time:
                    t = border_sleep_time
        return wrapper
    return decorator


@decorator_with_time_sleep(5, 1, 3, 20)
def test_function(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(i)
    return "result_of_test_function"


if __name__ == '__main__':
    test_function("qwerty", test="TEST")
