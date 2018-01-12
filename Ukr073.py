# -*- coding: utf-8 -*-

class SuperStr(str):
    row = ''

    def __init__(self, row):
        self.row = row

    def is_repeatance(self, s):
        len_p = len(self.row) / len(s)
        if s * len_p == self.row:
            return True
        else:
            return False

    def is_palindrom(self):
        # -*- coding: utf-8 -*-

        chet = len(self)%2
        half_len = len(self)/2
        l_begin = []
        l_end = []

        # l_begin набить прямой строкой
        # l_end набить реверснутой
        # сравнить, одинаковы ли они до половины


        for i in range(half_len):
            pass

        return self


s = SuperStr('121121121121')

print s.is_repeatance('121')
print s.is_palindrom()
