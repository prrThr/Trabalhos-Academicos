import os
import matplotlib.pyplot as plt
import pandas as pd


def clear():
    input("Pressione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


spotify = pd.read_csv("spotify.csv", encoding="ISO-8859-1", sep=',',
                      usecols=["title", 'artist', 'top genre', 'year', 'bpm'])


# ============================ #
#      Filtros de coluna       #
# ============================ #

generos = spotify['top genre'].unique()
musicas = spotify['title'].unique()
print(generos)

print()

pesquisar_genero = str(input(
    "Pesquise um genero para verificar se ele ja esteve entre os mais populares: "))

achou = False
for g in generos:
    if pesquisar_genero in g:
        achou = True

if achou is True:
    print(
        f"O genero {pesquisar_genero.upper()} ja esteve entre os generos mais populares!")
else:
    print(
        f"O genero {pesquisar_genero.upper()} nao esteve entre os generos mais populares!")


print()


print("Pesquise uma musica para verificar se ela ja esteve entre as mais populares")
pesquisar_musica = str(input(
    "Obs: Primeira letra sempre maiuscula e use espaco caso tenha mais de uma palavra: "))

if pesquisar_musica in musicas:
    print(
        f"A musica {pesquisar_musica.upper()} ja esteve entre as musicas mais populares!")
else:
    print(
        f"A musica {pesquisar_musica.upper()} nao esteve entre as musicas mais populares!")

clear()


# ============================ #
#     Operações de filtro      #
# ============================ #

print('\n=======================================================================================')
print(" ----> Musicas de ouro do Avicii <---- ")
avicci = spotify[spotify['artist'] == 'Avicii']
avicci = avicci.filter(['title', 'year'])
print('\n', avicci)
print('\n=======================================================================================')
avicci.to_csv("Avicii.csv", sep=',', index=False)

print("----> Populares do Hip Hop entre 2015-2018 <----")
hh = spotify[spotify['top genre'].str.contains('hip hop')]
hh = hh[hh['year'] >= 2015]
hh = hh[hh['year'] <= 2018]
hh = hh.filter(['title', 'artist', 'year'])
print('\n', hh)
print('\n=======================================================================================')
hh.to_csv("BestRaps20152018.csv", sep=',', index=False)

clear()

# ============================ #
#     Operações de GroupBy     #
# ============================ #
print("\n", "#=================================================#")
print(" #        Agrupamento por Artistas em 2010         #")
print(" #=================================================#")
gpa = spotify[spotify['year'] == 2010]
gpa = gpa.filter(['title', 'artist', 'year', 'top genre', 'bpm'])
gpa.to_csv('artistas2010.csv', sep=',', index=False)
grupoPorArtista = gpa.groupby('artist')

for artista, gpa in grupoPorArtista:
    if gpa['artist'].count() == 1:
        print(f"----> {artista:<24} com {gpa['artist'].count()} musica")
    else:
        print(f"----> {artista:<24} com {gpa['artist'].count()} musicas")

print("\n", "=========================================================================", "\n")
clear()

print("\n", "#=================================================#")
print(" #          Subgeneros do HIP HOP                  #")
print(" #=================================================#")
hiphopb = spotify[spotify['top genre'].str.contains('hip hop')]
hiphopb = hiphopb.filter(['title', 'artist', 'year', 'top genre', 'bpm'])
hiphopb.to_csv('HipHop.csv', sep=',', index=False)
hhBpm = hiphopb.groupby('top genre')

for genero, hiphopb in hhBpm:
    print("-----", genero.upper(), "-----")
    print(hiphopb.filter(['title', 'artist', 'year']))
    print("\n", "===========================================================================", "\n")

clear()

# ============================ #
#          Gráficos            #
# ===========================  #
alterando = pd.read_csv("spotify.csv", encoding="ISO-8859-1", sep=',')
for nome in alterando['top genre']:
    if 'hip hop' in nome or 'rap' in nome:
        alterando.replace(to_replace=nome, value='Hip Hop', inplace=True)

    elif 'pop' in nome:
        alterando.replace(to_replace=nome, value='pop', inplace=True)

    elif 'edm' in nome or 'house' in nome or 'big room' in nome or 'electro' in nome:
        alterando.replace(to_replace=nome, value='edm', inplace=True)

    else:
        alterando.replace(to_replace=nome, value='outros', inplace=True)

# Convertendo para .csv apenas para não dar warning
alterando.to_csv("alterando.csv", sep=',', index=False)

generos = pd.read_csv("alterando.csv", sep=',')

filtrando_generos = generos[generos['top genre'].str.contains('pop')]
gpg = filtrando_generos.groupby('year')
gpg['title'].count().plot(marker='o')

filtrando_generos = generos[generos['top genre'].str.contains('Hip Hop')]
gpg = filtrando_generos.groupby('year')
gpg['title'].count().plot(marker='o')

filtrando_generos = generos[generos['top genre'].str.contains('edm')]
gpg = filtrando_generos.groupby('year')
gpg['title'].count().plot(marker='o')

filtrando_generos = generos[generos['top genre'].str.contains('outros')]
gpg = filtrando_generos.groupby('year')
gpg['title'].count().plot(marker='o')

plt.legend(['Pop', 'Hip Hop', 'EDM', 'Outros'], fancybox=True, shadow=True)
plt.title('Gêneros mais populares do spotify 2010-2019')
plt.xlabel('Ano')
plt.ylabel('Quantidade de músicas no ano')
plt.axis(xmin=2010, xmax=2019)
print("Mostrando grafico GENEROS MAIS POPULARES DO SPOTIFY 2010-2019")
plt.show()
plt.savefig("grafico_generos.svg")
os.remove("alterando.csv")

clear()

# Lendo denovo apenas para não dar warning
bpm = pd.read_csv("spotify.csv", sep=',')

filtrando_bpm = bpm[bpm['bpm'] <= 80]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')

filtrando_bpm = bpm[bpm['bpm'] > 80]
filtrando_bpm = filtrando_bpm[filtrando_bpm['bpm'] <= 100]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')

filtrando_bpm = bpm[bpm['bpm'] > 100]
filtrando_bpm = filtrando_bpm[filtrando_bpm['bpm'] <= 130]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')

filtrando_bpm = bpm[bpm['bpm'] > 130]
filtrando_bpm = filtrando_bpm[filtrando_bpm['bpm'] <= 160]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')

filtrando_bpm = bpm[bpm['bpm'] > 160]
filtrando_bpm = filtrando_bpm[filtrando_bpm['bpm'] < 200]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')

filtrando_bpm = bpm[bpm['bpm'] >= 200]
gpb = filtrando_bpm.groupby('year')
gpb['title'].count().plot(marker='o')


plt.legend(['Até 80', '81 a 100', '101 a 130', '131 a 160',
           '161 a 200', 'Mais que 200'], fancybox=True, shadow=True)
plt.title('Tendência dos BPMs em relação aos anos')
plt.xlabel('Ano')
plt.ylabel('Músicas com o BPM relacionado no ano')
plt.axis(xmin=2010, xmax=2019)
print("Mostrando grafico de BPM")
plt.show()
plt.savefig("grafico_bpm.svg")

clear()

top_artistas = spotify.groupby('artist')

for artista, spotify in top_artistas:
    if spotify['artist'].count() >= 12:
        print(f"----> {artista:<24} com {spotify['artist'].count()} musicas")
        filtrando_artistas = spotify[spotify['artist'].str.contains(artista)]
        gpa = filtrando_artistas.groupby('year')
        gpa['artist'].count().plot(label=artista, marker='o')

print("Mostrando grafico de ARTISTAS MAIS POPULARES")
print(gpa)  # Apenas para verificação

plt.legend()
plt.title('Artistas mais populares do spotify 2010-2019')
plt.xlabel('Ano')
plt.ylabel('Vezes que o artista apareceu no ano')
plt.show()
plt.savefig("ArtistasTop20102019.svg")
