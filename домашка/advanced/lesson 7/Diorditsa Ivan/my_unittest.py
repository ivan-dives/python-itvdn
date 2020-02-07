import unittest
import unittest.mock

class Car:
    def __init__(self, speed=10):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def get_speed_from_other_function(self, foo):
        self.__speed = foo()


class MyTests(unittest.TestCase):
    def setUp(self):
        self.mycar = Car(20)
        self.mymock = unittest.mock.Mock(return_value=15)

    def test_car_speed_is_sane(self):
        self.assertEqual(self.mycar.get_speed(), 20)

    def test_python_interpreter_is_sane(self):
        self.assertTrue(1 == 1)

    def test_initialize_car(self):
        other_car = Car()
        other_car.get_speed_from_other_function(self.mymock)
        self.assertEqual(other_car.get_speed(), 15)

    def tearDown(self):
        del self.mycar
