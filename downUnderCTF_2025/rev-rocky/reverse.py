import hashlib
import itertools
import string

target = "d2f969f60c4d92701f35021256bdca3c"
charset = string.ascii_letters + string.digits

for l in range(6, 17):
    for cand in itertools.product(charset, repeat=l):
        s = ''.join(cand)
        h = hashlib.md5(s.encode()).hexdigest()
        print(f"({l}) {s}, {h}")
        if h == target:
            print(f"[+] Found: {s}")
            exit()