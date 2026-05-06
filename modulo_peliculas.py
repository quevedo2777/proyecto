"""
Agenda de pelicula.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    #creacion peliculas
    #creamos un diccionario pelicula para almacenar la informacion de la pelicula
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula#cuando se retorna el diccionario nos da la informacion de 

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto
    #encontrar pelicula
    #se verifica el nombre ingresado por el usuario por cada nombre de las peliculas guardadas
    if p1["nombre"] == nombre_pelicula:
        return p1
    elif p2["nombre"] == nombre_pelicula:
        return p2
    elif p3["nombre"] == nombre_pelicula:
        return p3
    elif p4["nombre"] == nombre_pelicula:
        return p4
    elif p5["nombre"] == nombre_pelicula:
        return p5
    else:
        return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    #guardamos la duracion en diferentes variables
    d1=p1['duracion']
    d2=p2['duracion']
    d3=p3['duracion']
    d4=p4['duracion']
    d5=p5['duracion']
    mayor=max(d1, d2, d3, d4, d5) #aqui encontramos la variable con mas duracion
    #comparamos la variable con la duracion maxima con las demas variables
    if mayor==d1:
        return p1
    elif mayor==d2:
        return p2
    elif mayor==d3:
        return p3
    elif mayor==d4:
        return p4
    elif mayor==d5:
        return p5
    return None

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    #sumamos todas las duraciones de las peliculas
    duracion= p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    #dividimos entre el total de la suma de las duraciones
    promedio= duracion // 5 
    #transformamos la duracion en hora estandar (HH:MM)
    horas = promedio // 60
    minutos = promedio % 60
    #concatenamos todo para imprimir
    if minutos < 10:
        return str(horas) + ":0" + str(minutos)
    else:
        return str(horas) + ":" + str(minutos)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    #creamos una lista con los diccionarios de las peliculas
    peliculas=[p1,p2,p3,p4,p5]
    #y una lista vacia para almacenar estrenos
    estrenos=[]
    #iteramos para buscar el valor de la clave anios
    for i in peliculas:
        if i['anio'] == anio:
            estrenos.append(i['nombre'])#guradamos el nombre de la pelicula con la fecha de estreno soliciada
    if not estrenos:#verificamos que la lista no este vacia
        return None
    return estrenos

    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    #en una lista guardamos los diccionarios
    lista=[p1,p2,p3,p4,p5]
    #y otra vacia para almacenar las peliculas mas 18
    pelis_mas18=[]
    #iteramos en la lista para encontrar peliculas mas 18
    for i in lista:
        if i['clasificacion'] == '18+':
            pelis_mas18.append(i['clasificacion'])#guardamos en la lista 
    return len(pelis_mas18)#retornamos la cantidad que representa la lista
def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    #creamos lista con los diccionarios
    peliculas = [p1, p2, p3, p4, p5]
    #en caso de que el usuario ponga el mismo dia y hora, retornara false
    for p in peliculas:
        if p != peli:
            if p["dia"] == nuevo_dia and p["hora"] == nueva_hora:
                return False

    if control_horario:
        #si la pelicula es un documental y el usuario lo reagenda despues de las 10 pm retorna false
        if "Documental" in peli["genero"] and nueva_hora >= 2200:
            return False
    #si la pelicula es de genero drama y el usuario la reagendo para el viernes debe retornar false
        if "Drama" in peli["genero"] and nuevo_dia == "Viernes":
            return False
    #si el usuario reagenda una pelicula entre semana despues de las 11 o antes de las 6 retorna false
        if nuevo_dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
            if nueva_hora >= 2300 or nueva_hora < 600:
                return False
    #aqui cambia directamente el valor de la clave en el diccionario por el valor solicitado por el usuario
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia

    return True
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    # en una variable guarda la claficicacion
    clasificacion = peli["clasificacion"]
    # descarta las peliculas en donde se puede invitar a todos
    if clasificacion == "Todos":
        return True
    #directamente evaluamos la edad del invitado con la clafisicacion y lo que retornamos es un bool
    if clasificacion == "18+":
        return edad_invitado >= 18
    #en la clasificacion 13+ si el usuario es menor a 13 años requerira de autorizacion de padres
    if clasificacion == "13+":
        if edad_invitado >= 13:
            return True
        else:
            return autorizacion_padres
    #evaluamos con or si almenos una se cumple returnara un true
    if clasificacion == "7+":
        return edad_invitado >= 7 or autorizacion_padres

    return True









