#!/usr/bin/env python3

import sys,random,string,os

HELP = '''Usage:

To encrypt:
python3 %s e file

To decrypt:
python3 %s d cipher otp

'''%(sys.argv[0],sys.argv[0])


def xor(int1, int2):
    return int1^int2
    

def otp_generate(pl_dec):
    length = len(bin(pl_dec))
    values = ('0','1')
    otp = None
    while otp == None:
        try:
            # Generate random binary string    
            otp_bin = ''.join(random.choice(values) for i in range(length))
            # Convert to int format to execute XOR
            otp_dec = int(otp_bin,2)
            # Convert to bytes
            otp = otp_dec.to_bytes(size,'big')
        except:
            pass 
    print('[+] OTP generated ')
    return otp_dec, otp



def encrypt(pl,size):
    '''
    pl is bytes stream
    size == size of the plaintext file in bytes
    encrypting function
    return cipher and otp in bytes stream
    '''
    print('[+] Encrypting in progress...')
    pl_dec = int.from_bytes(pl,byteorder='big') # parse the bytes to decimal representative  
    otp_dec, otp = otp_generate(pl_dec)
    cipher_dec = xor(pl_dec,otp_dec)
    cipher = cipher_dec.to_bytes(size,'big')
    print('[+] Finished encrypting!')
    return cipher,otp


def decrypt(cipher,otp):
    print('[+] Decrypting in progress.. ')
    cipher_dec = int.from_bytes(cipher,byteorder='big')
    otp_dec = int.from_bytes(otp,byteorder='big')
    pl_dec = xor(cipher_dec,otp_dec)
    pl = pl_dec.to_bytes(size,'big')
    print('[+] Finished decrypting.')
    return pl


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'e' and len(sys.argv) == 3:       
            pl_file = sys.argv[2]
            size = os.path.getsize(pl_file)
            with open(pl_file,'rb') as f:
                pl = f.read()
                e = encrypt(pl,size)
                with open(pl_file + '.cipher','wb') as c:
                    c.write(e[0])
                with open(pl_file + '.otp','wb') as o:
                    o.write(e[1])
        elif sys.argv[1] == 'd' and len(sys.argv) ==4:
            with open(sys.argv[2],'rb') as c:
                c = c.read()
                size = os.path.getsize(sys.argv[2])
                with open(sys.argv[3],'rb') as o:
                    o = o.read()
                    with open('decrypted','wb') as pl:
                        pl.write(decrypt(c,o))
        else:
            print(HELP)
    except:
        print(HELP)

# Debug area

# a = 23534**434342 # Tried various random values
# b = otp_generate(a)
# x = xor(b,a)
# d = xor(x,b)
# # print('origin value:',a)
# # print('otp value   :',b)
# # print('cipher value:',x)
# # print('decrypted   :',d)
# if a == d:
#     print('Value unchanged')
