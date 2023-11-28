import hashlib
password = "1"
passhash = hashlib.sha256(password.encode()).hexdigest()
print(passhash)