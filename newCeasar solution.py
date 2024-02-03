import string


LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def index(char):
   ALPHABET = string.ascii_lowercase[:16]
   for i in range(len(ALPHABET)):
     if ALPHABET[i]== char :
      return i   
   return -1 #character not found

def b16_decode(enc):
    decoded_flag=""
    for i in range(0,len(enc),2): 
        #we skip every two characters because the original encryption
        #takes a character, turns it into an 8 bit binary
        # then turns each four bits into their correspanding character in the alphabet
     binary= "{0:04b}".format(index(enc[i]))+"{0:04b}".format(index(enc[i+1]) )
     decoded_flag+=chr(int(binary,2))
    return decoded_flag


def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]



enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"  #replace with your version of the challenge
for key in ALPHABET: 
    flag=""
    print("key",key)
    for c in enc:
        flag+=shift(c,key)
    
    print("flag : ",b16_decode(flag))
    
    #flag found for key O


