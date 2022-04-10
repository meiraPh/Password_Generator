import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

while 1:
    pswd_len = int(input("Insira o tamanho da senha: "))
    pswd_count = int(input("Quantas senhas você quer gerar: "))
    for x in range(0, pswd_count):
        pswd = ""
        for x in range(0, pswd_len):
            pswd_char = random.choice(chars)
            pswd = pswd + pswd_char
        print("Sua nova senha: " + pswd)
        
