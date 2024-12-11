import PySimpleGUI as sg
layout = [
  [sg.text('HELLO WORLD')],
  [sg.Button('Click me')]
]

window = sg.Window('mine', layout)
while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED:
    break
  

window.close