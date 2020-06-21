import discord
import re

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("-hello") or message.content == "-h":
        await message.channel.send("Hello, I'm a test bot. Se você ainda não possui uma frase personalizada e deseja ter uma, basta dar o cu para paulinho que ele irá lhe ajudar :). Para mais comandos digite -help.")
    elif message.content.startswith("-changeshow") or message.content.startswith("-cs"):
        subs = message.content.split(' ', 1)[1]
        arquivo = open('frases.txt', 'r', encoding='UTF-8')
        save = []
        for linha in arquivo:
            if re.search(str(message.author), linha):
                linha = str(message.author) + ":" + subs + '\n'
            save.append(linha)
        arquivo.seek(0)
        arquivo.close()
        arquivo = open('frases.txt', 'w', encoding='UTF-8')
        for linha in save:
            arquivo.write(linha)
        arquivo.close()
    elif message.content.startswith("-show") or message.content == "-s":
        arquivo = open('frases.txt', 'r', encoding='UTF-8')
        for linha in arquivo:
            if re.search(str(message.author), linha):
                await message.channel.send(linha.split(':', 1)[1])
        arquivo.seek(0)
        arquivo.close()
    elif message.content.startswith("-help"):
        await message.channel.send('''Comandos:
        -show, -s: Exibe a sua frase personalizada.
        -changeshow [nova frase], -cs [nova frase]: Atualiza a sua frase.
        -hello, -h: Boas-vindas e direcionamentos.
        Como já ficou claro acima, alguns comandos podem ser abreviados, Ex: -show -> -s''')
    elif message.content.startswith("-ricardinho"):
        await message.channel.send('Eu moido', file=discord.File('ricardo_dentadura.png'))
    elif message.content.startswith("-cringeNunes"):
        await message.channel.send("Eu sou como Matheus Nunes. Frio, calculista e estrategista. Nossa semelhança é refletida na personalidade e na aparência, ambos temos traços que demonstram nossa superioridade genética, fruto de bons genes, esses traços são: maxilar quadrado, hunter eyes, nariz fino reto e queixo extenso. O problema é que Thomas usou dos artificios que Ihe foram concedidos para o bem próprio, não deixou que sua interpretação de realidade avançada o fizesse perceber que o mundo é um ciclo de vaidade e trocas por interesse onde não existem afetividades legitimas, que depois daqui não tem mais nada, então qualquer conquista é descartável, que o movimento e a inércia não levarão a resultados diferentes.. Ou talvez ele saiba disso e mente pra si mesmo. Ou talvez eu tente justificar minha falta de caráter aguda e preguiça e minta pra mim mesmo. Pra falar a verdade eu sei que to certo mas sou modesto.")
    elif message.content.startswith("-cringeRibeiro"):
        await message.channel.send("Meu nome é Lucas Ribeiro. Eu odeio um monte de coisas, e eu particularmente não gosto de nada. O que eu tenho não é um sonho, porque eu vou torná-lo uma realidade. Vou restaurar meu harem, e matar um certo alguém.")
    elif message.content.startswith("-releaseTheUga"):
        for c in range(500):
            await message.channel.send("UGA UGA UGA UGA UGA UGA UGA")
    elif message.content.startswith("-marcelaCongratulation"):
        for c in range(10):
            await message.channel.send(
                "PARABÉNS MARCELAAAAA https://tenor.com/view/deadpool-clapping-congratu-fucking-lations-gif-14151639")

client.run('NzA0MjE4MTgwNTgyNjM3NjY5.XqZ9WA.ZsssPhRpHNhMmy6gWlhWVwTqH-4')