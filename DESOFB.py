from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import timeit
start = timeit.default_timer()
# Define the plaintext to be encrypted
plaintext = b"Hello,my world!!"

# Generate a random 8-byte initialization vector (IV)
iv = get_random_bytes(8)

# Define the key for encryption and decryption
key = b"12345678"  # Replace with your own 8-byte key

# Create a DES cipher object using OFB mode
cipher = DES.new(key, DES.MODE_OFB, iv=iv)

# Store the results of each iteration
encryption_results = []
decryption_results = []

# Perform 16 iterations of encryption and store the results
previous_result = plaintext
for i in range(16):
    result = cipher.encrypt(previous_result)
    encryption_results.append((i+1, result, key))
    previous_result = result

# Perform 16 iterations of decryption and store the results
cipher = DES.new(key, DES.MODE_OFB, iv=iv)  # Reset the cipher for decryption
previous_result = result  # Use the result from the last encryption as the input for decryption
for i in range(16):
    result = cipher.decrypt(previous_result)
    decryption_results.append((16-i, result, key))
    previous_result = result

# Print the results
print("Encryption Results:")
for i, result, used_key in encryption_results:
    print(f"Iteration {i}: {result}, Key: {used_key}")
print("Final Encryption Result:", result.hex())

print("\nDecryption Results:")
for i, result, used_key in decryption_results:
    print(f"Iteration {i}: {result}, Key: {used_key}")
print("Final Decryption Result:", result.decode('utf-8'))

end = timeit.default_timer()
print("during time:",end-start)
