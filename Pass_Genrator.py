import random

import string

pass_len=8
values=string.ascii_letters+string.digits+string.punctuation


password=""
for i in range(pass_len):
    password+=random.choice(values)
    
    
print("your random password is : ",password)
    