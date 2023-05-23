# pyChamada - Sistema de Verificação de Presença

### Como executar
1. Clone este repositório e acesse-o:
```
$ git clone https://github.com/cap-nascimento/pychamada
$ cd pychamada
```
2. Instale as dependências necessárias:
```
$ pip install -r requirements.txt
```
3. Crie (se for necessário) e execute as *migrations* para o banco de dados:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
4. Execute o projeto:
```
$ python manage.py runserver
```
### Quem fez
- Anderson Vieira do Nascimento (cap-nascimento)
- André Carvalho de Roure (AndreRoure)