from nmap3 import *
from flask import Flask, request, jsonify
nm = nmap3.Nmap()
nm2 = nmap3.NmapScanTechniques()

def scan_top_ports(ip):

    resultado = nm.scan_top_ports(ip)
    return resultado

def detect_os(ip):
    resultado = nm.nmap_os_detection(ip)
    return resultado 

def scan_version_scan(ip):
    resultado = nm.nmap_version_detection(ip)
    return resultado

def nmap_all_ports__scan(ip):
    resultado = nm.nmap_subnet_scan(ip)
    return resultado
  
def nmap_syn_scan(ip):
    resultado = nm2.nmap_syn_scan(ip)
    return resultado

  
def nmap_fin_scan(ip):
    resultado = nm2.nmap_fin_scan(ip)
    return resultado



# API
app = Flask(__name__)

@app.route('/api/nmap', methods=['GET'])
def api():
    global ip

    MEU_USER_AGENT = 'nmap_test_api'
    
    user_agent = request.headers.get('User-Agent', '')

    if user_agent != MEU_USER_AGENT:
        return jsonify({'Erro': 'Sai fora'}), 403

    ip = request.args.get('@ip')
    opcoes = request.args

    resposta = {}

    if ip:
        resposta['@ip'] = ip
    elif ip == None:
        return jsonify({'Erro': 'Necessario um ip'}), 403
    else:
        return "Erro"

    comando = {"scan_top":scan_top_ports,
               "os": detect_os, 
               'sV': scan_version_scan, 
               'allports': nmap_all_ports__scan,
               'syn': nmap_syn_scan,
               'fin': nmap_fin_scan}
    
   
    for i in comando:
        if i in opcoes:
            resposta[i] = comando[i](ip)


    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
