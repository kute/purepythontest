#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/10 08:35'

"""

"""

import rsa


def main():
    #  e80861b179c3f6f57fb34d03f74363e525292c68288a30d6c90f1cdd454cb5a1d0f1f4ebee196fc7b34b100ef83a0e4bc6de177cec
    # e19a66d602189ba6209b42eef20b393453a97b8500a0d396b672d999e75277116c00fb88e12578f388763ed972547b2080d58b92805c
    #6bdef45bfe99d4a65f0fc952096dae8285edf94315
    servertime = 1473468000
    nonce = "S7Q2Z3"
    password = "bailong1"
    pubkey = "EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443"
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)#create public key
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)#create clear text
    passwd = rsa.encrypt(bytes(message, encoding="utf-8"), key)#cipher text

    passwd = passwd.decode()
    # passwd = binascii.b2a_hex(passwd)#convert the cipher text into hexadecimal
    passwd = int(str(passwd), 16)
    print(passwd)


if __name__ == '__main__':
    main()
