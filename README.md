# pyTextEncryption
Simple amature slow encryption. Statefull (perhaps safer) and stateless version. Shared map and list of 'keys/steps'.
Use it only if you have nothing better on your hands. <br>
I supose there is allready such an algorithm, if you are aware of what it is please tell me and I will edit it in this README. <br>
<br>
Slow, 11100 characters on avarage, version 2:
 - encrypted in 0.0057235 sec. <br>
 - decrypted in 0.0064435 sec. <br>

### Generic explenation how it works.
First a simple map is created: `{'a':'n', 'b':'\n', 'c':')' ... 'Z':'0' }` and a list of 'keys': `[-13, 50, 21, 43, -98 ... ]`, which are vectors by which the map will be moved before typing every letter. Keys are a list of one dimenison vectors.<br>
<br>
For an easy example, I will take map from above, `keys = [1, -22, 34]` and try to encrypt `'b'`. <br>
This is what will happen: <br>
```
m = {'a':'n', 'b':'\n', 'c':')' ... 'Z':'0' }
keys = [1, -22, 34]
msg = 'b'

# First thing is moving the map by the vector.
m = {'a':'0', 'b':'n', 'c':'\n' ... 'Z':'u' }
# look, everything in map moved one place to right and the last key of map moved to beggining.

# Second step is to get the value of 'b'.
m['b']  # '\n'
```
I hope it is quite understandable, decryption is just the oposite. <br>
For two parties to communicate they must have same map and keys.
<br>

### How Statefull works.
There was an issue I wanted to get rid of which was that encrypting the same message allways ended with the same text. <br>
Now Statefull (`EncryptorSt`) works by taking in account how many letters were sent before, this way the same message will result in the same text is by chance. <br>
The more technical explanation is the map doesn't reset when sending a new message, as to the opposite of stateless (`Encryptor`). <br>
<br>

### Version 2
First version was slow and solution to this problem was by not editing the map after every letter but to make a map char->int, int->char. This way it is possible to just add the vectors to a single variable and save it. <br>



