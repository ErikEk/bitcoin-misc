import bitcoinlib
import hashlib
import base58
import codecs
import ecdsa

#privKey1, pubKey1 = generate_key_pair(sha256(b'key0'))
#privKey2, pubKey2 = generate_key_pair(sha256(b'key1'))
#privKey3, pubKey3 = generate_key_pair(sha256(b'key2'))

from bitcoinlib.wallets import Wallet
w = Wallet.create('Wallet1')
w.get_key().address