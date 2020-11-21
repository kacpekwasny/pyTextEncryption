# pyTextEncryption
### Simple not performance oriented encryption statefull (perhaps safer) and stateless version. <br>
<br>

<p>Encryptor:</p>

```
from encryptor import Encryptor

# These args control how random are letter map changes
fEncrypt, fDecrypt = Encryptor().fGenFuncs(37, 21)

msg = "Quick brown fox jumped over the lazy dog!"

men = fEncrypt(msg)
print("1. ENCRYPTED\n", men)
print("1. DECRYPTED\n", fDecrypt(men))

print("\n # # # # # # # # # # # \n")

print("2. ENCRYPTED 'My message'\n", fEncrypt("My message"))
men = fEncrypt("Another message")
print("3. ENCRYPTED 'Another message'\n", men,"\n", "3. DECRYPTED\n",  fDecrypt(men))
```
Out:
```
1. ENCRYPTED
 .%7<"`1`#&@^!B5D$~rW
v)%?LR(X"bp          "@n N$k{
1. DECRYPTED
 Quick brown fox jumped over the lazy dog!

 # # # # # # # # # # # 

2. ENCRYPTED 'My message'
 VKowY8N_&V
3. ENCRYPTED 'Another message'
 +En0XT?v|V|}B^/ 
 3. DECRYPTED
 Another message
```
<br>
<p> EncryptorSt: </p>

```
from encryptor_statefull import EncryptorSt

# One has to decrypt every message in order to stay synced,
# there is also possibility to manualy sync EncryptorSt.vector
# nontheless these have to be same value for coders to work
# Every encryption is different

msg = "Quick brown fox jumped over the lazy dog!"

# this will work
e1, e2 = EncryptorSt.fMakePair(1213, 35)
m = e1.fEnc(msg)
print("1. ENCRYPTED\n", m)
print("1. DECRYPTED\n", e2.fDec(m))

# but watch what happens when one leaves one message not decoded
print("2. ENCRYPTED BUT FORGOT\n", e1.fEnc(msg))  # this message will be printed and forgot,
    # so it wont be decoded thus, e1 and e2 are out of sync.

men = e1.fEnc(msg)  # this message will be decrypted incorrectly by e2 because they are auto of sync.
print("2. ENCRYPTED BUT OUT OF SYNC\n", men)
print("2. DECRYPTED BUT OUT OF SYNC\n", e2.fDec(men)) # wrong decryption
print("2. DECRYPTED BY ACCIDENT GETTING IN SYNC\n", e2.fDec(men)) # correct decryption, we are luck because two messages with same number of letters were sent
    # and e1 and e2 by accident got synchronized again!

print("3. PRESENTATION, statefull encryption encrypts different every time.")

print( m1 := e1.fEnc(msg))
print(" # # # # # # ")
print( m2 := e1.fEnc(msg))

print("\n~~~~~~~~~~~~\n")

print(e2.fDec(m1))
print(e2.fDec(m2))
print("\n First m2 and then m1 wouldnt work, also avoiding anyone of these wouldnt give desired output.")
```
Out:
```
1. ENCRYPTED
 57jQ5'`4hu"C3r|x1ejxj?SOKuH<#`_]dLgl
??|s
1. DECRYPTED
 Quick brown fox jumped over the lazy dog!
2. ENCRYPTED BUT FORGOT
;*S@w%
      +,u5"3u3}_Al@r~a;.h]O7-9}},/
2. ENCRYPTED BUT OUT OF SYNC
 \C
   8\Xb1_0mp:!4@[w
                  @
                    .   -0+z`bZShAt?K  4(
2. DECRYPTED BUT OUT OF SYNC
."V$DU+(:'DY(;D#.&)XWD(/X+D-!XD%T=<DW(Z7
2. DECRYPTED BY ACCIDENT GETTING IN SYNC
 Quick brown fox jumped over the lazy dog!
3. PRESENTATION, encryption gives out different output.
f%:
   f)U5.Q>6^V*0\m:0:$Z|?Q!N;UW_S        C}l$$*y
 # # # # # # 
vp^RvPL[Z{B2Di1Qf>^Q^EW,}{VIbL&._|% -EE1M

~~~~~~~~~~~~

Quick brown fox jumped over the lazy dog!
Quick brown fox jumped over the lazy dog!

 First m2 and then m1 wouldnt work, also avoiding anyone of these wouldnt give desired output.
```



