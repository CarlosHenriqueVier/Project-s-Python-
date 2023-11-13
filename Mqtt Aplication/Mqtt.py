import json
from paho.mqtt import client as mqtt_client
stop = 0
host = 'test.mosquitto.org'
porta = 1883
topico_recebe = 'Liberato/iotTro/44xx/data'
matricula = '20000308'
topico_responde = 'Liberato/iotTro/44xx/rply/20000308'

def verifica_JSON(str):
    try:
        json.loads(str)
    except ValueError as e:
        return False
    return True

def resposta(mensagem):
    mensagem['seq'] = int(mensagem['seq']) + 800000
    mensagem['nome'] = "Carlos Henrique Vier"
    mensagem['turma'] = 4411
    if mensagem['tempInt']['valor'] > mensagem['tempExt']['valor']:
        mensagem['climatizado'] = "SIM"
    else:
        mensagem['climatizado'] = "NAO"
    del mensagem['tempExt']
    del mensagem['tempInt']
    del mensagem['umidade']

    print("Mensagem enviada")
    return json.dumps(mensagem)


def conectar():
    def conectado(client, userdata, flags, rc):
        if rc == 0:
            print("Esta conectado ao Broker.")
        else:
            print("Não esta conectado ao Broker! Erro: %d\n", rc)

    client = mqtt_client.Client(matricula)

    client.on_connect = conectado

    client.connect(host, porta)

    return client

def entrada(client: mqtt_client):
    def verifica_msg(client, userdata, msg):
        if(verifica_JSON(msg.payload.decode())):
            msg_dicpy = json.loads(msg.payload.decode()) 
            print(f"Matricula recebida é ({msg_dicpy['matricula']})")
            if(msg_dicpy['matricula'] == 20000308):
                client.publish(topico_responde, resposta(msg_dicpy))
                stop=1
            else:
                print("Matricula Errada!")
                stop=0


    client.subscribe(topico_recebe)
    
    client.on_message = verifica_msg

if __name__ == '__main__':
    client = conectar()
    while True:
        entrada(client)
        if stop == 1:
            break
        else:
            client.loop_forever()

    