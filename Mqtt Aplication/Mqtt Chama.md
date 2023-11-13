


Mqtt Chamada

`	`Primeiramente decidi utilizar a linguagem python por ter mais afinidade com. Após isso comecei primeiramente estudando o protocolo Mqtt, funcionamento e utilização, depois foi analisado o formato JSON, logo após parti para conhecer o Broker proposto para a realização da prática o Mosquitto.

`	`Minha primeira dificuldade foi a instalação do Broker porém após algumas tentativas e vídeos consegui efetivamente utilizá-lo e além de fins de teste realizei algumas conexões configurando dois brokers locais e realizando uma conexão bridge entre eles.

`	`Com isso aprendi os requisitos necessários para requisitar a mensagem JSON que é proposta na tarefa desta forma:

`	`Pode-se analisar que para se inscrever necessitamos do Host, da Porta e um tópico e ao nos inscrevemos recebemos um JSON com a mensagem com as informações, então o programa deve inscrever-se, verificar a inscrição, receber a mensagem,verificar a mensagem,caso seja a matrícula correta enviar de volta os seguinte parâmetros: unidade da temperatura externa, umidade da temperatura interna, a unidade de umidade e verificar através de uma comparação se o ambiente está climatizado.

`	`Comecei o código em python, ao estudar JSON, vi que existe uma biblioteca para a manipulação destes arquivos em python chamada json, já para a implementação da publicação e inscrição em protocolos MQTT existe o Paho.

Definição dos itens necessários para conexão:



Função verifica\_JSON: objetivo de verificar se um arquivo é JSON ou não:



Função resposta: objetivo é modificar o conteúdo da mensagem recebida:

Função conectar: primeiro uma função para implementação da função on\_connect que comunica quando tem uma requisição de conexão, depois efetivamente conecta, passando o host e a porta na função .connect:

Função entrada: primeiramente é criado uma função para verificar a mensagem juntando as funções anteriores e responde a matrícula, se é a correta enviar a mensagem da função resposta. Ele se inscreve com a implementação .subscribe e verifica utilizando a implementação on\_message.

Por fim, roda o código na main utiliza a variável stop para verificar se ja foi enviada a resposta caso não usa a implementação .loop\_forever que mantêm em loop o código.


