import hashlib
import itertools
import string

target = "d2f969f60c4d92701f35021256bdca3c"
charset = string.ascii_letters + string.digits

for l in range(5, 17):
    for p in itertools.product(charset, repeat=l):
        s = ''.join(p)
        print(s)
        if hashlib.md5(s.encode()).hexdigest() == target:
            print(f"[+] Found: {s}")
            break