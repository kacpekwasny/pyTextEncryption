from random import choice, randint
from copy import deepcopy

class EncryptorSt:
    
    vector = 0
    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
    string_l = list(string)
    slen = len(string)

    def __init__(self):
        d1, d2, rd1, rd2 = self.fGenDictPairAndReverse()
        self.key_l = self.fGenKeyl(100, 40)
        self.d1 = d1
        self.d2 = d2
        self.rd1 = rd1
        self.rd2 = rd2

    def fEncrypt(self, msg, key_l, d1, d2) -> str:
        """
        Encrypt message. \n
          Variable ex.: \n
            key_l = [1, 30, 12, -88, 12, -30, -11] \n
        """
        txt = ""
        l = len(key_l)
        for i, ch in enumerate(msg):
            v = key_l[i%l]
            self.vector = (self.vector + v) % self.slen
            txt += d2[ (d1[ch] + self.vector) % self.slen ]
        return txt
    
    def fDecrypt(self, txt, key_l, rd1, rd2) -> str:
        """
        Decrypt message. \n
          Variable ex.: \n
            txt - encrypted message, \n
            key_l = [1, 30, 12, -88, 12, -30, -11], \n
        """
        msg = ""
        l = len(key_l)
        for i, ch in enumerate(txt):
            v = key_l[i%l]
            self.vector = (self.vector + v) % self.slen
            index = (rd2[ch] - self.vector + self.slen) % self.slen
            msg += rd1[index]
        return msg


    def fEnc(self, msg) -> str:
        return self.fEncrypt(msg, self.key_l, self.d1, self.d2)

    def fDec(self, txt) -> str:
        return self.fDecrypt(txt, self.key_l, self.rd1, self.rd2)

    def fGenDictPairAndReverse(self) -> (dict, dict, dict, dict):
        # ENCRYPTION DICTS
        # make d1
        d1 = dict( [ (char, i) for i, char in enumerate(self.string)] )
        # make d2
        d2 = {}
        i = 0
        ls = self.string_l[:]
        while len(ls) > 0:
            char = choice(ls)
            ls.remove(char)
            d2[i] = char
            i += 1
        
        # DECRYPTION DICTS
        rd1 = dict( [ (v, k) for k, v in d1.items() ] )
        rd2 = dict( [ (v, k) for k, v in d2.items() ] )

        return d1, d2, rd1, rd2

    def fGenKeyl(self, max_, size) -> list:
        return [randint(0, max_) for _ in range(size)]

    @classmethod
    def fMakePair(cls) -> "EncryptorSt, EncryptorSt":
        e1 = cls()
        return e1, deepcopy(e1)
        



    