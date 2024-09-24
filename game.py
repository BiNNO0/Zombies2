import pygame, const, math, random
from load_images import *

pygame.init()
game = pygame.display.set_mode((const.anchow, const.altow))
pygame.display.set_caption("Game")

# set vars
vida = 3
player_x = 240
player_y = 180

# Cargar dos sonidos para disparo y dos para golpe
sonido_disparo_1 = pygame.mixer.Sound(r'assets\sounds\gun.wav')
sonido_disparo_2 = pygame.mixer.Sound(r'assets\sounds\gun2.wav')
sonido_golpe_1 = pygame.mixer.Sound(r'assets\sounds\hit.wav')
sonido_golpe_2 = pygame.mixer.Sound(r'assets\sounds\hit2.wav')

# Agrupar sonidos en listas
sonidos_disparo = [sonido_disparo_1, sonido_disparo_2]
sonidos_golpe = [sonido_golpe_1, sonido_golpe_2]

# Fuente para mostrar la vida
fuente = pygame.font.Font(r'assets\fonts\pixel.ttf', 30)

# Clase para las balas
class Bala:
    def __init__(self, x, y, angulo):
        self.x = x
        self.y = y
        self.velocidad = 10
        self.angulo = angulo
        self.image = pygame.Surface((5, 5))  # Crear una bala como un cuadrado
        self.image.fill((255, 255, 0))  # Bala amarilla
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def mover(self):
        self.x += math.cos(self.angulo) * self.velocidad
        self.y += math.sin(self.angulo) * self.velocidad
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)

# Clase para los enemigos
class Enemigo:
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.image_original = zombie
        self.image = self.image_original
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def mover_hacia_jugador(self, jugador_x, jugador_y):
        angulo = math.atan2(jugador_y - self.y, jugador_x - self.x)
        self.x += math.cos(angulo) * self.velocidad
        self.y += math.sin(angulo) * self.velocidad
        angulo_rotacion = math.degrees(angulo)
        self.image = pygame.transform.rotate(self.image_original, -angulo_rotacion)
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect.topleft)

# Lista para los enemigos y las balas
enemigos = []
balas = []

# Generar enemigos
def generar_enemigo():
    x = random.choice([0, const.anchow])
    y = random.choice([0, const.altow])
    vel = const.z_vel
    nuevo_enemigo = Enemigo(x, y, vel)
    enemigos.append(nuevo_enemigo)

# Temporizador para generar enemigos
GENERAR_ENEMIGO_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GENERAR_ENEMIGO_EVENT, 5000)

running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == GENERAR_ENEMIGO_EVENT:
            generar_enemigo()

    key = pygame.key.get_pressed()

    # Rotación del jugador
    rect_player = idle.get_rect(center=(player_x, player_y))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angulo = math.degrees(math.atan2(mouse_y - player_y, mouse_x - player_x))
    imagen_rotada = pygame.transform.rotate(idle, -angulo)
    rect_imagen_rotada = imagen_rotada.get_rect(center=rect_player.center)

    # Movimiento del jugador
    if key[pygame.K_w]:
        player_x += math.cos(math.radians(angulo)) * const.vel
        player_y += math.sin(math.radians(angulo)) * const.vel

    if key[pygame.K_s]:
        player_x -= math.cos(math.radians(angulo)) * const.vel
        player_y -= math.sin(math.radians(angulo)) * const.vel

    # Disparar balas
    if pygame.mouse.get_pressed()[0]:  # Si se hace clic izquierdo
        angulo_bala = math.atan2(mouse_y - player_y, mouse_x - player_x)
        nueva_bala = Bala(player_x, player_y, angulo_bala)
        balas.append(nueva_bala)
        random.choice(sonidos_disparo).play()  # Reproducir sonido de disparo aleatorio

    # Mover y dibujar balas
    for bala in balas[:]:
        bala.mover()
        bala.dibujar(game)
        # Si la bala sale de la pantalla, eliminarla
        if bala.x < 0 or bala.x > const.anchow or bala.y < 0 or bala.y > const.altow:
            balas.remove(bala)

        # Detectar colisión entre balas y enemigos
        for enemigo in enemigos[:]:
            if bala.rect.colliderect(enemigo.rect):
                enemigos.remove(enemigo)
                balas.remove(bala)
                random.choice(sonidos_golpe).play()  # Reproducir sonido de golpe aleatorio
    game.fill((100, 100, 100))
    game.blit(bg, [-10, -25])
    
    # Mover enemigos hacia el jugador y comprobar colisiones con el jugador
    for enemigo in enemigos:
        enemigo.mover_hacia_jugador(player_x, player_y)
        enemigo.dibujar(game)
        # Si el enemigo toca al jugador
        if enemigo.rect.colliderect(rect_imagen_rotada):
            vida -= 1
            enemigos.remove(enemigo)
            if vida <= 0:
                running = False  # Terminar el juego si la vida es 0

    # Dibujar fondo, jugador y balas
    game.blit(imagen_rotada, rect_imagen_rotada.topleft)

    # Mostrar vida
    texto_vida = fuente.render(f"Vida: {vida}", True, (255, 0, 0))
    game.blit(texto_vida, (10, 10))

    pygame.display.flip()

pygame.quit()


