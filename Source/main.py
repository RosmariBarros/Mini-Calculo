import PySimpleGUI as sg


def main():
    
    # Altera cor de fundo.
    sg.theme_background_color("white")

    # Quebra em camadas
    cabecalho = [
        [sg.Text("Calculadora", font="Inter 16", background_color="white",
                 text_color="#454545", pad=(75, (20, 30)))],
    ]

    primeiro_valor = [
        [sg.Text("Primeiro valor", font="Inter 16",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
        [sg.Input("",key="primeiro_valor",font="Inter 12",background_color="white",justification='center',border_width=0, pad=(20,(0,0)),)],
        [sg.HSep(pad=(20,(0,0)))]
    ]
    
    segundo_valor = [
        [sg.Text("Segundo valor", font="Inter 16",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
        [sg.Input("",key="segundo_valor", font="Inter 12",background_color="white",justification='center',border_width=0, pad=(20,(0,0)))],
        [sg.HSep(pad=(20,(0,0)))]
    ]
    
    opcoes = [sg.OptionMenu(background_color="white", key="opcoes",values=["Soma", "Subtração", "Multiplicação", "Divisão"], expand_x=True, pad=(20,(30,0)))]
    
    resultado = [
         [sg.Text("Resultado", font="Inter 16",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
         [sg.Text("",key="resultado", font="Inter 12",
                 background_color="white", text_color="#454545", pad=(20, (30, 5)))],
    ]
    
    excluir = [sg.Image(filename="x-circle-24.png", background_color="white", pad=(120,(0,0)), enable_events=True, k="limpar")]

    # Agrupar tudo
    layout = [cabecalho, primeiro_valor, segundo_valor, opcoes, resultado, excluir]
    
    # Configurando a tela
    window = sg.Window("Calculadora", layout=layout, size=(268, 490), margins=(0, 0), grab_anywhere=True)

    # Laco de repeticao para mostra essa tela.
    while True:
        # Atribuir os valores de exibicao.
        # event = Todos os eventos que acontecem na tela. Ex: clique no botao.
        # Values = valores dos inputs recebidos na tela.
        event, values = window.read(timeout=1)

        if event == sg.WIN_CLOSED:
            break

        numero_um = values["primeiro_valor"]
        numero_dois = values["segundo_valor"]
        opcao_usuario = values["opcoes"]
        
        
        if not bool(values["segundo_valor"]) or not bool(values["primeiro_valor"]):
            window["resultado"].update("")
        
        try:
            if event == "limpar":
                window["primeiro_valor"].update("")
                window["segundo_valor"].update("")
                window["opcoes"].update("")
                window["resultado"].update("")
            
            if len(numero_um) <= 5 and len(numero_dois) <= 5:
                if opcao_usuario == "Soma":
                    calculo = int(numero_um) + int(numero_dois)
                    window["resultado"].update(f"SOMA = {calculo}")        
                if opcao_usuario == "Subtração":
                    calculo = int(numero_um) - int(numero_dois)
                    window["resultado"].update(f"Subtração = {calculo}")        
                if opcao_usuario == "Multiplicação":
                    calculo = int(numero_um) * int(numero_dois)
                    window["resultado"].update(f"Multiplicação = {calculo}")        
                if opcao_usuario == "Divisão":
                    calculo = int(numero_um) / int(numero_dois)
                    window["resultado"].update(f"Divisão = {calculo}")
                
          
        except:
            pass

main()