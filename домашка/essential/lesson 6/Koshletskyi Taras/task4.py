#!/usr/bin/python3
# -*- coding: utf-8 -*_


def foo(**kwards):
    for k, v in kwards.items():
        print(f"key is {k}, value is {v}")

boo = {"key1":"value1", "key2":"value2", "key3":"value3", "key4":"value4",}

foo(**boo)