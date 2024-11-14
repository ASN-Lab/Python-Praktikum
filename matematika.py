import math
import random
import statistics

class Matematika:
    PI = math.pi

    @staticmethod
    def luas_lingkaran(r):
        return Matematika.PI * r ** 2

    @staticmethod
    def luas_persegi(s):
        return s ** 2

    @staticmethod
    def keliling_lingkaran(r):
        return 2 * Matematika.PI * r

    @staticmethod
    def volume_kubus(s):
        return s ** 3

    @staticmethod
    def akar_kuadrat(x):
        return math.sqrt(x)

    @staticmethod
    def rata_rata(data):
        return statistics.mean(data)

    @staticmethod
    def bilangan_acak(min_value, max_value):
        return random.randint(min_value, max_value)
        