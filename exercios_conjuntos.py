# Suponha que você foi contratado para desenvolver uma funcionalidade
# no sistema do RH de um novo banco digital. Esse banco teve acesso
# ao cadastro de clientes de outras três empresas concorrentes
# (Nubank, C6 e Inter) e gostaria de saber quais são os potenciais
# clientes. Para isso, pediu que você gerasse um relatório com 12
# items. Atenção, use apenas um print por item.

nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6     = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter  = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

# 01) Quais são os clientes de cada uma, separadamente.
print("Nubank:")
for nome in nubank:
    print(nome, end=',')
print('\n')
print("C6: ")
for nome in c6:
    print(nome, end= ', ')
print('\n')
print("Inter: ")
for nome in inter:
    print(nome, end= ', ')
print('\n')

# 02) Quais são os clientes de todas as concorrentes.
print("Clientes do Nubank, C6 e Inter: ")
print(nubank|c6|inter)
print('\n')

# 03) Quais são os clientes da Nubank que também são clientes do C6.
print("Clientes Nubank e C6: ")
print(nubank|c6)
print('\n')
    
# 04) Quais são os clientes da Nubank que também são clientes do Inter.
print("Clientes Nubank e Inter: ")
print(nubank|inter)
print('\n')

# 05) Quais são os clientes do C6 que também são clientes do Inter.
print("Mesmos clientes do C6 e Inter: ")
print(c6 & inter)
print('\n')

# 06) Quais são os clientes apenas da Nubank.
print("Clientes Nubank: ")
print(nubank - (c6|inter))
print('\n')

# 07) Quais são os clientes apenas do C6.
print('Clientes apenas do C6:')
print(c6 - (nubank|inter))
print('\n')

# 08) Quais são os clientes apenas do Inter.
print('Clientes apenas do Inter: ')
print(inter - (nubank|c6))
print('\n')

# 09) Clientes da Nubank e C6, mas não das duas ao mesmo tempo.
so_nubank = nubank - (c6|inter)
so_c6 = c6 - (nubank|inter)
so_inter = inter - (nubank|c6)
print("Clientes do Nubank e C6:")
print(so_nubank, so_c6)
print('\n')

# 10) Clientes da Nubank e Inter, mas não das duas ao mesmo tempo.
print("Clientes da Nubank e Inter: ")
print(so_nubank, so_inter)
print('\n')

# 11) Clientes do C6 e Inter, mas não dos dois ao mesmo tempo.
print("Clientes do C6 e Inter: ")
print(so_c6, so_inter)
print('\n')

# 12) Quais são os clientes das três simultaneamente.
print("Todos os clientes do Nubank, C6 e Inter: ")
print(so_nubank, so_c6, so_inter)