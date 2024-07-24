# Curso Python x Selenium

Esse é um curso feito para aprender desde o inicio da linguagem Python, até a automatização de tarefas utilizando Selenium.

## 🚀 Sumário;

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.
Consulte **[Comandos Terminal](#-Comandos-Terminal)** para saber quais fora os comandos utilizados no terminal para funcionar o arquivo.
Consulte **[Comandos Arquivo](#-Comandos-Selenium-Usados)** para saber quais funções utilizamos nesse projeto, ex: .get(), .click(), .find_element();
Consulte **[Conteúdo Curso](#-Conteúdos-Vídeos)** para ver tudo que foi passado pelo curso, pelo professor Eduardo;

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Dar exemplos
```

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Diga como essa etapa será:

```
Dar exemplos
```

E repita:

```
Até finalizar
```

Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

## ⚙️ Executando os testes

Explicar como executar os testes automatizados para este sistema.

### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

## 📦 Implantação

### Libs que utilizamos no projeto

* `urlparse: from urllib.parse import urlparse` - serve
* `Sleep: from time import sleep`
* `Chrome(): from selenium.webdriver import Chrome`
* `Firefox(): from selenium.webdriver import Firefox`
* `expected_conditions / EC: from selenium.webdriver.support import expected_conditions as EC`
* `WebDriverWait: from selenium.webdriver.support.ui import WebDriverWait`
* `By: from selenium.webdriver.common.by import By`

# Serve para poder usar o WebDriverWait





## 🐧 Comandos-Terminal

Aqui estão os comandos utilizados desde o início do projeto:

* `python -m venv .venv` - Cria uma variável de ambiente chamada **.venv** ;
* `source .venv/bin/activate` - Ativa seu ambiente para que possa instalar oque utilizaremos no projeto ;
* `pip install selenium` - Instala o Selenium dentro do ambiente em que você está ;
* `pip install --upgrade pip` - Faz o update da versão do seu pip, caso esteja obsoleto;
* `python -i "nome_arquivo"` - Executa o código / conteúdo do arquivo e não finaliza a página (Isso trava o terminal, use 'ctrl + z' para destravar);

## </> Comandos-Selenium-Usados

Aqui estão os comandos mais importantes utilizados dentro do arquivo, algo como uma documentação para que você possa utilizá-los também;

* `imagem.click()` - Usamos a variável: imagem = navegador.find_elements(By.TAG_NAME, "img"), assim somos capazes de procurar um elemento pela sua tag "a, p, img, button, etc.";
* `browser.find_elements(By.TAG_NAME, "p")` - Com essa função, nós passamos qual o navegador que estamos utilizando no caso **Chrome().find_elements(By.TAG_NAME, "p")**, assim somos capazes de buscar uma lista de elementos pela tag específica que queremos, como p, a, img, section";
* `browser.get('sua_url_aqui')` - Usamos essa função para podermos entrar no site que colocarmos no local da **url**;
* `browser.back()` - Volta para a page **anterior** (clica na flecha de voltar lá em cima do navegador);
* `browser.forward()` - **Avança** para a página mais a frente caso você já tenha entrado nela com o .get() e depois dado .back();
* `urlparse(browser.current_url)` - **Precisa-se importar uma lib** chamada **URLlib** para que possamos parsear uma url da maneira mostrada aqui! Outros comandos existentes para buscar sobre urlparse --->>>> `urlparse(browser.current_url).scheme`,`urlparse(browser.current_url).netloc`,`urlparse(browser.current_url).path`,`urlparse(browser.current_url).params`,`urlparse(browser.current_url).query`,`urlparse(browser.current_url).fragment`;
* `browser.refresh()` - Dá um f5 na página, mas só dá uma continuidade à tabela de páginas acessadas, ai é como se vocÊ desse 2 gets para a página em que você deu refresh;


## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Selenium](https://selenium-python.readthedocs.io/locating-elements.html) - Automatização para navegação em browsers;
* [Python](https://docs.python.org/pt-br/3/) - A linguagem utilizada para a criação do Projeto;
* [GIT](https://git-scm.com/docs/git/pt_BR) - Sistema de controle de revisão de código utilizado;

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📚 Conteúdos-Vídeos

* **Busca-Aninhada - Aula04** - [Vídeo Aula para saber sobre Busca Aninhada](https://youtu.be/H6D8EFSGml0?si=Sf5C5ZhfmhM65Dj1&t=141)
* **Atributos -Aula04** - [Vídeo Aula para saber sobre Atributos](https://youtu.be/H6D8EFSGml0?si=EsUyJ2CptxKlJwPa&t=1523)
* **Navegação -Aula04** - [Vídeo Aula para saber sobre Navegação](https://youtu.be/H6D8EFSGml0?si=cW5ksnVMSaA96Prc&t=2564)
* **URLLib - Aula04** - [Vídeo Aula para saber sobre URLlib](https://youtu.be/H6D8EFSGml0?si=D4Jkm4XZhDNoHQrO&t=3992)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
🤍 por [Lucas Ariosi](https://github.com/SLAriosi) 😊