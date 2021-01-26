from PySimpleGUI import PySimpleGUI as sg

sg .theme('dark grey 9')

layout = [
    [sg.Text('User'), sg.Input(key='user', size=(25, 1))],
    [sg.Text('Pass'), sg.Input(key='pass', password_char='*', size=(25, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Login')]
]

window = sg.Window('Tela de login', layout)
print = sg.Print

while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Login':
        if values['user'] == 'Junior' and values['pass'] == '123456':
            print
            print('Bem vindo ao programa')

        else:
            print
            print('Usuário ou senha incorretos')