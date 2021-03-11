import gamelib

ANCHO_BORDE = 30
ANCHO_VENTANA = 300
ANCHO_ALTO_CELDA = 24

def juego_crear():
    """Inicializar el estado del juego"""
    turno = 'O'
    posicion = []
    juego = turno, posicion
    
    return juego

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    turno, posicion = juego


    if ANCHO_BORDE < x < (ANCHO_VENTANA - ANCHO_BORDE) and ANCHO_BORDE < y < (ANCHO_VENTANA - ANCHO_BORDE):

        x_centro = ANCHO_BORDE + ((x - ANCHO_BORDE) // ANCHO_ALTO_CELDA * ANCHO_ALTO_CELDA) + (ANCHO_ALTO_CELDA / 2)
        y_centro = ANCHO_BORDE + ((y - ANCHO_BORDE) // ANCHO_ALTO_CELDA * ANCHO_ALTO_CELDA) + (ANCHO_ALTO_CELDA / 2)

        if not (x_centro, y_centro) in posicion:
            posicion.append((x_centro, y_centro))

            if turno == 'O':
                return 'X', posicion
            return 'O', posicion

    return turno, posicion

def juego_mostrar(juego):
    """Actualizar la ventana"""
    turno, posicion = juego

    gamelib.title('5 EN LINEA')
    gamelib.draw_text('- ５  ｅｎ  ｌｉｎｅａ -', ANCHO_VENTANA / 2, ANCHO_BORDE - 15, fill='#0BEAFA')


    if len(posicion) > 0:
        for i in range(len(posicion)):
            if i % 2 == 0:
                gamelib.draw_text('O', posicion[i][0], posicion[i][1], fill='#01DF01')
            if i % 2 != 0:
                gamelib.draw_text('X', posicion[i][0], posicion[i][1], fill='#E819F8')


    gamelib.draw_rectangle(ANCHO_BORDE, ANCHO_BORDE, (ANCHO_VENTANA - ANCHO_BORDE), (ANCHO_VENTANA - ANCHO_BORDE), outline='#FF8000', fill='', width=2)

    for i in range((ANCHO_ALTO_CELDA + ANCHO_BORDE), (ANCHO_VENTANA - ANCHO_BORDE), ANCHO_ALTO_CELDA):
        gamelib.draw_line(ANCHO_BORDE, i, (ANCHO_VENTANA - ANCHO_BORDE), i, fill='#FFFF00', width=1)

    for j in range((ANCHO_ALTO_CELDA + ANCHO_BORDE), (ANCHO_VENTANA - ANCHO_BORDE), ANCHO_ALTO_CELDA):
        gamelib.draw_line(j, ANCHO_BORDE, j, (ANCHO_VENTANA - ANCHO_BORDE), fill='#F3F781', width=1)

    gamelib.draw_text(f'T u r n o :  {turno} ', ANCHO_VENTANA / 2, ANCHO_VENTANA - 15, fill='#0BEAFA')


def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(300, 300)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)
