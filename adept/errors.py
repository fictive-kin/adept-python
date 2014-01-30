# -*- coding: utf-8 -*-


class OperationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class AccountError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
