#crie um script que digite uma nome completo e veja se ele tem o nome silva no nome





nome = (input('Digite seu Nome Completo :')).strip()
print(f'Seu Nome tem Silva? {'silva' in nome.lower()}')