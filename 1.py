import pygame
import sys


clock = pygame.time.Clock()
screen_with_levels = 0
 
class Player:
    def __init__(self, walk_right, walk_left):
        self.walk_left = walk_left
        self.walk_right = walk_right

        self.player_speed = 8
        self.player_x = 0
        self.player_y = 0

        self.player_anim_count = 0

    def hero_display(self):
        if keys[pygame.K_LEFT]:
            screen.blit(self.walk_left[self.player_anim_count], (self.player_x, self.player_y))
        else:
            screen.blit(self.walk_right[self.player_anim_count], (self.player_x, self.player_y))

    def movement(self):
        if keys[pygame.K_LEFT] and self.player_x > 10:
            self.player_x -= self.player_speed
        elif keys[pygame.K_RIGHT] and self.player_x < 520:
            self.player_x += self.player_speed
        elif keys[pygame.K_UP] and self.player_y > 10:
            self.player_y -= self.player_speed
        elif keys[pygame.K_DOWN] and self.player_y < 320:
            self.player_y += self.player_speed

    def animation(self):
        if self.player_anim_count == 2:
            self.player_anim_count = 0
        else:
            self.player_anim_count += 1


class Level_1:
    def __init__(self):
        pass

class Level_2:
    def __init__(self):
        pass

class Level_3:
    def __init__(self):
        pass


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 25)
        text_surface = font.render(self.text, True, '#1d2a36')
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return True


if __name__ == '__main__':
    pygame.init()

    size = (600, 400)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('labyrinth')

    icon = pygame.image.load('data/гриб.png')
    pygame.display.set_icon(icon)

    bg_x = 0

    bird_walk_right = [
            pygame.image.load('data/птица1.png'),
            pygame.image.load('data/птица2.png'),
            pygame.image.load('data/птица3.png')]

    bird_walk_left = [
            pygame.image.load('data/птица11.png'),
            pygame.image.load('data/птица22.png'),
            pygame.image.load('data/птица33.png')]

    player_bird = Player(bird_walk_right, bird_walk_left)

    running = True


    while running:
        if screen_with_levels == 0:
            bg = pygame.image.load('data/bg.png')

        keys = pygame.key.get_pressed()
        if screen_with_levels == 0:
            screen.blit(bg, (bg_x, 0))
            screen.blit(bg, (bg_x + 600, 0)) #смещение фона
        else:
            screen.blit(bg, (0, 0))

        #player_bird.hero_display()
        #player_bird.movement()
        #player_bird.animation()

        if bg_x == -600:
            bg_x = 0
        else:
            bg_x -= 2

        play_button = Button(185, 200, 100, 25, 'Играть', 'data/кнопка.png', 'data/кнопка1.png')
        rules_button = Button(300, 200, 100, 25, 'Правила', 'data/кнопка.png', 'data/кнопка1.png')
        back_button = Button(100, 300, 100, 25, 'Назад', 'data/кнопка.png', 'data/кнопка1.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        if screen_with_levels == 0:
            play_button.check_hover(pygame.mouse.get_pos())
            rules_button.check_hover(pygame.mouse.get_pos())
            play_button.draw(screen)
            rules_button.draw(screen)
        elif screen_with_levels == 1:
            back_button.check_hover(pygame.mouse.get_pos())
            back_button.draw(screen)

        if play_button.handle_event(event):
            screen_with_levels = 1
            bg = pygame.image.load('data/фон1.jpg')
            bg = pygame.transform.scale(bg, (600, 400))

        if back_button.handle_event(event):
            screen_with_levels = 0


        if rules_button.handle_event(event):
            print(2)


        clock.tick(9)

        pygame.display.update()