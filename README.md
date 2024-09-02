# NmapAPI
- NmapAPI é uma API desenvolvida em Python que utiliza a biblioteca nmap3 para realizar varreduras de rede e detectar informações sobre sistemas operacionais, portas e serviços em um IP específico.

## 🛠️ Funcionalidades
- Argumentos:
  
  - (scan_top): Realiza uma varredura das principais portas.
  
  - (os): Identifica o sistema operacional do dispositivo.
  
  - (sV): Identifica os serviços em execução e suas versões.
  
  - (allports): Realiza uma varredura completa em todas as portas.
  
  - (syn): Executa uma varredura SYN.
  
  - (fin): Executa uma varredura FIN.
 
  - (exec): Executa comando no sistema. (Cuidado)

## 🚀 Utilização
- Para utilizar a API, é necessário iniciar o servidor Flask e realizar as requisições HTTP para o endpoint /api/nmap.

```bash
python NmApi.py
```
Depois que o servidor estiver em execução, você pode fazer requisições para o endpoint, incluindo o IP alvo e as opções de varredura desejadas.

- Exemplo de Requisição:

```bash
curl -H "User-Agent: nmap_test_api" "{ip}:{porta}/api/nmap?@ip={ip_alvo}&{argumentos}"
```
## 📋 Requisitos
- Certifique-se de que você tenha o Python 3.x instalado, juntamente com as bibliotecas necessárias para executar o NmapAPI.

- Instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```
## ⚠️ Aviso
- Este projeto é destinado para fins educacionais ;).

