import glfw
from OpenGL.GL import *
import math

# tuplas 
vertices_translacao = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

vertices_escala = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

vertices_rotacao = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    glClearColor(0, 0, 0, 1)

# escala
def escala(v, ex, ey):
    novo_escala = []
    for x, y in v:
        novo_escala.append([x * ex, y * ey])
    return novo_escala

# translação
def translacao(v, tx, ty):
    novo_translacao = []
    for x, y in v:
        novo_translacao.append([x + tx, y + ty])
    return novo_translacao

# rotação 
def rotacao(v, r_angulo):
    novo_rotacao = []
    
    rad = math.radians(r_angulo) 
    cos = math.cos(rad)
    sen = math.sin(rad)

    for x, y in v:
        xr = x * cos - y * sen
        yr = x * sen + y * cos
        novo_rotacao.append([xr, yr])

    return novo_rotacao

def render(v):    
    glBegin(GL_TRIANGLES)    
    for x, y in v:
        glVertex2f(x, y)                    
    glEnd()
    
def main():
    glfw.init()
    window = glfw.create_window(800, 600, "Matrizes de Transformação", None, None)
    glfw.make_context_current(window)

    init()

    v_translacao = translacao(vertices_translacao, -0.6, 0.2)
    v_escala = escala(vertices_escala, 2, 2)
    v_rotacao = translacao(rotacao(vertices_rotacao, 45), 0.5, 0)
    

    
    glClear(GL_COLOR_BUFFER_BIT)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        render(vertices_translacao)  
        render(v_translacao)
        render(v_escala)
        render(v_rotacao)

        glfw.swap_buffers(window)

    glfw.terminate()
    
if __name__ == "__main__":
    main()