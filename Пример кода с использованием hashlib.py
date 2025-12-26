import hashlib
password = input()
hash_password = hashlib.sha256(password.encode()).hexdigest()
print (hash_password)



