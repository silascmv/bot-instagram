from genericpath import isfile
import PySimpleGUI as sg
from instapy.util import smart_run
import connector as con
import threading

sg.theme('Reddit')

def janela_login():
     #LAYOUT DEFINITION
        layout = [
            [sg.Text('Usuário : ',size=(10,0)),sg.Input(size=(15,0),key='user')],
            [sg.Text('Senha   : ',size=(10,0)),sg.InputText(size=(15,0), key='password', password_char='*')],
            [sg.Button('Login'),sg.Button('Exit',key='Exit')],
            #[sg.Output(size=(60,15))],
            [sg.Image(r'robot.png')]
        ]
        # DEFINIR JANELA E PASSAR O LAYOUT COMO PARAMETRO
        return sg.Window("Bot for Instagram",layout=layout,size=(400,200),element_justification='c',resizable=True,finalize=True)


def janela_principal():
        layout = [
            [sg.Text('Selecionar uma opção abaixo:')],
            [sg.Button('Auto-Follow'),sg.Button('Auto-Like'),sg.Button('Auto-Comment')]
        ]
        return sg.Window('Menu Principal',layout=layout,size=(300,300),finalize=True,element_justification='c',resizable=True,)

def janela_auto_follow():
        layout = [
            [sg.Text('Configurações')],
            [sg.Text('Tags a serem seguidas : ',size=(15,0)),sg.Input(size=(15,0),key='tags')],
            [sg.Text('Quantidade de seguidores : ',size=(15,0)),sg.Input(size=(15,0),key='qntdFollowers')],
            [sg.Button('Iniciar Follow'),sg.Button('Voltar')],
            [sg.Output(size=(60,15))]
        ]
        return sg.Window('Auto-Follow Config and Start',layout=layout,finalize=True,size=(400,250),element_justification='c',resizable=True,)


def janela_auto_like():
        layout = [
            [sg.Text('Tag para curtir : ',size=(15,0)),sg.Input(size=(15,0),key='tagsToLike')],
            [sg.Text('Quantidade de Likes : ',size=(15,0)),sg.Input(size=(15,0),key='qntdLikes')],
            [sg.Button('Iniciar Likes'),sg.Button('Voltar')],
            [sg.Output(size=(60,15))]

        ]
        return sg.Window('Auto-Like Config and Start',layout=layout,finalize=True,size=(400,250),element_justification='c',resizable=True,)

def janela_auto_comment():
        layout = [
            [sg.Text('Informe a url no qual você quer comentar: ',size=(15,0)),sg.Input(size=(15,0),key='urlToComment')],
            [sg.Text('Quantidade de comentários : ',size=(15,0)),sg.Input(size=(15,0),key='qntdComment')],
            [sg.Text('Quantidade de Usuários para Marcar por comentário : ',size=(15,0)),sg.Input(size=(15,0),key='qntdUserPerComment')],
            [sg.Button('Iniciar Auto-Comment'),sg.Button('Voltar')],
            [sg.Button('Salvar Nova Lista de Usuarios'),sg.Button('Listar Usuarios Salvos')],
           # [sg.Output(size=(60,15))]


        ]
        return sg.Window('Auto-Comment Config and Start',layout=layout,finalize=True,size=(400,600),element_justification='c',resizable=True,)



tela_login = janela_login()
tela_principal = None
tela_auto_follow = None
tela_auto_like = None
tela_auto_comment = None
global connection


