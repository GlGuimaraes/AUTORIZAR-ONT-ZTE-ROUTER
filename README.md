# Autorizar ONT - Script Python para Autorização de ONT em ROUTER da ZTE
Este é um script Python desenvolvido para automatizar a autorização de ONTs (Optical Network Units) em ROUTER da marca ZTE. Utilizando as bibliotecas Netmiko, datetime e time, o script simplifica o processo de configuração e autorização ao solicitar apenas algumas informações do usuário.

Com ele configuramos o equipamento e as credenciais WI-FI do cliente.

## Funcionalidades
- Autorização Automática: Autoriza ONTs em ROUTER da ZTE com base nas informações fornecidas.
- Informações Requeridas: Apenas o serial completo da ONT, o nome do cliente, o slot, PON, posição e a VLAN desejada são necessários.
## Pré-requisitos
Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- Netmiko
- datetime
- time
  
## Cofigure o Script

Abra o arquivo do script e ajuste os parâmetros conforme necessário. Você precisará fornecer o seguinte:

- Serial da ont: O serial completo da ONT que você deseja autorizar.
- Nome do Cliente: Nome do cliente para identificação.
- Slot: Slot onde a ONT será alocada.
- PON: Porta PON onde a ONT será conectada.
- Posição: Posição da ONT no slot.
- VLAN: VLAN desejada para a ONT.
- Login PPPOE do cliente.
- Senha PPPOE do cliente.
- Nome do SSID 2.4 do cliente.
- Senha do SSID 2.4 do cliente.
- Nome do SSID 5G do cliente.
- Senha do SSID do cliente.
- Execute o Script

## Contribuição
Se você deseja contribuir com melhorias ou correções para o projeto, fique à vontade para abrir um pull request. Verifique as issues abertas e sinta-se livre para relatar bugs ou sugerir novos recursos.

## Contato
Para dúvidas ou mais informações, entre em contato com: https://www.linkedin.com/in/glguimaraes23/

Email:  Glguimaraes@yahoo.com
GitHub: https://github.com/glguimaraes

## IMAGENS DO PROJETO
![dada](https://github.com/user-attachments/assets/d24774c2-e250-4b4b-a6d7-824cce36dc22)
![czxucgxzh](https://github.com/user-attachments/assets/680889df-a831-4346-8819-911d87cfdef5)



