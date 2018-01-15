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

        half_len = len(self) / 2
        l_begin = []
        l_end = []

        for i in self:
            l_begin.append(i)
            l_end.append(i)

        l_end.reverse()

        k = 0
        for i in range(half_len):
            if l_begin[i] != l_end[i]:
                k += 1
                break

        if k == 0:
            return True
        else:
            return False


s = SuperStr('1210121')

print s.is_repeatance('121')
print s.is_palindrom()
