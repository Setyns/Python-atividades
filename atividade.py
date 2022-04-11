from ast import Not


while True:
  senha = input('Digite sua senha: ')
  list(senha)
  if len(senha) < 6:
    print('Deve conter no mínimo 6 caracteres.')
  elif len(senha) > 10:
    print('Deve conter no máximo 10 caracteres.')
  else:
    if not any(x.isupper() for x in senha):
      print('Deve conter pelo menos uma letra minúscula.')
    elif not any(x.islower() for x in senha):
      print('Deve conter pelo menos uma letra maiúscula.')
    elif not any(x.isdigit() == False for x in senha):
      print('Deve conter pelo menos um número.')
    else:
      break
    
print('Senha válida.')