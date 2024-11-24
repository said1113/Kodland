import random

def nickname_maker(nickname_length):
    letters_numbers = "qazwsxedcrfvtgbyhnujmikolp1234567890"
    nickname = ""
    for i in range(nickname_length):
        nickname += random.choice(letters_numbers)
    return nickname

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def help():
    helper_command_1 = ""
    helper_command_2 = ""
    helper_command_3 = ""
    helper_command_4 = ""
    helper_command_1 = "$merhaba : Bu komut botla selamlaşmanız için"
    helper_command_2 = "$bye : Bu komut bota hoşça kal demeniz için"
    helper_command_3 = "$nickname : Bu komut botdan bir random nickname isteğinde bulunmanız için"
    helper_command_4 = "$password : Bu komut botdan bir random password isteğinde bulunmanız için"
    return [helper_command_1, helper_command_2, helper_command_3, helper_command_4]

nickname_length = random.randint(8, 15)
print("Generated Nickname:", nickname_maker(nickname_length))
print("Help Commands:", help())
