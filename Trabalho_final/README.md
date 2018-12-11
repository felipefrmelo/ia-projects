# Text Minig: Avaliador de Comentário

### Tratamento do `virtualenv` para o flask rodar direito
+ http://flask.pocoo.org/docs/1.0/installation/#install-create-env
+ https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

### Por que e como usar
+ O FLASK é chato por nâo mudar muito bem o arquivo de serve, entâo, criw um ambiente para cada caso e utilize
1. Cri um diretorio, pode ser `venv`
2. Entra nele, depois em `/Scripts` e execute `. activate`. Isso vai executar esse ambiente e vac vai percber que no pompt vai aparecer `(base)` 
	- Agora estamo num ambiente em python zerado
3. Faça os imports por `pip` normal, de tudo que vai usar, e do flask
4. Execute no prompt (com o diretorio onde está o `server.py = arquivo micro-framework do server que voce criou`
```
http://flask.pocoo.org/docs/1.0/quickstart/
$ export FLASK_APP=hello.py
$ flask run
```
5. Tem que aparecer: `* Running on http://127.0.0.1:5000/`,
6. Para sair do flask, de CTRL+C e para sair desse ambiente, deactivate