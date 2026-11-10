# asistente.py
# Asistente virtual de la Escuela Privada Jean Piaget.
# Recibe un mensaje y devuelve una respuesta para mostrar en la página web.

import unicodedata


def normalizar(texto):
    """Convierte el texto a minúsculas y elimina las tildes."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )


def estado_inicial():
    """Crea el estado inicial de la conversación."""
    return {}


def responder(mensaje, estado):
    """Procesa una consulta y devuelve (respuesta, estado)."""
    pregunta = normalizar(mensaje)

    if pregunta == "cuota":
        return "La cuota escolar se abona mensualmente y tiene un valor de $260.000.", estado

    elif pregunta == "vestimenta":
        return (
            "Para asistir a la institución es obligatorio utilizar el uniforme correspondiente, "
            "que consiste en una chomba azul oscuro, un pantalón cargo azul oscuro "
            "(o una pollera escocesa, opcional para las alumnas) y un suéter azul oscuro, "
            "todos con el logo de la escuela. El calzado es a elección, siempre que sea de color oscuro.\n\n"
            "El uniforme de Educación Física consiste en una chomba celeste, un jogging azul oscuro, "
            "un short azul oscuro y un buzo azul oscuro.\n\n"
            "Para los actos institucionales se utiliza el mismo pantalón o pollera, el suéter, "
            "la camisa blanca de la escuela y zapatos oscuros."
        ), estado

    elif pregunta == "horarios":
        return (
            "La cursada se realiza normalmente desde las 08:00 hasta las 12:30 hs. "
            "Sin embargo, dependiendo del año y de las materias correspondientes, "
            "algunos días puede extenderse hasta las 13:10 hs.\n\n"
            "También existen actividades de contraturno, como Educación Física, "
            "que se realizan en horarios específicos."
        ), estado

    elif pregunta in ("titulo y especializacion", "titulo", "especializacion"):
        return (
            "La escuela secundaria Jean Piaget cuenta con una orientación en Ciencias Naturales. "
            "Al finalizar los estudios, los alumnos obtienen el título de Bachiller en Ciencias Naturales, "
            "que les brinda una formación general y conocimientos relacionados con las ciencias "
            "biológicas, físicas y químicas, además de prepararlos para continuar sus estudios superiores."
        ), estado

    elif pregunta in ("sistema de faltas", "faltas", "inasistencias"):
        return (
            "La institución cuenta con un régimen de inasistencias. Al alcanzar las 15 faltas, "
            "el alumno debe abonar una reincorporación para poder continuar con su trayectoria escolar. "
            "Esta reincorporación tiene un costo mensual informado de $260."
        ), estado

    elif pregunta in ("equipo docente", "docentes", "profesores"):
        return (
            "El equipo docente está conformado por profesores especializados en las distintas materias. "
            "Los docentes pueden variar dependiendo del año que curse cada alumno.\n\n"
            "Entre los profesores de 4° y 5° año se encuentran:\n\n"
            "Física y Biofísica: Franco Tejada Barrantes.\n"
            "Matemática: Fabián Agüero.\n"
            "Química: Nicolás Zupán.\n"
            "Biología: Santiago Frías Rivero.\n"
            "Ecología: Facundo Deforel.\n"
            "Lengua y Literatura: Mariana Despa.\n"
            "Lengua Extranjera (Inglés): Lourdes Despa.\n"
            "Ciencia, Tecnología y Sociedad: Carmen Núñez.\n"
            "Construcción de Ciudadanía: Florencia Oliva.\n"
            "Filosofía y Sociología: Víctor Mercado.\n"
            "Técnicas de Estudio: María Morán.\n"
            "Educación Física: Diego Tejada Barrantes.\n"
            "Otros docentes: Sergio González, Antonella Togni, Nazarena Páez Molina y Adriana Álamo."
        ), estado

    elif pregunta == "directivos":
        return (
            "El equipo directivo y de coordinación de la institución está conformado por:\n\n"
            "Dirección General: Lic. Mariana Barrantes Mancini.\n"
            "Vicedirector del Nivel Secundario: Ing. Franco R. Tejada Barrantes.\n"
            "Representación Legal: A. Raúl Tejada.\n"
            "Coordinadora del Área de Matemáticas: Gabriela Vega.\n"
            "Coordinadora del Área de Sociales: Graciela Cortez."
        ), estado

    elif pregunta in ("hola", "buenas", "buenos dias", "buenas tardes", "buenas noches"):
        return (
            "¡Hola! Bienvenido al nivel secundario de la Escuela Privada Jean Piaget. "
            "¿Qué deseas conocer? Podés consultar por cuota, vestimenta, horarios, "
            "título y especialización, sistema de faltas, equipo docente o directivos."
        ), estado

    elif pregunta == "salir":
        return "¡Gracias por tu visita! ¡Hasta pronto!", estado

    else:
        return (
            "La opción ingresada no es válida. Podés consultar por: cuota, vestimenta, "
            "horarios, título y especialización, sistema de faltas, equipo docente o directivos."
        ), estado


# Prueba rápida indicada en la guía de la profesora.
if __name__ == "__main__":
    estado = estado_inicial()
    print(responder("hola", estado)[0])
    print(responder("cuota", estado)[0])
    print(responder("horarios", estado)[0])
