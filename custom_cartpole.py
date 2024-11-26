import pygame
import numpy as np
from gymnasium.envs.classic_control.cartpole import CartPoleEnv

class CustomCartPoleEnv(CartPoleEnv):
    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode
        self.city_background = None
        self.cart_image = None

        if render_mode == 'human':
            pygame.init()
            self.screen = pygame.display.set_mode((600, 400))
            self.clock = pygame.time.Clock()
            # Cargar imágenes personalizadas
            self.city_background = pygame.image.load('espacio1.png')
            self.city_background = pygame.transform.scale(self.city_background, (600, 400))
            self.cart_image = pygame.image.load('satelite1.png')
            self.cart_image = pygame.transform.scale(self.cart_image, (50, 30))

    def render(self):
        if self.render_mode == 'human':
            # Dibuja el fondo
            self.screen.blit(self.city_background, (0, 0))
            
            # Posición del carrito (normalizada a la pantalla)
            cart_x = int(300 + self.state[0] * 200)  # Mapear posición a píxeles
            cart_y = 300

            # Dibuja el carrito
            self.screen.blit(self.cart_image, (cart_x - 25, cart_y - 15))

            # Dibuja la vara como una línea
            pole_length = 100  # Longitud gráfica de la vara
            angle = self.state[2]  # Ángulo actual
            pole_x_end = cart_x + pole_length * np.sin(angle)
            pole_y_end = cart_y - pole_length * np.cos(angle)
            pygame.draw.line(self.screen, (0, 0, 0), (cart_x, cart_y), (pole_x_end, pole_y_end), 5)

            pygame.display.flip()
            self.clock.tick(60)
        else:
            super().render()

    def close(self):
        if self.render_mode == 'human':
            pygame.quit()
        super().close()
