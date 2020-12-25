from encryptor_st import EncryptorSt
from time import time

def fTestEncryptorSt(mssg):
    e1, e2 = EncryptorSt.fMakePair()
    
    txt = e1.fEnc(mssg)
    msg = e2.fDec(txt)
    if msg == mssg:
        print("Success first crypto.")
        # print("    Encrypted:", repr(txt))
        print("\n")
    else:
        print("Failed first crypto.")
        print("    Encrypted:", repr(txt))
        print("    Decrypted:", msg)
        print("\n")

    txt = e2.fEnc(mssg)
    msg = e1.fDec(txt)
    if msg == mssg:
        print("Success second crypto.")
        # print("    Encrypted:", repr(txt))
        print("\n")
    else:
        print("Failed second crypto.")
        print("    Encrypted:", repr(txt))
        print("    Decrypted:", msg)
        print("\n")

def fTestEncryptorStTime(reps, msg):
    e1, e2 = EncryptorSt.fMakePair()

    sumt1 = 0
    sumt2 = 0

    for _ in range(reps):
        enc_msg, t1 = fTimeIt(lambda: e1.fEnc(msg) )
        dec_msg, t2 = fTimeIt(lambda: e2.fDec(enc_msg))
        sumt1 += t1
        sumt2 += t2
        if msg != dec_msg:
            print("Failed!", "\nmsg:", msg, "\ndec_msg", dec_msg)

    print(sumt1/reps)
    print(sumt2/reps)

def fTimeIt(fFunc):
    start = time()
    ret = fFunc()
    return ret, time()-start


if __name__ == "__main__":
    from sys import argv
    msg = " ".join(argv[2:])
    msg = msg if len(msg) else "The Quick Brown fox jumped over a lazy dog. See what I did there?. Nothing actually. Although it is a panagram." * 100
    print("len(msg):", len(msg))
    fTestEncryptorSt( msg )
    print("\nTime of single encryption and decryption and then whole test time:")
    print(fTimeIt( lambda:
        fTestEncryptorStTime( int(argv[1] if len(argv)>1 else 100), msg)
    )[1])




