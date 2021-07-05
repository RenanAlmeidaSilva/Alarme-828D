manual = ''
with open('manual.txt', 'rb') as m:
    manual = m.read().decode()
full = []
alarmes = []
txt = ''
manualList = manual.split('\n')
for linha in manualList:
    if linha not in ['Alarmes\r', 'NCK-Alarme\r']:
        if not linha.find('Manual de diagnóstico, 03/2013, 6FC5398-8BP40-3KA1') >= 0:
            if linha[:3].isdigit():
                if txt:
                    full.append(txt)
                    txt = ''

            txt += linha + '\n'
for x in full:
    if x[:7].split()[0].isdigit():
        numero = x.split()[0]
        titulo = x.split('\n')[0][x.split('\n')[0].find(' '):]
    # print(numero, titulo)
    alarmes.append(dict(
        numero=numero,
        titulo=titulo
    ))


print([x for x in alarmes if x['numero'] == '2001'][0]['titulo'])

'''    for alarme in alarmes:
        if alarme['numero'] == message.text:
            saida = (f'Titulo = {alarme["titulo"]}\n'
                    f'definicoes = {alarme["definicoes"]}\n'
                    f'Titulo = {alarme["titulo"]}\n')
                    
    if x.find('Reação:') >= 0:
        await message.answer(reacoes)

    if x.find('Definições:') >= 0:
        await message.answer(definicoes)
    else:
        definicoes = ''
    if x.find('Reação:') >= 0:
        await message.answer(reacoes)


    saida = [x for x in alarmes if x['numero'] == message.text][0]['titulo']
    saida2 = [x for x in alarmes if x['numero'] == message.text][0]['reconhecimento']
    saida3 = [x for x in alarmes if x['numero'] == message.text][0]['correcao']

    titulo = [x for x in alarmes if x['numero'] == message.text][0]['titulo']
    definicoes = [x for x in alarmes if x['numero'] == message.text][0]['definicoes']
    reacoes = [x for x in alarmes if x['numero'] == message.text][0]['reacoes']
    correcoes = [x for x in alarmes if x['numero'] == message.text][0]['correcoes']
    programa = [x for x in alarmes if x['numero'] == message.text][0]['programa']
    parametro = [x for x in alarmes if x['numero'] == message.text][0]['parametro']
    valormsg = [x for x in alarmes if x['numero'] == message.text][0]['valormsg']
    objeto = [x for x in alarmes if x['numero'] == message.text][0]['objeto']
    reconhecimento = [x for x in alarmes if x['numero'] == message.text][0]['reconhecimento']
    causa = [x for x in alarmes if x['numero'] == message.text][0]['causa']
    correcao = [x for x in alarmes if x['numero'] == message.text][0]['correcao']
    
     if txt != '':
        await message.answer(txt,parse_mode=types.ParseMode.HTML)
        
with open('alarmes.json', 'r') as f: alarmes = json.load(f)
'''