from random import choice


class Encryptor:

    string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
    string_l = list(string)
    def fCrypt(self, msg, d1, d2) -> str:
        """
        depending on what d1 and d2 are it might encrypt or decrypt. \n
        To encrypt: \n
          d1 and d2, repectevily. \n
        To decrypt:
          rd2 and rd1. \n
        
        """
        txt = ""
        for ch in msg:
            txt += d2[ d1[ch]]
        return txt

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

    def fGenEncDecFunc(self) -> "fEnc, fDec":
        """
        Make functions ready to encrypt and decrypt, \n
        with ready input. \n
        """
        d1, d2, rd1, rd2 = self.fGenDictPairAndReverse()
        fEnc = lambda msg: self.fCrypt(msg, d1, d2)
        fDec = lambda txt: self.fCrypt(txt, rd2, rd1)
        return fEnc, fDec

        