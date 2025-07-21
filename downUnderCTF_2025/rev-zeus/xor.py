import struct

# 암호화된 64비트 정수들
data = [
    0x0C1F1027392A3409,
    0x011512515C6C561D,
    0x5A411E1C18043E08,
    0x3412090606125952,
    0x12535C546E170B15,
    0x003A110315320F0E,
]

# 바이트 배열로 변환
cipher_bytes = bytearray()
for qword in data:
    cipher_bytes += struct.pack("<Q", qword)

# v11의 마지막 4바이트는 *(char *)v11 + 7부터 DWORD로 대입됨 (1313495552 == 0x4E505445)
tail_dword = 0x4E505445
cipher_bytes[47:51] = struct.pack("<I", tail_dword)  # offset 47부터 4바이트를 덮어씀

# XOR 키
key = b"Maimaktes1337"
key_len = len(key)

# XOR 복호화
plaintext = bytearray()
for i in range(len(cipher_bytes)):
    plaintext.append(cipher_bytes[i] ^ key[i % key_len])

print("decoded:", plaintext.decode(errors="ignore"))