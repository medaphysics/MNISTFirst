import pygame

pygame.init()

# Ekran boyutları
SIM_WIDTH = 100
GRAPH_WIDTH = 1000
HEIGHT = 600
WIDTH = SIM_WIDTH + GRAPH_WIDTH
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zıplamalı Serbest Düşme + Yükseklik Grafiği")

# Renkler
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
GRAPH_COLOR = (255, 0, 0)

# Zemin
floor_y_px = HEIGHT - 50

# Zaman ve fizik sabitleri
FPS = 60
dt = 1 / FPS
pixel_per_meter = 50  # 1 m = 50 px
g = 9.81
damping = 0.8
threshold = 0.5

# Grafik verisi
graph_data = []
max_points = GRAPH_WIDTH
graph_stopped = False

class Ball:
    def __init__(self, x_px, y_px, radius_px, color, mass_kg):
        self.x = x_px
        self.y_px = y_px
        self.radius = radius_px
        self.color = color
        self.mass = mass_kg

        self.y_m = y_px / pixel_per_meter
        self.vy = 0
        self.ay = 0

    def update_physics(self):
        self.ay = g
        self.vy += self.ay * dt
        self.y_m += self.vy * dt

        self.y_px = self.y_m * pixel_per_meter

        if self.y_px + self.radius >= floor_y_px:
            self.y_px = floor_y_px - self.radius
            self.y_m = self.y_px / pixel_per_meter
            self.vy = -self.vy * damping

            if abs(self.vy) < threshold:
                self.vy = 0
                self.ay = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y_px)), self.radius)

ball = Ball(x_px=SIM_WIDTH // 2, y_px=50, radius_px=20, color=BLUE, mass_kg=2.0)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Zemin çizgisi
    pygame.draw.line(screen, BLACK, (0, floor_y_px), (SIM_WIDTH, floor_y_px), 2)

    # Fizik güncelle
    ball.update_physics()
    ball.draw(screen)

    # Grafik alanı
    graph_x = SIM_WIDTH
    pygame.draw.rect(screen, GRAY, (graph_x, 0, GRAPH_WIDTH, HEIGHT))

    # Grafik verisi güncelle
    if not graph_stopped:
        graph_data.append(ball.y_px)
        if len(graph_data) > max_points:
            graph_data.pop(0)

    # Grafik çiz
    if len(graph_data) > 1:
        for i in range(len(graph_data) - 1):
            x1 = graph_x + i
            x2 = graph_x + i + 1
            y1 = int(graph_data[i])
            y2 = int(graph_data[i + 1])
            pygame.draw.line(screen, GRAPH_COLOR, (x1, y1), (x2, y2), 2)

    if ball.vy == 0:
        graph_stopped = True

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
