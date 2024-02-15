from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# Définition du style personnalisé
custom_style = Style.from_dict({
    'prompt': 'bg:#000044 #ffffff',
    'input': '#ff0066',
    'output': '#44ff00',
})

while True:
    user_input = prompt('MonTerminal> ', style=custom_style)
    
    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'hello':
        print('Hello, world!')
    else:
        print('Command not recognized. Type "exit" to quit.')
