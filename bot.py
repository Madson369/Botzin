import discord
import random
import time
from aiohttp import request
import os
from time import sleep
from discord.ext import commands, tasks
from itertools import cycle
import asyncio

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    # ,activity=discord.Game('Comendo cu de curioso'))
    await client.change_presence(status=discord.Status.online)
    print('bot is ready')
    change_status.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('leon'):
        await message.channel.send('opiniao errada!')

    if message.content.startswith('jair'):
        await message.channel.send('kkk gay!')

    if message.content.startswith('teu pai'):
        await message.channel.send('o teu!')

    if message.content.startswith('cara intrometido'):
        await message.channel.send('MEU PAU TEM VITILIGO')

    if message.content.startswith('fish pog'):
        await message.channel.send('https://tenor.com/view/fish-pog-fish-poggers-fish-pog-champ-poggers-gif-16548474')

    if message.content.startswith('hmm'):
        await message.channel.send('https://tenor.com/view/cadeirudo-dancing-party-hard-gif-11502959')

    if message.content.startswith('POG'):
        await message.channel.send('https://tenor.com/view/rise-pieces-pog-is-alive-when-you-say-pog-pog-gif-17519305')

    if message.content.startswith('agr vai'):
        await message.channel.send("<:zuki:719757832756658247>")

    if message.content.startswith('diz oi ronaldo'):
        await message.channel.send("oi oq fdp ta me tirando")

    if message.content.startswith('?'):
        await message.channel.send("sim")

    if message.content.startswith('janux'):
        await message.channel.send("https://preview.redd.it/ownxbkpyjs061.png?width=640&height=377&crop=smart&auto=webp&s=4e0a1bc23fd2928fe99da1f5789b036e004488dd")
    
    if message.content.startswith('Manel'):
        await message.channel.send("Bom dia você conhece o manel nariz de aspirador?")
    
    if message.content.startswith('sim'):
        await message.channel.send("não")
    
    if message.content.startswith('bot buro'):
        await message.channel.send("teu cu")

    if message.content.startswith('bot burro'):
        await message.channel.send("teu cu  ")

    if message.content.startswith('cala a boca ronaldo'):
        await message.channel.send("ti fude maluco ")
    
    if message.content.startswith('humor'):
        await message.channel.send('sim')

   
        
    await client.process_commands(message)


@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def foto(ctx):
    author = ctx.message.author
    pfp = author.avatar_url
    await ctx.channel.send(pfp)





@client.command(aliases=['8ball', '8bola'])
async def _8ball(ctx, *, question):
    responses = ["claro porra.",
                 "sem duvida.",
                 "sem duvida confia.",
                 "Sim - pode apostar fdp.",
                 "vai.",
                 "provavelmente.",
                 "parece bom.",
                 "Sim.",
                 "Pergunta depois.",
                 "a meia noite te conto segredo gigatonico.",
                 "sla porra.",
                 "pergunte denovo mais tarde.",
                 "Não conte com isso.",
                 "eu acho que não.",
                 "minhas fontes dizem que não.",
                 "não parece bom.",
                 "duvidoso."]
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

players = {}


@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def gostosa(ctx):
    await ctx.author.send ("gostosa")
    await ctx.author.send ("gostosa")
    await ctx.author.send ("gostosa")
    await ctx.author.send ("gostosa")

@client.command()
async def nome(ctx):
    await ctx.send(crianome())

@client.command()
async def lerolero(ctx):
    await ctx.send(lerolero1())

@client.command()
async def nick(ctx):
    try:
        await ctx.message.delete()
        await ctx.author.edit(nick=crianome())
    except discord.errors.Forbidden:
        await ctx.channel.send("tenho permissao n")
    else:
        await ctx.channel.send("mudei o nick la brother")

        #    await ctx.author.send("tenho permissao n")
        #else:
        #await ctx.author.send("mudei o nick la brother")


@client.command()
async def leave(ctx):
    vc = ctx.voice_client

    if not vc:
        await ctx.send("ta falando sozinho esquizofrenico")
        return

    await vc.disconnect()
    await ctx.send("flw puta")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')



