import openai
import json
import os

openai.api_key = "sk-f2F2ajsxkrwppRLn752AVAgU18cAGNS56ayfhQm3l4qIlWXY"
openai.api_base = "https://api.f2gpt.com/v1"

plaintext = "Hello,my world!!"
key = "12345678"

# initial prompt
# prompt = """try to use following methods and demands to encrypt and decrypt the text ```{}``` and use the key: ```{}```\
# (1) methods:DES algorithm with ECB mode,DES algorithm with CBC mode,DES algorithm with OFB mode,DES algorithm with CFB mode,AES algorithm with ECB mode\
# (2) essential demand: execute the whole process of encryption and decryption with these 5 methods\
# (3) what data should we log: output the minimum storage that each method needs,running time of each methods(1 round including encryption and decryption),\
# the actual maximum length about the information string in the whole process(or the maximum temporary memory that alogrithms need),and output the three results of each method.\
# (4) output:the result of encryption and decryption in each method,the constant data(like S-Box,IP table of DES) used in the process,\
# the three results that evaluates these algorithms (#mentioned in '(3)'),other formation which can used to evaluate each method\
# (5) the format of output should be designed as a JSON format\
# complete the data in this model and please output the content of constant data(S-Box etc.,show them with matrix or other 2-dimension format) after the JSON "Table" independently\
# (6) achieve these work in at least 10 minutes,check the output and give me a relatively reasonable data "table" with JSON format\
# tips 1:don't use identifiers to express the output results\
# """.format(plaintext,key)

# evaluation
# prompt_evaluation = """try to use following methods and demands to execute the process of encrypt and decrypt the text ```{}``` and use the key: ```{}```\
# (1) methods:DES algorithm with ECB mode,DES algorithm with CBC mode,DES algorithm with OFB mode,DES algorithm with CFB mode\
# (2) essential demand: execute the whole process of encryption and decryption with these 4 methods\
# (3) what data should we log: maximum and minimum storage the method actually uses,the parameters which can evaluate the security,the parameters of runtime and the result to express error rate\
# (4) output:the result of encryption and decryption in each method\
# the three results that evaluates these algorithms (#mentioned in '(3)')\
# (5) the format of output should be designed as a JSON format\
# complete the data in this model and please give some other formulations to evaluate these methods\
# (6) achieve these work in at least 10 minutes,check the output and give me a relatively reasonable data "table" with JSON format\
# tips 1:don't use identifiers to express the output results\
# tips 2:all of the terms should give accurate value\
# tips 3:don't give me the code,give me the answers\
# """.format(plaintext,key)


# upgrades
# prompt = """try to use following methods and demands to encrypt and decrypt the text ```{}``` and use the key: ```{}```\
# #tips 2:change the RowShift function in AES(e.g. Row i:shift left by i*2 position),achieve in the AES process and show the encryption,decryption result with change\
# tips 1:don't use identifiers to express the output results\
# tips 3:change the XOR to AND in ```F``` function,give the encrypting results\
# tips 4:don't give me the code,give me results\
# (1) methods:DES algorithm with ECB mode\
# (2) essential demand: execute the whole process of encryption and decryption\
# (4) output:the result of encryption and decryption in the method\
# (5) the format of output should be designed as a JSON format\
# complete the data according to this model and give the instructions of Rowshifts function in AES\
# (6) achieve these work in at least 10 minutes,check the output and give me a relatively reasonable data "table" with JSON format\
# """.format(plaintext,key)

# # context
# prompt = """
# Your task is to simulate a scene:you should achieve a communication with encryption and decryption with AES with ECB mode\
# you should give:(```output them in JSON format```)
# (1)the plaintext,ciphertext,decoded ciphertext,and check the correction with some parameters
# (2)some parameters to evaluate the runtime,security,memory and storage,error rate,praticability,meaning and value
# (3)do something to upgrade the encryption and decryption and show the effect
# (4)give a grade to summarize the value of the algorithm(0 is lowest and 1 is highest,between 0 and 1)
# (5)give more constructive advice to this encrypting background
# you can have a long time to think and check the answers
# """

#few-shot
prompt = """
give me some application fields(at least 3 examples) of DES encrypting algorithm and show me the following message:
(1)application and short introduction
(2)some theory and formulation which generates or upgrades from the combination of DES and this field
(3)where can i find related project about this combination(DES and this field),give me url or other key information
label 1:please give me some formulations,norm and mathmetic theory of DES on these application(e.g. the usage of DES in SSL/TLS protocol)
"""

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": prompt}],
    temperature = 0
)

print(completion.choices[0].message["content"])
