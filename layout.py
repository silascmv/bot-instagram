import PySimpleGUI as sg
import connector as con
#import connector as connector
sg.theme('Reddit')
class TelaPython:
    def __init__(self):
        #LAYOUT DEFINITION
        layout = [
            [sg.Text('Usuário : ',size=(10,0)),sg.Input(size=(15,0),key='user')],
            [sg.Text('Senha   : ',size=(10,0)),sg.InputText(size=(15,0), key='password', password_char='*')],
            [sg.Button('Login'),sg.Button('Exit',key='Exit')]
            #[sg.Output(size=(30,20))]
        ]
        # DEFINIR JANELA E PASSAR O LAYOUT COMO PARAMETRO
        self.janela = sg.Window("Login in Instagram",size=(500,300),element_justification='c',resizable=True).layout(layout)

    def Start(self):
        #EXTRAIR DADOS DA TELA
        while True:
            ## START LAYOUT
            self.button,self.values = self.janela.Read()
            user = self.values['user']
            password =self.values['password']
            """  print(f'User : {user}')
            print(f'Password : {password}') """
            if password == '' or user == '':
                sg.popup('Necessário Preencher Usuário e Senha!')
            else:
                print('Connectar ao Instragram')
                connection = con.Connector()
                connection.makeConnection(user,password)
               
            

loginLayout = TelaPython()
loginLayout.Start()