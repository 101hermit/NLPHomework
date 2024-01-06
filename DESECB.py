# 导入必要的库
from Crypto.Cipher import DES
import binascii
import timeit
start = timeit.default_timer()

# 设置密钥
key = b'abcdefgh'  # 8字节长度的密钥

# 显示密钥
print("原始密钥:", key)

# 显示ECB加密模式
cipher = DES.new(key, DES.MODE_ECB)

# 显示16次迭代加密的密钥与加密结果
for i in range(16):
    encrypted = cipher.encrypt(key)
    print("第{}次迭代加密密钥:".format(i+1), key, " 加密结果:", binascii.hexlify(encrypted))
    key = encrypted  # 将上一轮加密结果作为下一轮的密钥

# 重置密钥
key = b'abcdefgh'  # 8字节长度的密钥

# 显示16次迭代解密的密钥与解密结果
for i in range(16):
    decrypted = cipher.decrypt(key)
    print("第{}次迭代解密密钥:".format(i+1), key, " 解密结果:", decrypted)
    key = decrypted  # 将上一轮解密结果作为下一轮的密钥

# 加密
text = b'Hello,my world!!'
encrypted_text = cipher.encrypt(text)
print("最终加密结果:", binascii.hexlify(encrypted_text))

# 解密
decrypted_text = cipher.decrypt(encrypted_text)
print("最终解密结果:", decrypted_text)

end = timeit.default_timer()
print("during time:",end-start)
