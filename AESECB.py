from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import timeit

start = timeit.default_timer()
# Define the plaintext to be encrypted
plaintext = b"Hello,my world!!"

# Generate a random 16-byte key
key = get_random_bytes(16)

# Create an AES cipher object using ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Store the results of each iteration
encryption_results = []
decryption_results = []

# Perform encryption
result = plaintext
for i in range(16):
    result = cipher.encrypt(result)
    encryption_results.append((i + 1, result, key))

# Perform decryption
decrypted_result = result
for i in range(16):
    decrypted_result = cipher.decrypt(decrypted_result)
    decryption_results.append((16 - i, decrypted_result, key))


# Print the results
print("Encryption Results:")
for i, result, used_key in encryption_results:
    print(f"Iteration {i}: {result}, Key: {used_key}")
print("Final Encryption Result:", result.hex())

print("\nDecryption Results:")
for i, result, used_key in decryption_results:
    print(f"Iteration {i}: {result}, Key: {used_key}")
print("Final Decryption Result:", result.decode('utf-8', 'ignore'))

end = timeit.default_timer()
print("during time:",end-start)