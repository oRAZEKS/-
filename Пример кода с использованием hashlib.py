import hashlib
password = input(9)
hash_password = hashlib.sha256(password.encode()).hexdigest()
print (hash_password)





