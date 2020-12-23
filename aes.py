# import
#from Crypto.Cipher import AES
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os, struct, random

def encrypt_file(key, filename):

    chunk_size = 64*1024
    BS = 16

    output_filename = filename + '.encrypted'

    # iv값 정하기
    iv = os.urandom(16)

    # AES암호화 블록 생성
    encryptor = AES.new(key,AES.MODE_CBC,iv)

    # 원래의 파일 사이즈 구하기
    filesize = os.path.getsize(filename)

    # 암호화할 파일과 암호화후 저장할 파일 열기
    with open(filename, 'rb') as inputfile:
        with open(output_filename, 'wb') as outputfile:

            # 파일사이즈와 IV값 적어놓기
            outputfile.write(struct.pack('<Q',filesize))
            outputfile.write(iv)


            # 암호화할 파일 읽어오기
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                # 16byte(128bit)로 나눠지지 않을 경우 패딩추가
                elif len(chunk) % 16 != 0:
                   # PKCS#5 PADDING  BS -len(chunk) % BS 는 INT 기때문에 문자로 바꾼뒤 바이트 단위로 환산 후 곱해서 패딩을 해줌
                    chunk += str((BS - len(chunk) % BS)).encode('utf-8') * (BS - len(chunk) % BS)

                    outputfile.write(encryptor.encrypt(chunk))

# 파일명 입력받기
file_name = input("What is file name to Encryption ? \n")

# 패스워드 설정

password_input = input("input password. : \n")
password = password_input.encode('utf-8')
#password = "password".encode('utf-8')



# SHA256을 통한 키값에 따른 해시값 구하기

def makeKey(password) :
    hasher = SHA256.new(password)
    return hasher.digest()


encrypt_file(makeKey(password),file_name)

print("complete!")
