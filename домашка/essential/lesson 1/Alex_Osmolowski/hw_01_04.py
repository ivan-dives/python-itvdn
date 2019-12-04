# - ваш объект должен уметь печататься через print (подсказка _str_)
# - ваш объект должен уметь арифметику: + - / % *
# - ваш объект должен уметь сравнения < <= == >= >
# - ваш объект должен уметь not
# - ваш объект должен уметь if myobj (подсказка _bool_)
# - ваш объект должен уметь отвечать функции len (подсказка _len_)
# - ваш объект должен уметь сказать Привет в момент создания и Досвидания в момент смерти (подсказка _init_ _del_)
# - ваш объект должен уметь кастоваться в int()
# - ваш объект должен поддерживать любой метод (подсказка _getattr_)


class LandPlot:
    """Класс - участок земли"""
    def __init__(self, length, width, price, address):
        self.length = length
        self.width = width
        self.price = price
        self.address = address
        print("Приветствую вас! Я - это:")

    def __getattr__(self, item):
        if item == "size_in_ga":
            return (self.length*self.width)/10000
        else:
            return "пока информация отсутсвует"

    def __len__(self):
        return len(str(self.length))+len(str(self.width))+len(str(self.price))+len(self.address)

    def __bool__(self):
        return self.length > 0 and self.width > 0 and self.price > 0 and self.address.strip() != ""

    def __int__(self):
        return self.length * self.width

    def __eq__(self, other):
        if not isinstance(other, LandPlot):
            return False
        return self.address == other.address and \
               self.width == other.width and \
               self.length == other.length and \
               self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, LandPlot):
            return True
        else:
            return  self.address != other.address or \
                    self.width != other.width or \
                    self.length != other.width or \
                    self.price != other.price

    def __str__(self):
        __frm_tmpl = "Земельный участок по адресу:\n{}\nДлина: {} м\nШирина: {} м\nРазмер: {}га\nЦена: ${}" + \
            "\nLength data in object type of 'LandPlot' = {} symbols"
        return __frm_tmpl.format(self.address, self.length, self.width, self.size_in_ga, self.price, len(self))

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __add__(self, other):
        return int(self) + int(other)

    def __neg__(self):
        return -int(self)

    def __sub__(self, other):
        return int(self) - int(other)

    def __mul__(self, other):
        return int(self) * int(other)

    def __truediv__(self, other):
        return int(self) / int(other)

    def __floordiv__(self, other):
        return int(self) // int(other)

    def __mod__(self, other):
        return int(self) % int(other)

    def __del__(self):
        print('Земельный участок по адресу "{}" прощается с вами!'.format(self.address))


def main():
    lnd = LandPlot(100, 50, 1500, "Переяслав-Хмельницкий район")
    print("lnd:")
    if lnd:
        print(lnd)
    else:
        print("Странный участок!")
    print("Площадь участка: {} кв. м".format(int(lnd)))
    print()

    print("lnd_copy:")
    lnd_copy = LandPlot(100, 50, 1500, "Переяслав-Хмельницкий район")
    if lnd_copy:
        print(lnd_copy)
    else:
        print("Странный участок!")
    print("Площадь участка: {} кв. м".format(int(lnd_copy)))
    print()

    if lnd == lnd_copy:
        print("Два участка идентичны!")
    else:
        print("Это разные участки!")

    print()
    print("lnd_other:")
    lnd_other = LandPlot(10, 20, 10000, "Бориспольский район")
    if lnd_other:
        print(lnd_other)
    else:
        print("Странный участок!")
    print("Площадь участка: {} кв. м".format(int(lnd_other)))
    print()

    print("lnd < lnd_copy:", lnd < lnd_copy)
    print("lnd <= lnd_copy:", lnd <= lnd_copy)
    print("lnd > lnd_other:", lnd > lnd_other)
    print("lnd >= lnd_other:", lnd >= lnd_other)
    print("-lnd =", -lnd)
    print("lnd + lnd_other =", lnd + lnd_other)
    print("lnd - lnd_other =", lnd - lnd_other)
    print("lnd * lnd_other =", lnd * lnd_other)
    print("lnd / lnd_other =", lnd / lnd_other)
    print("lnd // lnd_other =", lnd // lnd_other)
    print("lnd % lnd_other =", lnd % lnd_other)
    print()


if __name__ == '__main__':
    main()
