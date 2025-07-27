#crie um script que digite uma cidade e se ela começa com a palavra santo

cidade = (input('Digite sua Cidade em que Naceu:')).strip()
print(cidade[:5].upper() == 'SANTO')