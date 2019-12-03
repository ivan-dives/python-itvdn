#!/usr/bin/python3
# -*- coding: utf-8 -*_


class Editor:

    def __init__(self, key=None):
        self.key = key

    def view_document(self, document):
        print(f'View {document}')

    def edit_document(self, document):
        print(f'I can only View {document}, please buy ProVersion')


class ProEditor(Editor):

    __LICENSE = "QWERTY"

    def edit_document(self, document):
        if self.key == self.__LICENSE:
            print(f"You can edit this {document}")
        else:
            super().edit_document(document)

    def input_license(self, key):
        self.key = key


def main():
    edi = ProEditor()
    edi.view_document("My Document")
    edi.edit_document("My Document")
    edi.input_license("QWERTY")
    edi.edit_document("My Document")





if __name__ == '__main__':
    main()

