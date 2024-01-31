#!/usr/bin/python3 -u

from pwn import *

enc_flag = bytes.fromhex("0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d");
enc_text= bytes.fromhex("2366101d3922231d3979201d3923751d3971751d3927791d3971713a1d392525");
dec_text= b'A'*32

key = xor(enc_text, dec_text);

print(xor(enc_flag, key).decode());




