from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('DarkGreen')
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario',size=(40,1))],
    [sg.Text('Senha')],
    [sg.Input(key='senha',password_char='*',size=(15,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar'), sg.Button('Cancelar')],
    [sg.Text('',key='mensagem')]
]
#janela
janela = sg.Window('Tela de Login', layout)
#eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Cancelar':
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Guilherme' and valores['senha'] == '123456':
            print('Bem-vindo Guilherme')
        else:
           janela['mensagem'].update('Senha ou usuário incorreto')
