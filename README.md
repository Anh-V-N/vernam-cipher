

# Description

A python script that encrypt and decrypt Vernam Cipher. In encrypt mode, the script  generates a pair of Cipher (extension .cipher) and One-Time Pad (extension .otp) for the original file. In decrypt mode, the script requires a cipher file and a otp file to recontruct the original file.

# Usage

To encrypt:
python3 ./vernam.py e file

To decrypt:
python3 ./vernam.py d cipher otp

# Example
![example](https://raw.githubusercontent.com/Anh-V-N/vernam-cipher/master/example.png)
