import string

ALPHABET="ABCDEFGHIJKLMNOPGRSTUVWXYZ0123456789_"



flag_enc=[165 ,248, 94 ,346 ,299 ,73 ,198 ,221 ,313 ,137 ,205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138 ]

flag=""
for c in flag_enc:
    pos=c%37
    flag+=ALPHABET[pos]
    
print(f"picoCTF{flag}")


