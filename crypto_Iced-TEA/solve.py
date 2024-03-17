from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b
from enum import Enum


class Mode(Enum):
    ECB = 0x01
    CBC = 0x02


class Cipher:
    def __init__(self, key, iv=None):
        self.BLOCK_SIZE = 64
        self.KEY = [b2l(key[i:i+self.BLOCK_SIZE//16]) for i in range(0, len(key), self.BLOCK_SIZE//16)]
        self.DELTA = 0x9e3779b9
        self.IV = iv
        if self.IV:
            self.mode = Mode.CBC
        else:
            self.mode = Mode.ECB

    def _xor(self, a, b):
        return b''.join(bytes([_a ^ _b]) for _a, _b in zip(a, b))

    def decrypt(self, ct):
        blocks = [ct[i:i+self.BLOCK_SIZE//8] for i in range(0, len(ct), self.BLOCK_SIZE//8)]

        msg = b''
        if self.mode == Mode.ECB:
            for block in blocks:
                msg += self.decrypt_block(block)
        elif self.mode == Mode.CBC:
            X = self.IV
            for block in blocks:
                dec_block = self.decrypt_block(block)
                msg += self._xor(X, dec_block)
                X = block
        return msg

    def decrypt_block(self, ct):
        m = b2l(ct)
        m0 = m >> (self.BLOCK_SIZE//2)
        m1 = m & ((1 << (self.BLOCK_SIZE//2)) - 1)
        K = self.KEY
        msk = (1 << (self.BLOCK_SIZE//2)) - 1

        s = self.DELTA << 5
        for i in range(32):
            m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
            m1 &= msk
            m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
            m0 &= msk
            s -= self.DELTA

        m = ((m0 << (self.BLOCK_SIZE//2)) + m1) & ((1 << self.BLOCK_SIZE) - 1)

        return l2b(m)


if __name__ == '__main__':
    KEY = bytes.fromhex('850c1413787c389e0b34437a6828a1b2')
    cipher = Cipher(KEY)
    ct = bytes.fromhex('b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843')
    msg = cipher.decrypt(ct)
    print(msg)
