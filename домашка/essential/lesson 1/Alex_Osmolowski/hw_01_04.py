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

    def __getattr__(self, item):
        if item == "size_in_ga":
            return (self.length*self.width)/10000
        else:
            return "пока информация отсутсвует"

    def __bool__(self):
        return self.length > 0 and self.width > 0 and self.price > 0 and self.address.strip() != ""

    def __int__(self):
        return self.length * self.width

    def __eq__(self, other):
        if not isinstance(other, LandPlot):
            return False
        return self.address == other.address and self.width == other.width and \
               self.length == other.width and self.price == other.price

    def __ne__(self, other):
        if not isinstance(other, LandPlot):
            return True
        else:
            return  self.address != other.address or \
                    self.width != other.width or \
                    self.length != other.width or \
                    self.price != other.price

    def __str__(self):
        __frm_tmpl = "Земельный участок по адресу:\n{}\nДлина: {} м\nШирина: {} м\nРазмер: {}га\nЦена: ${}"
        return __frm_tmpl.format(self.address, self.length, self.width, self.size_in_ga, self.price)


def main():
    lnd = LandPlot(100, 50, 1500, "Переяслав-Хмельницкий район")
    lnd_copy = LandPlot(100, 50, 1500, "Переяслав-Хмельницкий район")
    # lnd_copy = lnd
    if lnd:
        print(lnd)
    else:
        print("Странный участок!")
    print("Площадь участка: {} кв. м".format(int(lnd)))

    print()
    if lnd_copy:
        print(lnd_copy)
    else:
        print("Странный участок!")

    if lnd == lnd_copy:
        print("Два участка идентичны!")
    else:
        print("Это разные участки!")


if __name__ == '__main__':
    main()
