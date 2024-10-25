import random, sys

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&-_()=?'
password = ''
length = 32 if len(sys.argv) == 1 else int(sys.argv[1])

for a in range(1,length,1):    
    password += random.choice(letters)

print(password)
exit()
