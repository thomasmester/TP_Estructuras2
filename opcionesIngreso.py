import auxiliares as aux
import verificaciones as ver
import clases.Invitado as Invitado
import json

def case3():
    nombre = ver.verificarInputSinNumeros(
        "Ingrese su nombre: ", "Ingreso invalido. Ingrese su nombre: ")
    apellido = ver.verificarInputSinNumeros(
        "Ingrese su apellido: ", "Ingreso invalido. Ingrese su apellido: ")
    jsonData = aux.jsonHandler('invitados.json')
    coincide = True
    while (coincide == True):
        coincide = False
        dni = ver.verificarNumeroInput(
            "Ingrese su DNI: ", "Ingreso invalido: ")
        email = ver.verificarInputMail()
        for i in range(len(jsonData)):
            if jsonData[i]['DNI'] == str(dni) and jsonData[i]['email'] != email:
                coincide = True
            if jsonData[i]['DNI'] != str(dni) and jsonData[i]['email'] == email:
                coincide = True
        if (coincide == True):
                print('Un usuario con el mismo dni no se puede registrar con diferentes mails y no puede registrarse más de un usuario con un mismo mail.')
        encontro = False
        for i in range(len(jsonData)):
            if int(jsonData[i]['DNI']) == dni:
                jsonData[i]['cantVecesIngresa'] = int(jsonData[i]['cantVecesIngresa']) + 1
                encontro = True
        if not encontro:
            datosInvitado = Invitado(nombre, apellido, dni, email, 1)
            jsonData.append(datosInvitado.__dict__)
        
            with open('invitados.json', 'w') as g:
                js = json.dumps(jsonData)
                g.write(js)