#crie um script que leia uma distancia em metros e mostre em varios parametros
m = float(input('Digite uma Distancia Em Metros :'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('======================================')
print(f'Distancia em Kilometro : {km}')
print(f'Distancia em hectometro : {hm}')
print(f'Distancia em Decametro : {dm}')
print(f'Distancia em Metros : {m}')
print(f'Distancia em Decimetros : {dm:.0f}')
print(f'Distancia em Centimetros : {cm:.0f}')
print(f'Distancia em Milimetros :{mm:.0f}')
print('======================================')
