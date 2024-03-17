from random import randint

c = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"

def to_identity_map(a):
    return ord(a) - 0x41


def from_identity_map(a):
    return chr(a % 26 + 0x41)


def decrypt(c):
    m = ''
    for i in range(len(c)):
        ch = c[i]
        if not ch.isalpha():
            mch = ch
        else:
            chi = to_identity_map(ch)
            mch = from_identity_map(chi - i)
        m += mch
    return m

print(f"HTB{{{decrypt(c)}}}")
