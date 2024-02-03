### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('C:/Users/Administrator/Desktop/Pico/pw crack1/level1.flag.txt.enc', 'rb').read() #put the file and script in the same folder



def level_1_pw_check():
    
    decryption = str_xor(flag_enc.decode(), "1e1a")
    
    return decryption



print(level_1_pw_check()) #should print out the flag