while True:
        window,event,values = sg.read_all_windows()
        # BLOCK OF CLOSE ACTIONS - START
        if window == tela_login and event == sg.WIN_CLOSED:
            break
        if window == tela_principal and event == sg.WIN_CLOSED:
            break
        if window == tela_auto_follow and event == sg.WIN_CLOSED:
            break
        if window == tela_auto_like and event == sg.WIN_CLOSED:
            break
        # BLOCK OF CLOSE ACTIONS - END

        # EVENTS SCREEN - LOGIN
        if window == tela_login:
            #print('Clicou no Login')
            user = values['user']
            password = values['password']
            """  print(f'User : {user}')
            print(f'Password : {password}') """
            if (password == '' or user == '') and event == 'Login':
                sg.popup('Necessário Preencher Usuário e Senha!')
            elif (password != '' and user != '') and event == 'Login':
                    sg.popup('Iniciando processo de Login - Aguarde até ser redirecionado para a pagina do seu Perfil!')
                    print('Iniciando processo de Login - Aguarde até ser redirecionado para a pagina do seu Perfil!')
                    connection = con.Connector(user,password)
                    #connection.makeConnection()
                    #con.Connector.
                    #resultado = connection.makeConnection(user,password)
                    sg.popup('Login realizado com sucesso!')
                    #print(vars(resultado))
                    #print(dir(resultado))
                    tela_principal = janela_principal()
                    tela_login.hide()
                
            if event == 'Exit':
                break
        # EVENTS SCREEN - MAIN - START
        if window == tela_principal:
            if event == 'Auto-Follow':
                tela_auto_follow = janela_auto_follow()
                tela_principal.hide()
            elif event == 'Auto-Like':
                tela_auto_like = janela_auto_like()
                tela_principal.hide()
            elif event == 'Auto-Comment':
                tela_auto_comment = janela_auto_comment()
                tela_principal.hide()
        # EVENTS SCREEN - MAIN - END

        # EVENTS SCREEN - AUTO-FOLLOW - START 
        if window == tela_auto_follow:
            if event == 'Voltar':
                tela_principal = janela_principal()
                tela_auto_follow.hide()
            if event == 'Iniciar Follow':
                tags = values['tags']
                quantidadeSeguidores = int(values['qntdFollowers'])
                if tags == '' or quantidadeSeguidores == '':
                    sg.popup('Necessário informar a quantidade de seguidores e as tags')
                else:
                    #try:
                    threading.Thread(target=connection.autoFollow,args=(tags,quantidadeSeguidores)).start()
                    #except:
                    #   print('An exception ocurred')
        # EVENTS SCREEN - AUTO-LIKE - START 
        if window == tela_auto_like:
            if event == 'Voltar':
                tela_principal = janela_principal()
                tela_auto_like.hide()
            if event == 'Iniciar Likes':
                tags = values['tagsToLike']
                quantidadeLikes = int(values['qntdLikes'])
                if tags == '' or quantidadeLikes == '':
                    sg.popup('Necessário informar a quantidade de seguidores e as tags')
                else:
                    try:
                        threading.Thread(target=connection.autoLike,args=(tags,quantidadeLikes)).start()
                        #connection.autoLike(tags,quantidadeLikes)
                    except:
                        print('An exception ocurred')

        # EVENTS SCREEN - AUTO-FOLLOW - END
        # EVENTS SCREEN - AUTO-COMMENT - START  
        if window == tela_auto_comment:
            if event == 'Voltar':
                tela_principal = janela_principal()
                tela_auto_comment.hide()
            if event == 'Iniciar Auto-Comment':
                urlToLike = values['urlToComment']
                quantidadeComment = int(values['qntdComment'])
                qntdUserPerComment = int(values['qntdUserPerComment'])
                if urlToLike == '' or quantidadeComment == '' or qntdUserPerComment == '':
                    sg.popup('Necessário informar a quantidade de comentáros, a quantidade de usuarios por comentários e a url para comentar')
                else:
                    #try:
                    print(urlToLike)
                    threading.Thread(target=connection.autoComment,args=(urlToLike,quantidadeComment,qntdUserPerComment)).start()
                    #except:
                    #print('An exception ocurred')
            if event == 'Salvar Nova Lista de Usuarios':
                    threading.Thread(target=connection.saveListFollowing).start()
            if event == 'Listar Usuarios Salvos':
                    threading.Thread(target=connection.getListFollowing).start()
        # EVENTS SCREEN - AUTO-COMMENT - END
