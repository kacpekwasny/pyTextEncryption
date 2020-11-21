from copy import deepcopy
from random import choice, randint
from encryptor import Encryptor


class EncryptorSt(Encryptor):
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"

    def __init__(self, keys_len: int, *key_steps_start_end: int):
        self.d = self.fGenDict()
        self.r = self.fReverseDict(self.d)
        self.keys = self.fGenKeys(keys_len, *key_steps_start_end)
        self.vector = 0

    def fInherit(self, other):
        self.d = other.d
        self.r = other.r
        self.keys = other.keys
        self.vector = other.vector

    def fEnc(self, message):
        encr_msg =  self.fEncryptKeys(message, self.fRotate(self.d, self.vector), self.keys)
        self.fUpdateVector(len(message))
        return encr_msg

    def fDec(self, text):
        msg = self.fDecryptKeys(text, self.fReverseDict(self.fRotate( self.d, self.vector)), self.keys)
        self.fUpdateVector(len(text))
        return msg
        
    @classmethod
    def fMakePair(cls, keys_len, *key_steps_start_end):
        e1 = cls(keys_len, *key_steps_start_end)
        e2 = cls(keys_len, *key_steps_start_end)
        e2.fInherit(e1)
        return e1, e2

    def fCountVector(self, steps) -> int:
        s = 0
        i = 0
        while i <= steps:
            s += self.keys[i % len(self.keys)]
            i += 1
        return s

    def fUpdateVector(self, steps):
        s = self.fCountVector(steps)
        self.vector = (self.vector + s) % len(self.d)

# # # # # # # # # # # #


if __name__ == "__main__":
    e = EncryptorSt(23, 17)
    ee = exit
    t = test
    en, de = e.fGenFuncs(200, 14)
    e1, e2 = e.fMakePair(23, 17)
    msg = "Quick brown fox jumped over the lazy dog!"






