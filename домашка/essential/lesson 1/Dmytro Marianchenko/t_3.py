class Temperature:

    def __init__(self, tempo):
        self.tempo = tempo

    @property
    def tempo_to_c(self):
        return (self.tempo - 32) / 1.8

    @property
    def tempo_to_f(self):
        return (self.tempo + 32) * 1.8


def main():
    t = input("Input temperature in format '10 c' or '10 f':\n>>  ")
    container = t.split()
    arg1 = container[1]
    tempo = int(container[0])
    calc = Temperature(tempo)
    if arg1 == "f" or "F":
        result1 = calc.tempo_to_c
        print(f"{round(result1)} C")
    elif arg1 == "c" or "C":
        result1 = calc.tempo_to_f
        print(f"{round(result1)} F")


if __name__ == '__main__':
    main()
