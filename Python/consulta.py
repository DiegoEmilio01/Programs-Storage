json = dict()
deseables, requeridas, prohibidas, hay_id = False, False, False, False
texto = '" '
if json["desired"]:
    deseables = True
    for palabra in json["desired"]:
        texto += palabra + " "
if json["required"]:
    requeridas = True
    for palabra in json["required"]:
        texto += '\"' + palabra + '\" '
if json["forbidden"]:
    prohibidas = True
    for palabra in json["forbidden"]:
        texto += "-" + palabra + " "
if json["userId"]:
    hay_id = True
    sender = json["userId"]

texto += ' "'
if deseables and not requeridas and not prohibidas:
    return None
elif not deseables and not requeridas and prohibidas:
    texto = "x " + texto
elif hay_id and not deseables and not requeridas and not prohibidas:
    return "otra_consulta"

if hay_id:
    return db.messages.find({"$and": [{"$text": {"$search": texto}}, {"sender": sender}]}, {"score": {"$meta": "textScore"}}).sort({"score": {"$meta": "textScore"}})
else:
    return db.messages.find({"$text": {"$search": texto}}, {"score": {"$meta": "textScore"}}).sort({"score": {"$meta": "textScore"}})
