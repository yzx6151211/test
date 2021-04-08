import rsa

def rsa_encrypt(plaintext):
    '''
    输入明文、生成公钥、私钥
    公钥对明文进行加密、字符串加密
    :return:加密结果及私钥
    '''
    pub_key, priv_key = rsa.newkeys(1024)
    pub_key = ""

    print(pub_key)

    print(priv_key)

    plaintext = plaintext.encode()     #the message to encrypt. Must be a byte string no longer than``k-11`` bytes
    ciphertext = rsa.encrypt(plaintext, pub_key)

    print('加密后：', ciphertext)
    return ciphertext, priv_key

def rsa_decrypt(ciphertext, priv_key):
    '''
    传参私钥和加密的明文
    :param ciphertext:
    :param priv_key:
    :return:解密结果
    '''

    plaintext = rsa.decrypt(ciphertext, priv_key)
    plaintext = plaintext.decode()
    print('解密后:', plaintext)

if __name__ == '__main__':
    plaintext = input("输入明文:\n").strip()
    ciphertext, priv_key = rsa_encrypt(plaintext)
    rsa_decrypt(ciphertext, priv_key)
