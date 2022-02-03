# Streaming Debt Collector

**pt.** Esta aplicação foi construída com o intuito de automatizar o processo de envio de mensagens no whatsapp, avisando-os que o pagamento de um serviço de streaming está datado.

---

**en.** This application was built with the idea of automate the process of sending messages to whatsapp contacts, telling them that a straming service payment is due.

## How does it work (Como funciona)

**pt.** O arquivo `populate_csv.txt` reúne os dados dos contatos, presentes em variáveis de ambiente, e popula um *dict*. A partir deste é criado um *pandas.DataFrame*, o qual é exportado para o arquivo `contacts.csv`.

Em `main.py`, utilizando o módulos *Pandas* é realizada a importação desse arquivo *csv*, de onde são extraído os dados necessários para montar e enviar a mensagem logo em seguida, com a utilização do módulo *PyWhatKit*. Durante o envio da mensagem, é calculada a nova data de cobrança e armazenada no arquivo `contacts.csv`.

---

**en.** The file `populate_csv.txt` gathers all contacts data, present in enviroment variables, and populates a *dict*. From which is created a *pandas.DataFrame*, which is, then, exported to the `contacts.csv` file.

In `main.py`, by using the *Pandas* module, the *csv* is imported, where all the necessary data is extracted and the message is, then, mounted and sent to all the contacts, by using the *PyWhatKit* module. During this process, a new charge data is calculated and stored into the `contacts.csv` file.

## How to run it (Como executar)

**pt.**
1. Faça download ou clone este repositório.
2. Execute `pip install -r requirements.txt` para instalar todas as dependências necessárias.
3. Crie as suas próprias variáveis de ambiente ou insira os dados *hard-coded*. Você decide.
4. Execute `python3 populate_csv.py` para criar o seu arquivo csv. 
4. Então, finalmente, Execute `python3 main.py` para cobrar as pessoas! 

---

**en.**
1. Download or clone this repository.
2. Run `pip install -r requirements.txt` to install all dependencies.
3. Create your own Env. Vars. or hard-code the needed information. It's up to you.
4. Run `python3 populate_csv.py` to create your csv file. 
4. Then, finally, run `python3 main.py` To collect money from people! 