for filename in os.listdir('C:/Users/Madso/Desktop/Bot/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@tasks.loop(minutes=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

status = cycle(['comendo cu de curioso', 'porra nenhuma','coçando as bola' ])


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('pleas pass in all required arguments.')


#putaria aq abaixo



import random

def crianome():

    f = open('C://Users//Madso//Desktop//nomes//animais.txt')
    text = f.readlines()
    f.close()

    a = []
    [a.append(line.rstrip("\n"))for line in text]

    animal = random.choice(a)



    f = open('C://Users//Madso//Desktop//nomes//adjetivos.txt')
    text = f.readlines()
    f.close()

    b = []
    [b.append(line.rstrip("\n"))for line in text]

    adjetivo = random.choice(b)



    f = open('C://Users//Madso//Desktop//nomes//adjetivos.txt')
    text = f.readlines()
    f.close()

    d = []
    [d.append(line.rstrip("\n"))for line in text]

    adjetivo2 = random.choice(d)

    f = open('C://Users//Madso//Desktop//nomes//noun.txt')
    text = f.readlines()
    f.close()

    c = []
    [c.append(line.rstrip("\n"))for line in text]

    noun = random.choice(c)

    nome = adjetivo.capitalize()+adjetivo2.capitalize()+noun.capitalize()+animal.capitalize()

    if len(nome) > 32:
        return crianome()

    if len(nome) <= 32:
        return nome 


def lerolero1():
    
        frase = ""
        
        pica1 = [
            "Caros amigos, ",
            "Por outro lado, ",
            "Assim mesmo, ",
            "No entanto, não podemos esquecer que ",
            "Do mesmo modo, ",
            "A prática cotidiana prova que ",
            "Nunca é demais lembrar o peso e o significado destes problemas, uma vez que ",
            "As experiências acumuladas demonstram que ",
            "Acima de tudo, é fundamental ressaltar que ",
            "O incentivo ao avanço tecnológico, assim como ",
            "Não obstante, ",
            "Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se ",
            "Pensando mais a longo prazo, ",
            "O que temos que ter sempre em mente é que ",
            "Ainda assim, existem dúvidas a respeito de como ",
            "Gostaria de enfatizar que ",
            "Todavia, ",
            "A nível organizacional, ",
            "O empenho em analisar ",
            "Percebemos, cada vez mais, que ",
            "No mundo atual, ",
            "É importante questionar o quanto ",
            "Neste sentido, ",
            "Evidentemente, ",
            "Por conseguinte, ",
            "É claro que ",
            "Podemos já vislumbrar o modo pelo qual ",
            "Desta maneira, ",
            "O cuidado em identificar pontos críticos n",
            "A certificação de metodologias que nos auxiliam a lidar com "
        ]

        pica2 =[
            "a execução dos pontos do programa ",
            "a complexidade dos estudos efetuados ",
            "a contínua expansão de nossa atividade ",
            "a estrutura atual da organização ",
            "o novo modelo estrutural aqui preconizado ",
            "o desenvolvimento contínuo de distintas formas de atuação ",
            "a constante divulgação das informações ",
            "a consolidação das estruturas ",
            "a consulta aos diversos militantes ",
            "o início da atividade geral de formação de atitudes ",
            "o desafiador cenário globalizado ",
            "a mobilidade dos capitais internacionais ",
            "o fenômeno da Internet ",
            "a hegemonia do ambiente político ",
            "a expansão dos mercados mundiais ",
            "o aumento do diálogo entre os diferentes setores produtivos ",
            "a crescente influência da mídia ",
            "a necessidade de renovação processual ",
            "a competitividade nas transações comerciais ",
            "o surgimento do comércio virtual ",
            "a revolução dos costumes ",
            "o acompanhamento das preferências de consumo ",
            "o comprometimento entre as equipes ",
            "a determinação clara de objetivos ",
            "a adoção de políticas descentralizadoras ",
            "a valorização de fatores subjetivos ",
            "a percepção das dificuldades ",
            "o entendimento das metas propostas ",
            "o consenso sobre a necessidade de qualificação ",
            "o julgamento imparcial das eventualidades "
        ]
        pica3 = [
            "nos obriga à análise ",
            "cumpre um papel essencial na formulação ",
            "exige a precisão e a definição ",
            "auxilia a preparação e a composição ",
            "garante a contribuição de um grupo importante na determinação ",
            "assume importantes posições no estabelecimento ",
            "facilita a criação ",
            "obstaculiza a apreciação da importância ",
            "oferece uma interessante oportunidade para verificação ",
            "acarreta um processo de reformulação e modernização ",
            "pode nos levar a considerar a reestruturação ",
            "representa uma abertura para a melhoria ",
            "ainda não demonstrou convincentemente que vai participar na mudança ",
            "talvez venha a ressaltar a relatividade ",
            "prepara-nos para enfrentar situações atípicas decorrentes ",
            "maximiza as possibilidades por conta ",
            "desafia a capacidade de equalização ",
            "agrega valor ao estabelecimento ",
            "é uma das consequências ",
            "promove a alavancagem ",
            "não pode mais se dissociar ",
            "possibilita uma melhor visão global ",
            "estimula a padronização ",
            "aponta para a melhoria ",
            "faz parte de um processo de gerenciamento ",
            "causa impacto indireto na reavaliação ",
            "apresenta tendências no sentido de aprovar a manutenção ",
            "estende o alcance e a importância ",
            "deve passar por modificações independentemente ",
            "afeta positivamente a correta previsão "
        ]
        pica4 = [
            "das condições financeiras e administrativas exigidas.",
            "das diretrizes de desenvolvimento para o futuro.",
            "do sistema de participação geral.",
            "das posturas dos órgãos dirigentes com relação às suas atribuições.",
            "das novas proposições.",
            "das direções preferenciais no sentido do progresso.",
            "do sistema de formação de quadros que corresponde às necessidades.",
            "das condições inegavelmente apropriadas.",
            "dos índices pretendidos.",
            "das formas de ação.",
            "dos paradigmas corporativos.",
            "dos relacionamentos verticais entre as hierarquias.",
            "do processo de comunicação como um todo.",
            "dos métodos utilizados na avaliação de resultados.",
            "de todos os recursos funcionais envolvidos.",
            "dos níveis de motivação departamental.",
            "da gestão inovadora da qual fazemos parte.",
            "dos modos de operação convencionais.",
            "de alternativas às soluções ortodoxas.",
            "dos procedimentos normalmente adotados.",
            "dos conhecimentos estratégicos para atingir a excelência.",
            "do fluxo de informações.",
            "do levantamento das variáveis envolvidas.",
            "das diversas correntes de pensamento.",
            "do impacto na agilidade decisória.",
            "das regras de conduta normativas.",
            "do orçamento setorial.",
            "do retorno esperado a longo prazo.",
            "do investimento em reciclagem técnica.",
            "do remanejamento dos quadros funcionais."
        ]
        a = random.choice(pica1)
        b = random.choice(pica2)
        c = random.choice(pica3)
        d = random.choice(pica4)
        

        frase = a + b + c + d
        return frase







             
#putaria aq acima

client.run('Nzc5OTUwODk2ODU1MTIxOTMw.X7n_4A.rFt55PL9lCLAa59p89jQ_5PNftQ')
