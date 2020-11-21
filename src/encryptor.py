from copy import deepcopy
from random import choice, randint


class Encryptor:
    chars = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c")
    default = dict([(c, c) for c in chars])

    def fEncryptKeys(self, message, key_char_char_d, key_steps_l) -> str:
        # aliases
        kch = deepcopy(key_char_char_d)
        kstp = deepcopy(key_steps_l)
        encr_msg = ""

        for i, l in enumerate(message):
            kch = self.fRotate(kch, key_steps_l[ (i+1) % (len(kstp)) ])
            encr_msg += kch[l]

        return encr_msg

    def fDecryptKeys(self, message, key_char_char_d, key_steps_l) -> str:
        return self.fEncryptKeys(message, key_char_char_d, [ -i for i in key_steps_l])

    def fEncryptDict(self, message, key_char_char_d) -> dict:
        return "".join( list( map(lambda x: key_char_char_d[x], message) ))

    def fRotate(self, key_char_char_d, steps) -> dict:
        """
        Rotate this by eight steps
        [0,1,2,3,4,5,6,7,8,9]
        end with:
        [2,3,4,5,6,7,8,9,0,1]
        Rotate <list of len 12 by 15> == Rotate by 3

        Unrotate by negating sign
        """
        key_char_char_d = deepcopy(key_char_char_d)

        sign = steps
        steps = abs(steps) % len(key_char_char_d) # ensures above
        values = list(key_char_char_d.values())

        if sign >= 0:
            values = values[-steps:] + values[:len(values) - steps]
        else:
            values = values[abs(steps):] + values[:abs(steps)]
        # values are now rotated
        
        # replace values with rotated
        for k, v in zip(key_char_char_d, values):
            key_char_char_d[k] = v
        
        return key_char_char_d

    def fReverseDict(self, key_char_char_d) -> dict:
        ret_d = {}
        for k, v in key_char_char_d.items():
            # {"k":"v", "i":"x", "j":"v"} → {"v":"k", "x":"i", !→"v":"j"}
            if v in ret_d:
                raise TypeError("multiple keys to same value")
            ret_d[v] = k
        return ret_d

    def fGenDict(self) -> dict:
        ret_d = deepcopy(self.default)
        chars = deepcopy(self.chars)
        for k in self.default.keys():
            c = choice(chars)
            chars.remove(c)
            ret_d[k] = c
        # If somone messes up big time
        if len(chars) > 0:
            raise NotImplementedError("Encryptor.fGenDict has not used chars left, unacceptable.")
        return ret_d

    def fGenKeys(self, length, *start_end) -> list:
        if len(start_end) > 2:
            raise NotImplementedError("to many inputs, max 2")
        if len(start_end) == 2:
            start, end = start_end[0], start_end[1]
        elif len(start_end) == 1:
            end = start_end[0]
            start = -end
        else:
            start = -10
            end = 10

        if not (type(length) == int and type(start) == int and type(end) == int and length>0):
            raise TypeError("input has to be int")

        return [ randint(start, end) for _ in range(length) ]

    def fGenFuncs(self, *for_keys):
        d = self.fGenDict()
        rd = self.fReverseDict(d)
        k = self.fGenKeys(*for_keys)
        encrypt = lambda msg: self.fEncryptKeys(msg, d, k)
        decrypt = lambda txt: self.fDecryptKeys(txt, rd, k)
        return encrypt, decrypt

# # # # # # # # # # # #

def test():
    e = Encryptor()

    # Check fGenDict
    d = e.fGenDict()
    # check if every char in dict
    success = True
    for c in Encryptor.chars:
        if not c in d and success:
            print("fGenDict FAILED!")
            success = False
    if success:
        print("fGenDict Success!")

    # Check fReverseDict
    success = True
    rd = e.fReverseDict(d)
    for k, v in rd.items():
        if not d[v] == k and success:
            print("fReverseDict FAILED!")
    if success:
        print("fReverseDict Success!")

    # check key encryption
    msg = "quick brown fox jumped over fence!><P@*ASND *!@ DHA"

    # fGenKeys, nothing to check
    # keys = e.fGenKeys(len(msg)//2, len(msg)//6 + 1)
    keys = [1,2,3]

    # fEncryptKeys and fDecryptKeys
    mk = e.fEncryptKeys(msg, e.default, keys)
    if mk == msg:
        print("fEncryptKeys FAILED!")
    else:
        print("fEncryptKeys Success!")

    mk = e.fDecryptKeys(mk, e.default, keys)
    if mk != msg:
        print("fDecryptKeys FAILED!")
        print(mk, msg)
    else:
        print("fDecryptKeys Success!")
    
    # fEncryptDict and with reversed dict
    success = True
    mk = e.fEncryptDict(msg, d)
    if mk == msg:
        print("fEncryptDict FAILED!")
    else:
        print("fEncryptDict Success!")
    
    mk = e.fEncryptDict(mk, rd)
    if mk != msg:
        print("fEncryptDict in reverse FAILED!")
        print(msg, mk)
    else:
        print("fEncryptDict in reverse Success!")

    # fGenFuncs
    fEnc, fDec = e.fGenFuncs(20)
    mk = fEnc(msg)
    if mk == msg:
        print("fGenFuncs fEnc FAILED!")
    else:
        print("fGenFuncs fEnc Success!")

    mk = fDec(mk)
    if msg != mk:
        print("fGenFuncs fDec FAILED")
    else:
        print("fGenFuncs fDec Success!")

if __name__ == "__main__":
    e = Encryptor()
    ee = exit
    t = test
    en, de = e.fGenFuncs(200, 14)






