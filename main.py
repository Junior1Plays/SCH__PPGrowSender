import requests
import time

print("\n\npp grow sender")
print("by Junior Schueller\n\n")

token = input("Insira seu Token (para o Discord autorizar a mensagem): ")

channel_id = input("\nInsira o ID do Canal: ")


print("\nEnviando...\n")


url = "https://discord.com/api/v9/channels/" + channel_id + "/messages"

payload = {
    "content": "pp grow"
}

header = {
    "authorization": token
}

def sendppgrow(tkn, cid):
    print("Aguardando 10 segundos...\n\n")
    time.sleep(10)
    r = requests.post(url, headers=header, data=payload)
    print("Mensagem enviada!\n")
    return sendppgrow(token, channel_id)

sendppgrow(token, channel_id) 
