import sys
import os

como_usar = "Uso: python %s \"diretório pai\" \"lista de extenções\"" %(os.path.split(sys.argv[0]))[1]

def parâmetro_inicial():
    if len(sys.argv) < 3:
    	print(como_usar)
    	return False
    else:
    	return True

def verifica_diretório(diretório):
	if os.path.isdir(diretório):
		print("\n\ndiretório '%s' encontrado" %(sys.argv[1]))
		return True
	else:
		print("diretório '%s' não encontrado" %(sys.argv[1]))
		return False

def separa_extençoes(lista):
	lista = []
	i = 2
	while i < len(sys.argv):
		lista.append(sys.argv[i])
		i += 1

	return lista

def pesquisa(lista, extenção):
	try:
		return lista.index(extenção)
	except ValueError:
		return -1

def limpa_lista_extenções(lista_extenções):
	lista_limpa = []
	for elemento in lista_extenções:
		if pesquisa(lista_limpa, elemento) == -1:
			lista_limpa.append(elemento)
	print("Lista limpa")
	return lista_limpa

def abre_arquivo(nome, modo):
	arquivo = open(nome, modo, encoding="utf-8")
	return arquivo

def fecha_arquivo(arquivo):
	arquivo.close()

def procura_extenção(diretório, lista_limpa):
	extenções_encontradas = []

	for extenção in lista_limpa:
		encontrado = False
		print(" - %s: Aguarde " %extenção)
		for raiz, diretórios, arquivos in os.walk(diretório):
			for arquivo in arquivos:
				if os.path.splitext(arquivo)[1] == extenção:
					extenções_encontradas.append(extenção)
					encontrado = True
					print(" -- Encontrado\n")
					break
				if encontrado:
					break
			if encontrado:
				break
		if not encontrado:
			print(" -- Não encontrado\n")
		

	return extenções_encontradas

def css():
	print(" -- Criando estilo.css")
	css = abre_arquivo("estilo.css", "w")
	css.write("""*{
	padding: 0;
	margin: 0;
}

body{
	font-family: "Ubuntu";
	background-color: #D4D3D3;
}

li{
	list-style: none;
}


#barra-navegação{
	position: fixed;
	width: 100%;
	height: 70px;
	background-color: #A9A9A9;
	bottom: 0;
	border-top: 1px solid #ffd;
}

#titulo-menu{
	width: 1000px;
	margin: 0 auto;
	padding-bottom: 10px;
}

#titulo{
	text-align: center;
	display: block;
	margin-top: 5px;
}

#menu{
	text-align: center;
	padding: 5px 10px;
}

#menu a{
	text-decoration: none;
	padding: 5px 5px;
	margin: 10px;
	
}

#menu a:link{
	color: #4E4D4D;
}

#menu a:visited{
	color: #4E4D4D;
}

#menu a:hover{
	color: #fff;
	background-color: #5F5D5D;
}

#menu a:active{
	color: red;
}


#principal{
	width: 1000px;
	margin:  5px auto 80px auto;
}


.area-extenção{
	background-color: white;
	display: block;
	margin-bottom: 10px;
}


.titulo-extenção{
	text-align: center;
	display: block;
	margin-bottom: 20px;
	padding-top: 20px;
}


.arquivos{
	text-align: center;
	padding-bottom: 20px;
}

.arquivos a{
	text-decoration: none;
	color: #4E4D4D;
	font-size: 18px;
}

.arquivos a:hover{
	background-color: #5F5D5D;
	color: #fff;

}""")

	fecha_arquivo(css)

def operação(diretório, lista):
	html = abre_arquivo("pagina.html", "w")

	html.write("""<!doctype html>

<html>
	<head>
		<title>{0}</title>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="estilo.css">
	</head>

	<body>
		<div id="barra-navegação">
			<div id="titulo-menu">
				<span id="titulo"><h2>Extenções Encontradas</h2></span>
				<div id="menu">
""".format(" ".join(lista)))
	for e in lista:
		html.write("\t\t\t\t\t<a href=\"#{0}\">{0}</a>\n".format(e))
	html.write("""				</div>
			</div>
		</div>

		<div id="principal">\n\n""")

	for extenção in lista:
		print(" -- Escrevendo: %s" %extenção)
		html.write("""			<div class="area-extenção">
				<span class="titulo-extenção"><h2><a name="{0}">{0}</a></h2></span>
				<div class="arquivos">
					<ul>
""".format(extenção))
		for raiz, diretórios, arquivos in os.walk(diretório):
			for arquivo in arquivos:
				if os.path.splitext(arquivo)[1] == extenção:
					html.write("\t\t\t\t\t\t<li><a href=\"%s\\%s\">%s</a></li>\n"
						%(raiz, arquivo, os.path.split(arquivo)[1]))
		html.write("""					</ul>
				</div>
			</div>\n\n""")

	html.write("""		</div>
		</body>
</html>""")
	fecha_arquivo(html)


def programa():
	if parâmetro_inicial():
		if verifica_diretório(sys.argv[1]):
			lista = separa_extençoes(sys.argv)
			lista_limpa = limpa_lista_extenções(lista)
			print("Procurando alguma extenção:\n")
			extenções_encontradas = procura_extenção(sys.argv[1], lista_limpa)
			if len(extenções_encontradas) == 0:
				print("%d extenção(ões) encontradada(s)" %len(extenções_encontradas))
				print("Fim")
				return
			print("Extenção(ões) encontrada(s): %s\n" %(" ".join(extenções_encontradas)))
			print("operação:")
			css()
			operação(sys.argv[1], extenções_encontradas)
			print("Sucesso")


try:
	programa()
except KeyboardInterrupt:
	print("CTRL + C = KeyboardInterrupt")