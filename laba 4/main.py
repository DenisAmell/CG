import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import customtkinter

def draw_scaled(scale_x=1.0, scale_y=1.0, scale_z=1.0):
    glPushMatrix()
    glScalef(scale_x, scale_y, scale_z)
    draw_clipped_sphere(1, 20,1, 1)
    glPopMatrix()


def draw_clipped_sphere(radius, sides, vertical_scale, clip_height):
    angle_step = 360.0 / sides
    for i in range(0, sides // 2):  # Ограничиваем цикл только верхней половиной
        lat1 = math.pi * (i / sides)
        z1 = math.sin(lat1) * radius * vertical_scale
        zr1 = math.cos(lat1) * radius

        lat2 = math.pi * ((i + 1) / sides)
        z2 = math.sin(lat2) * radius * vertical_scale
        zr2 = math.cos(lat2) * radius

        glBegin(GL_QUAD_STRIP)
        for j in range(sides + 1):
            lon = 2 * math.pi * (j / sides)
            x = math.cos(lon) * zr2
            y = math.sin(lon) * zr2
            glVertex3f(x, y, z2)

            x = math.cos(lon) * zr1
            y = math.sin(lon) * zr1
            glVertex3f(x, y, z1)
        glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, -2.395 / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x = 0.8 * math.cos(math.radians(angle))
        y = 0.8 * math.sin(math.radians(angle))

        glVertex3f(x, y, -2.395 / 2.0)
    glEnd()

    # Отключаем плоскость отсечения после отрисовки полушария
    glDisable(GL_CLIP_PLANE1)


def animate():
    global rotation

    # Очистка буферов цвета и глубины
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Установка источника света
    light_position = (-1, 1, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Перемещение и вращение сцены
    glTranslatef(0.0, 0.0, -5.0)

    # Вращение полушара
    glRotatef(rotation, 1, 1, 0)

    # Рисование полушара
    glutSolidSphere(1.0, 20, 20)

    # Увеличение угла вращения
    rotation += 1

    pygame.display.flip()
    pygame.time.wait(10)


def main( radius, sides, vertical_scale, light_1, light_2, light_3, light_4):
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glLightfv(GL_LIGHT0, GL_POSITION, [light_1, light_2, light_3, light_4])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glEnable(GL_LIGHT0)
    glMaterial(GL_FRONT, GL_DIFFUSE, [0.0, 0.0, 1.0, 1.0])
    clip_height = 1.0  # Adjust the clip height as needed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rotation = light_1
        glRotatef(rotation, light_2, light_3, light_4)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_CLIP_PLANE0)
        glClipPlane(GL_CLIP_PLANE0, (0, 0, 1, clip_height))

        # Отрисовка верхней части сферы
        draw_scaled()
        draw_clipped_sphere(radius, sides, vertical_scale, clip_height)

        # glDisable(GL_CLIP_PLANE0)

        # Включение и настройка второй плоскости отсечения
        glEnable(GL_CLIP_PLANE1)
        glClipPlane(GL_CLIP_PLANE1, (0, 0, -1, clip_height))
        draw_scaled()
        # Отрисовка нижней части сферы
        draw_clipped_sphere(radius, sides, vertical_scale, clip_height)

    # glDisable(GL_CLIP_PLANE1)
        rotation += 1
        pygame.display.flip()
        pygame.time.wait(10)


def window():
    customtkinter.set_appearance_mode("dark")

    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("320x320")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label1 = customtkinter.CTkLabel(master=frame, text="parameter a value")
    label1.pack(pady=30, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter scale")
    entry1.pack(pady=10, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter light parameters")
    entry2.pack(pady=10, padx=10)

    def DoIt():
        radius = float(entry1.get().split()[0])
        sides = int(entry1.get().split()[1])
        value_z = float(entry1.get().split()[2])
        light_1 = int(entry2.get().split()[0])
        light_2 = int(entry2.get().split()[1])
        light_3 = int(entry2.get().split()[2])
        light_4 = int(entry2.get().split()[3])

        main(radius, sides, value_z, light_1, light_2, light_3, light_4)

    button = customtkinter.CTkButton(master=frame, text="Do it", command=DoIt)
    button.pack(pady=10, padx=10)

    root.mainloop()



if __name__ == "__main__":
    window()
