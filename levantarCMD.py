import subprocess
import os

# Sistema operativo: Windows
def abrir_cmd_windows(num_cmds):
    # Obtener la ruta actual del script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    programa = 'main.py'
    # Verificar que main.py existe en la ruta actual
    main_py_path = os.path.join(ruta_actual, "main.py")
    if not os.path.isfile(main_py_path):
        print(f"No se encontró {programa} en la ruta: {ruta_actual}")
        return
    # Comando para abrir una nueva ventana de cmd y ejecutar main.py
    for i in range(num_cmds):
        # Comando para abrir cmd, cambiar a la ruta actual y ejecutar main.py
        cmd_command = f'start cmd /K "cd /d {ruta_actual} && python {programa}"'
        subprocess.Popen(cmd_command, shell=True)
    print(f"Se han abierto {num_cmds} ventanas de cmd ejecutando {programa} en la ruta: {ruta_actual}")

# Sistema operativo: Linux
def abrir_terminal_linux(num_cmds):
    # Obtener ruta actual del script
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    programa = 'main.py'
    # Verificar que main.py existe en la ruta actual
    main_py_path = os.path.join(ruta_actual, "main.py")
    if not os.path.isfile(main_py_path):
        print(f"No se encontró {programa} en la ruta: {ruta_actual}")
        return
    # Detectar el shell predeterminado del usuario linux
    # Si no encuentra el shell, se usará /bin/bash por defecto
    shell_path = os.getenv('SHELL','/bin/bash')
    shell = os.path.basename(shell_path)
    # Lista de terminales
    terminales = ['gnome-terminal', 'xterm', 'konsole', 'xfce4-terminal', 'lxterminal', 'mate-terminal', 'alacritty','hyper','sakura','rxtv','tilda','yakuake']
    # Buscar una terminal gráfica compatible
    terminal = next((terminall for terminall in terminales if os.system(f'which {terminall} > /dev/null') == 0), None)
    # Si no se encontró ninguna terminal gráfica compatible
    if terminal is None:
        print("No se encontró ninguna terminal gráfica compatible.\n")
        return
    # Abrir una nueva terminal y ejecutar main.py
    for i in range(num_cmds):
        # Comando para abrir cmd, cambiar a la ruta actual y ejecutar main.py
        linux_command = f'{terminal} -- {shell} -c "cd {ruta_actual} && python3 {programa}; exec {shell}"'
        subprocess.Popen(linux_command, shell=True)
    print(f"Se han abierto {num_cmds} ventanas de cmd ejecutando {programa} en la ruta: {ruta_actual}")


if __name__ == "__main__":
    # Definir la cantidad de CMD a levantar
    num_cmds = 3  # Cambia este valor según lo que necesites
    # Verificar el sistema operativo
    if os.name == 'nt':
        abrir_cmd_windows(num_cmds)
    elif os.name == 'posix':
        abrir_terminal_linux(num_cmds)
    else:
        print("Sistema operativo no soportado")