from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from datetime import datetime
import base64
import qrcode


def generate_qrcode(data):
    content = ''
    for key in data.keys():
        content += data[key]
        
    qr = qrcode.QRCode(version=1, box_size=10)
    qr.add_data(content)
    
    filename = 'tempqrcode.png'
    img = qr.make_image()
    img.save('qrcodereader/static/images/' + filename)
    
    return filename


def base64Encoding(input):
  dataBase64 = base64.b64encode(input)
  dataBase64P = dataBase64.decode("UTF-8")
  return dataBase64P


def base64Decoding(input):
    return base64.decodebytes(input.encode("ascii"))


def encrypt_content(message, key):
    keyBytes = key.encode('ascii')
    salt = get_random_bytes(32)
    encryptionKey = PBKDF2(keyBytes, salt, 32, count=15000, hmac_hash_module=SHA256)
    cipher = AES.new(encryptionKey, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('ascii'), AES.block_size))
    ivBase64 = base64Encoding(cipher.iv)
    saltBase64 = base64Encoding(salt)
    ciphertextBase64 = base64Encoding(ciphertext)
    return saltBase64 + ":" + ivBase64 + ":" + ciphertextBase64


def decrypt_content(message, key):
    keyBytes = key.encode('ascii')
    data = message.split(':')
    salt = base64Decoding(data[0])
    iv = base64Decoding(data[1])
    ciphertext = base64Decoding(data[2])
    decryptionKey = PBKDF2(keyBytes, salt, 32, 15000, hmac_hash_module=SHA256)
    cipher = AES.new(decryptionKey, AES.MODE_CBC, iv)
    decryptedText = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decryptedTextP = decryptedText.decode('UTF-8')
    return decryptedTextP


def format_datetime(input):
    input_formatted_str = input.strftime("%d-%m-%y %H:%M:%S")
    return datetime.strptime(input_formatted_str, "%d-%m-%y %H:%M:%S")


def timecount(input):
    input = input.replace(' ', '')
    result = 0
    if input.find('day') != -1:
        input = input.replace('days', '').replace('day', '')
        days, hours = input.split(',')
        result += int(days) * 24*60*60
        input = hours
    
    hour, min, sec = input.split(':')
    result += int(hour)*60*60 + int(min)*60 + int(sec)
    return result