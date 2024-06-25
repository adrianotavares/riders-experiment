# riders-experiment

API RESTful para Busca de Motociclistas

**User Story:**

Como usuário, 
quero pesquisar motociclistas por cidade 
para que eu possa facilmente localizar os amigos em cada cidade.

**Critérios de Aceitação:**

* A API deve receber o nome da cidade como parâmetro.
* A API deve retornar um JSON com os seguintes campos para cada motociclista encontrado:
    * id
    * name
    * city
    * latitude
    * longitude
    * brand
    * model
    * status (true ou false)

**Endpoint:**

```
GET /riders?city={city_name}
```

```json
[
  {
    "id": 1,
    "name": "João",
    "city": "São Paulo",
    "latitude": -23.55052,
    "longitude": -46.633309,
    "motorcycle_brand": "Honda",
    "motorcycle_model": "CG 160",
    "status": true
  },
  {
    "id": 2,
    "name": "Maria",
    "city": "Rio de Janeiro",
    "latitude": -22.906846,
    "longitude": -43.172896,
    "motorcycle_brand": "Yamaha",
    "motorcycle_model": "Fazer 250",
    "status": false
  }
]

```

Para executar o arquivo riders.py, você pode seguir estas etapas:

1. Abra um terminal ou prompt de comando: Navegue até o diretório onde o arquivo riders.py está salvo usando o comando cd.

2. Crie um ambiente virtual (opcional): É recomendável criar um ambiente virtual para isolar o código e as dependências do projeto. Você pode criar um ambiente virtual usando o comando python3 -m venv venv (no Linux ou macOS) ou py -3 -m venv venv (no Windows).

3. Ative o ambiente virtual (opcional): Depois de criar o ambiente virtual, você precisa ativá-lo. No Linux ou macOS, use o comando source venv/bin/activate. No Windows, use o comando venv\Scripts\activate.

4. Instale as dependências: O arquivo riders.py depende do Flask e do módulo json. Instale essas dependências usando o comando pip install flask e pip install json.

5. Execute o aplicativo: Execute o arquivo riders.py usando o comando python3 riders.py.

6. Teste a API: Depois que o aplicativo estiver em execução, você pode testar a API acessando o seguinte URL em um navegador da Web:

```
http://127.0.0.1:5000/riders?city=São Paulo
http://127.0.0.1:5000/riders?city=ALL

```
Isso retornará uma lista de motociclistas que estão localizados em São Paulo. Você pode substituir "São Paulo" pelo nome de qualquer outra cidade para filtrar os motociclistas por cidade.

Observação: Certifique-se de que o arquivo riders.json esteja no mesmo diretório que o arquivo riders.py.

**Executar Testes**

if __name__ == '__main__':
    unittest.main()

Como executar os testes:

* Salve o código acima em um arquivo chamado test_riders.py no mesmo diretório do arquivo riders.py.
* Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão salvos.
* Execute o seguinte comando:

```console
python3 test_riders.py
```

Os testes serão executados e os resultados serão exibidos no terminal.

