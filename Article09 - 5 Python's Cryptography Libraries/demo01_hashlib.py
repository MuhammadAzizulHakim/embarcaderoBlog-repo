import hashlib
 
m = hashlib.sha256()
m.update(b"Hello")
m.update(b" World!")
 
print(m.digest())
print(m.digest_size)
print(m.block_size)
 
print(hashlib.sha256(b"Hello World!").hexdigest())
# More condensed example:
print(hashlib.sha224(b"Hello World!").hexdigest())
 
# Using new() with an algorithm provided by OpenSSL:
h = hashlib.new('ripemd160')
h.update(b"Nobody inspects the spammish repetition")
print(h.hexdigest())