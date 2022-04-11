import re
def test_password(password):
    min_special_char = 1
    min_len = 6
    max_len = 16
    min_lower_char = 1
    max_upper_char = 1

    password = "@cLeiton"
    

    if len (password) < min_len:
        print('tamanho minimo de: ', min_len)
    if len (password) > max_len:
        print('tamanho maximo de: ', max_len)
    if len(re.findall(r'[@#$]', password)) < min_special_char:
     print("Precisa conter caracteres especiais '@#$'", min_special_char)
    if len(re.findall(r'[A-Z]', password)) < max_upper_char:
     print('Precisa conter maiúsculas!', max_upper_char)
    if len(re.findall(r'[a-z]', password)) < min_lower_char:
     print('Precisa conter minúsculas!', min_lower_char)

    else:
        print('senha valida! ')
