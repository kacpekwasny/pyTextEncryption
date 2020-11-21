from timeit import default_timer as time
from encryptor import Encryptor
from encryptor_statefull import EncryptorSt

def fTestEncSt():
    print("fTestEncSt")
    e = EncryptorSt(23, 17)

    # Check fGenDict
    d = e.fGenDict()
    # check if every char in dict
    success = True
    for c in EncryptorSt.chars:
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

    # test fEnc fDec
    e1, e2 = EncryptorSt.fMakePair(23, 17)
    msg = "Quick brown fox jumped over the lazy dog!"
    mk1 = e1.fEnc(msg)
    if mk1 == msg:
        print("fEnc t1 FAILED!")
    else:
        print("fEnc t1 Success!")

    mk1dec = e2.fDec(mk1)
    if mk1dec != msg:
        print("fEnc&fDec t1 FAILED!")
    else:
        print("fEnc&fDec t1 Success!")

    mk2 = e1.fEnc(msg)
    if mk2 == msg:
        print("fEnc t2 FAILED!")
    else:
        print("fEnc t2 Success!")

    mk2dec = e2.fDec(mk2)
    if mk2dec != msg:
        print("fEnc&fDec t2 FAILED!")
    else:
        print("fEnc&fDec t2 Success!")

    if mk1 == mk2:
        print("fEnc&fDec t3 rotation FAILED!")
    else:
        print("fEnc&fDec t3 rotation Success!")

    msg = 5 * EncryptorSt.string
    print("msg:", msg)
    for i in range(10):
        s = time()
        mk3 = e1.fDec(e2.fEnc(msg))
        e = time()
        print("Enc and Dec time =", e - s, "FAILED" if mk3 != msg else "Sueccess")

def fTestEnc():
    print("fTestEnc")
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

def fTimeExec(func):
    s = time()
    func()
    print("Exec", func, "in:", time() - s)

if __name__ == "__main__":
    fTestEnc()
    fTestEncSt()
