
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

alpha = [chr(x) for x in range(97, 123)]
dict_decode = {}
j = 0
key = key.replace(" ", "")

for i in key:
    if i not in dict_decode.keys() :
        dict_decode[i] = alpha[j]
        j += 1

decode_msg = ""

for k in range(len(message)):
    if message[k] != " ":
        decode_msg += dict_decode.get(message[k])
    else:
        decode_msg += " "

print(decode_msg)