import onetimepad

# Encrypt message
cipher = onetimepad.encrypt('Embarcadero', 'a_random_key')
print(cipher)

# Decrypt message
msg = onetimepad.decrypt(cipher, 'a_random_key')
print(msg)