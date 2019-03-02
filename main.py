import sys
import nacl.secret
import nacl.utils
import time
import base64


def create_box():
    try:
        key_ = open('KEY', 'r')
        key = base64.b64decode(key_.read().encode('utf8'))
    except:
        print('Key not found')
        key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
        with open('KEY', 'w') as keyfile:
            keyfile.write(base64.b64encode(key).decode('utf8'))

    print('key', base64.b64encode(key).decode('utf8'))

    return nacl.secret.SecretBox(key)


@profile
def encrypt(f, j):
    box = create_box()
    f = open(f, 'r', encoding='ISO-8859-1')
    encoded = f.read().encode('ISO-8859-1')
    out = box.encrypt(encoded)
    j = open(j, 'w')
    to_write = base64.b64encode(out).decode('utf8')
    j.write(to_write)


@profile
def decrypt(f, j):
    box = create_box()
    f = open(f, 'r', encoding='utf8')
    decoded = base64.b64decode(f.read())
    out = box.decrypt(decoded)
    j = open(j, 'w', encoding="ISO-8859-1")
    to_write = out
    j.write(to_write.decode('ISO-8859-1'))


{'decrypt': decrypt, 'encrypt': encrypt}[sys.argv[1]](sys.argv[2], sys.argv[3])
