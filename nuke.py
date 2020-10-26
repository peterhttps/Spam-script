import pyautogui, time

def options():
    print("Digite o que desejas spammar\n[1] Mensagem\n[2] Texto")
    choice = input("> ")
    return choice

def spamScript():
    print("Iniciando em 5 segundos")
    time.sleep(5)
    f = open("spamscript.txt", "r")
    
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

def spamWord():
    msg = input("Qual a mensagem que voce quer spamar\n> ")
    quantTimes = input("Quantas vezes?\n> ")

    print("Iniciando em 5 segundos")
    time.sleep(5)
    for i in range(int(quantTimes)):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")

option = options()
    
if str(option) == '1':
    spamWord()
elif str(option) == '2':
    spamScript()
else:
    print("digita certo ae")

print("SCRIPT FINALIZADO")



