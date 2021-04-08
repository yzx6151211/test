from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64

# 私钥
private_key ="-----BEGIN PRIVATE KEY-----"+"\n"+"MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBALh2/VLmHCgNL8nC"+"\n"+"mKACNmXchU4eBSxi8b8qo9ciU7hcARKZA/bMedUl15l4LQMtsNrDQXagqJrv73zs"+"\n"+"ul7Pr0JHE+3gqdeIWlFVuLSWV5DyqylBIDEx94RcBerKn6ibf+ESPf5UIfokT/oG"+"\n"+"pY5GBK7Ca2HnPUkHmmobY4LTdROBAgMBAAECgYAAjqt5QqS3IkMQsvvPD/KmICJu"+"\n"+"9/xABBSC5VgVYE8scWq3aarvZfLASBr8pbZNGig8oPZjq1yXCz6H/BccDjiTU1z1"+"\n"+"Oeyr/V5HOpEYqZHTHg+7SeR7j2f6THSqmPw8cPb//4WnXol1IbXJGrS7Yf1Me/TM"+"\n"+"Q2xFx22DW8DnG2Z2+QJBAPW5ikvlN1X5qby3+2uXFhXGktbrKlH3DtMJnbhjCvcO"+"\n"+"NMYc+crP6R+/85guALHI34TzlBoGNw7dYitczy5vVKMCQQDALarYIdPcsqFVWaOe"+"\n"+"fFv601OrJjgmatxotR754tomdZmFd8jQp9QIjGLjCtUM40cnH5nMha2CtEHGUJQ4"+"\n"+"+FWLAkAKZahhX7iArcit0IcV3VW05CsQZvDqeO6qpUyEIcS0AWjgPRegqj1t93xC"+"\n"+"IygqXZp/kKLimwK3YUynEw09JL7LAkAdheZ9FZVKjlaimga8zjYDLnvoCxMNM9Vw"+"\n"+"cIK1uNfymJZhHqnHBEFantaCMqPQOwovRHeIJ/Ej5zVDlhVvOxdJAkEAuryz0AM0"+"\n"+"Rru4Ur9PePykQ4bBvPx3KI3hYpVmi/eiK2zl98I8c1+RSso+3poRt6oiUgNcDAzC"+"\n"+"yFrTuGoxw0O50w=="+"\n"+"-----END PRIVATE KEY-----"



'''-----BEGIN RSA PRIVATE KEY-----
5353dfggd
-----END RSA PRIVATE KEY-----
'''

# 公钥
public_key = "hfgghftetet" '''-----BEGIN PUBLIC KEY-----
hfgghftetet
-----END PUBLIC KEY-----'''


def rsa_encrypt(message):
    """校验RSA加密 使用公钥进行加密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(public_key))
    cipher_text = base64.b64encode(cipher.encrypt(message.encode())).decode()
    return cipher_text


def rsa_decrypt(text):
    """校验RSA加密 使用私钥进行解密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(private_key))
    retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
    return retval
if __name__ == '__main__':
    a ="fPzjBmx0e3j4+5NwGZO2gr4PODGdfpsMNBD0ErAe/+PWrHcIAZ3I/FkUyXV3HVRlDba93BwCh/TADtEkMREl3OwtM7xnhb7V7g73xaC+XNR12tVvb+aRHwejgTPh24jeoOW/zk8eMYvNmYMXSwYOeKwpIJkodTNrirdV5DHxWJM="
    rsa_decrypts =  rsa_decrypt(a)
    print(rsa_decrypts)