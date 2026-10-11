# Como clonar meu repositório do GitHub e como executar o programa

### 1. Copiar o link do repositório

1. Acesse o meu [Repositório do GitHub](https://github.com/120KSN/AV5).
2. Clique no botão verde **Code**.
3. Na aba **HTTPS**, copie o link do repositório.

Exemplo:

```text
https://github.com/120KSN/AV5.git
```

### 2. Iniciar a clonagem no VS Code

1. Abra o VS Code.

2. Abra o terminal

3. Entre na pasta de destino

No Windows:

```powershell
cd "pasta/subpasta"
```

4. Clone o repositório

Execute o comando abaixo:

```bash
git clone https://github.com/usuario/projeto.git
```

Por exemplo:

```bash
git clone https://github.com/120KSN/AV5.git
```

5. Entre na pasta que foi criada

No terminal:

```bash
cd AV5
```

6. Abra o seu gerenciador do MySQL

OBS: Caso use o banco de dados SQLITE, pule para o passo 9

Abra o aplicativo que você usa para gerenciar seu servidor MYSQL (Exemplos: MySQL Workbench, DBeaver, prompt, etc.)

7. Execute o comando SQL para criar o banco de dados do projeto

```sql
CREATE DATABASE nome_do_seu_banco;
```

8. Crie o arquivo .env

Na sua pasta onde está o programa, crie o arquivo .env e coloque as seguintes informações dentro dele:

```text
MYSQL_USER=nome_de_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_HOST=servidor_do_seu_banco
MYSQL_PORT=3306
MYSQL_DATABASE=nome_do_seu_banco
```

9. Instale o uv

Caso ainda não tenha ele instalado, instale ele com:

```bash
pip install uv
```

Caso já tenha ele instalado, pule para o passo 10

10. Baixe as bibliotecas do pyproject.toml com uv

No terminal:

```bash
uv sync
```

11. Executando o programa

Rode o comando:

```bash
uv run programa_av5.py
```