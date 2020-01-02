#!/usr/bin/python3
# -*- coding: utf-8 -*_


def read_config(path):
    conf = {}
    with open(path) as f:
        line = f.readline()
        while line:
            lst = line.strip().split("=")
            conf[lst[0]] = lst[1]
            line = f.readline()
    return conf


def print_config(config):
    for k, v in config.items():
        print(f"{k}={v}")


def chenge_config(config, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        config[k] = v


def write_config(path, config):
    string = ""
    for k, v in config.items():
        string += f"{k}={v}\n"
    with open(path, 'w') as f:
        f.write(string)


def main():
    config = read_config("config.txt")
    print_config(config)
    chenge_config(config, username="petr", password="qwerty")
    print_config(config)
    write_config("config1.txt", config)


if __name__ == '__main__':
    main()
