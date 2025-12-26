import hashlib
password = input(1)
hash_password = hashlib.sha256(password.encode()).hexdigest()
print (hash_password)




