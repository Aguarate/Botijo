__author__ = 'Aguarate - @aguarate'
# -*- coding:UTF-8
import tweepy, os

def login():
    #Tokens de la aplicación0
    CONSUMER_TOKEN =  #Consumer token
    CONSUMER_SECRET =  #Consumer secret

    #Auth de app
    auth = tweepy.OAuthHandler(CONSUMER_TOKEN, CONSUMER_SECRET)

    #Guardamos o cargamos tokens de usuario
    ACC_TOKEN_SV = os.path.expanduser('~/.botijo_keys')

    if not os.path.exists(ACC_TOKEN_SV):
        #Si el archivo de tokens no existe procedemos a crearlo
        try:
            print("URL de autorización. Copia el PIN tras permitir acceso\n")
            #Petición de URL para pin con los tokens de la app ya en 'auth'
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print("¡Error! No se ha podido obtener el token.")

        print(redirect_url)

        p = raw_input('Introduce el PIN:')

        try:
            auth.get_access_token(p)
        except tweepy.TweepError:
            print("¡Error! PIN incorrecto")

        #Valores recibidos en los atributos 'key' y 'secret' del objeto
        f = open(ACC_TOKEN_SV, 'w')
        f.write(auth.access_token.key+"\n")
        f.write(auth.access_token.secret)
        f.close()

    f = open(ACC_TOKEN_SV, 'r')
    key = f.readline().strip()

    secret = f.readline().strip()
    f.close()

    auth.set_access_token(key, secret)

    #Devolvemos una sesión autenticada lista para ser usada con la api.
    return auth