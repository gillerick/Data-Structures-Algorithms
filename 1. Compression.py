# def compressedString(message):
#
#     R = []
#     for i in message:
#         counter = message.index(i)
#         try:
#             while i == message[counter + 1]:
#                 counter += 1
#                 R.append(i+str(counter))
#             # counter = 1
#             if i != message[counter]:
#                 R.append(i)
#         except IndexError:
#             pass
#     print(R)
#
#
# compressedString("Abaaac")

def compress(string):
    temp = {}
    result = ""
    for x in string:
        if x in temp:
            temp[x] = temp[x] + 1
        else:
            temp[x] = 1
    for key, value in temp.items():
        # if value > 1:
        result += str(key) + str(value)
        # else:
        #     result += str(key)

    print(result)

compress("Abaabbbc")
