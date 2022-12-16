import pygame

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up_manager2 import PowerUpManager2
from dino_runner.utils.text_utils import draw_message_componet

FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.death_count = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.power_up_manager2 = PowerUpManager2()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()    
        
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.power_up_manager2.reset_power_ups()
        self.game_speed = 10
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()   

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.score, self.game_speed, self.player)
        self.power_up_manager2.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #Também aceita código hexadecimal "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()        
        self.power_up_manager.draw(self.screen)
        self.power_up_manager2.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"SCORE: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect_center = (800, 10)
        self.screen.blit(text, text_rect_center)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) /1000, 2)
            if time_to_show >= 0:
                draw_message_componet(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds.",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()    

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Aperte qualquer tecla para iniciar", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect_center = (half_screen_height - 1, half_screen_width - 300)
            self.screen.blit(text, text_rect_center)
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 200))
        elif self.death_count > 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Você perdeu, aperte para reiniciar", True, (0, 0, 0))
            ext_rect = text.get_rect()
            text_rect_center = (half_screen_height - 1, half_screen_width - 300)
            self.screen.blit(text, text_rect_center)
            text = font.render(f"Sua pontuação: {self.score}   Total de mortes: {self.death_count}", True, (0, 0, 0))
            ext_rect = text.get_rect()
            text_rect_center = (half_screen_height - 1, half_screen_width - 200)
            self.screen.blit(text, text_rect_center)
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 200))
        else:
            return

        pygame.display.update()
        self.handle_events_on_menu()