#!/usr/bin/env python3


# Importando Bibliotecas
from netmiko import ConnectHandler
from datetime import datetime
from time import sleep

# Parametros da OLT
zte = {
	'device_type': 'alcatel_aos',
	'host': 'x.x.x.x', #IP OLT
	'username': 'xxxx',  #Usuário OLT
	'password': 'xxxx', #Senha OLT
	}

# Connect to OLT
net_connect = ConnectHandler(**zte)

# show terminal to prove connection
net_connect.find_prompt()
print('\n///-///-///-///-///-///-///-///-///-///-///-///-\n')
print('SCRIPT DESENVOLVIDO POR : GUILHERME GUIMARÃES \n')
print('///-///-///-///-///-///-///-///-///-///-///-///- \n')


#Serial
serial = input("Informe o serial da ONU completo: ")

#Nome
nome = input("Informe o nome do Cliente: ")

#Slot
slot = input("Informe o SLOT: ")

#Pon
pon = input("Informe a pon: ")

#Posição
posicao = input("Informe a posição: ")

#Vlan
vlan = input("Informe a Vlan desejada: ")

#Login PPPOE
lpppoe = input("Informe o Login PPPOE do cliente: ")

#Senha PPPOE
spppoe = input("Informe a senha PPPOE do cliente: ")

#Nome wifi 2.4
ssid = input("Informe o SSID 2.4 do cliente: ")

#Senha wifi 2.4
senhassid = input("Informe a senha do SSID 2.4 do cliente: ")

#Nome wifi 5G
ssid5 = input("Informe o SSID 5G do cliente: ")

#Senha wifi 5G
senhassid5 = input("Informe a Senha do SSD 5G do cliente: ")


#Configurando a interface na OLT
conf = net_connect.send_config_set('conf t')
InterfaceOlt = net_connect.send_config_set(f'interface gpon_olt-1/{slot}/{pon}')
Autorizando = net_connect.send_config_set(f'onu {posicao} type F6600 sn {serial}')
back = net_connect.send_config_set('exit')

#Configurando a interface na posição da ONU
InterfaceOnu = net_connect.send_config_set(f'interface gpon_onu-1/{slot}/{pon}:{posicao}')
name = net_connect.send_config_set(f'name "{nome}"')
Profile = net_connect.send_config_set('tcont 1 profile 1G')
Tcont = net_connect.send_config_set('gemport 1 tcont 1')
back = net_connect.send_config_set('exit')

#Configurando mng
OnuMng = net_connect.send_config_set(f'pon-onu-mng gpon_onu-1/{slot}/{pon}:{posicao}')
Service = net_connect.send_config_set(f'service 1 gemport 1 vlan {vlan}')
PortEth = net_connect.send_config_set(f'wan-ip ipv4 mode pppoe username {lpppoe} password {spppoe} vlan-profile {vlan} host 1')
back = net_connect.send_config_set('exit')

#Configurando a interface Vport
Vport = net_connect.send_config_set(f'interface vport-1/{slot}/{pon}.{posicao}:1')
ServicePort = net_connect.send_config_set(f'service-port 1 user-vlan {vlan} vlan {vlan}')
back = net_connect.send_config_set('exit')

#Configurando parametros wifi
OnuMng = net_connect.send_config_set(f'pon-onu-mng gpon_onu-1/{slot}/{pon}:{posicao}')
nome_ssid = net_connect.send_config_set(f'ssid ctrl wifi_0/1 name {ssid}')
senha_ssid = net_connect.send_config_set(f'ssid auth wpa wifi_0/1 key {senhassid}')

nome_ssid5 = net_connect.send_config_set(f'ssid ctrl wifi_0/5 name {ssid5}')
senha_ssid5 = net_connect.send_config_set(f'ssid auth wpa wifi_0/5 key {senhassid5}')

#Verificando se conectou
conf = net_connect.send_config_set('conf t')
teste = net_connect.send_config_set(f'show gpon remote-onu wan-ip gpon_onu-1/{slot}/{pon}:{posicao}')

while 'connected' not in teste:
    sleep(7)
    teste = net_connect.send_config_set(f'show gpon remote-onu wan-ip gpon_onu-1/{slot}/{pon}:{posicao}')
    print('conectando...')

print('conectado')

# disconect ssh connection
net_connect.disconnect()
