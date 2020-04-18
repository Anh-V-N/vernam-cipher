<h1> vernam-cipher </h1>
<h2> Description: </h2>
A python script that encrypt and decrypt Vernam Cipher. In encrypt mode, the script  generates a pair of Cipher (extension .cipher) and One-Time Pad (extension .otp) for the original file. In decrypt mode, the script requires a cipher file and a otp file to recontruct the original file.

<h2>Usage</h2>

To encrypt:
python3 ./vernam.py e file

To decrypt:
python3 ./vernam.py d cipher otp

<h2>Example</h2>
![example](https://raw.githubusercontent.com/Anh-V-N/vernam-cipher/master/example.png)
