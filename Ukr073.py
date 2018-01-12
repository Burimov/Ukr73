class SuperStr(str):
    row = ''

    def __init__(self, row):
        self.row = row

    def is_repeatance(self, s):
        len_p = len(self.row)/len(s)
        if s*len_p == self.row:
            return True
        else:
            return False


    def is_palindrom(self):
        pass


s = SuperStr('123123123123')

print s.is_repeatance('123')
