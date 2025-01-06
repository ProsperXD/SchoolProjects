import pygame
import random
import sys
import pickle
import os

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLACK = (0, 0, 0, 128)
LIGHT_WHITE = (255, 255, 255,128)
Light_RED = (255, 0, 0,128)
BLOCK_SIZE = 20
MIN_FPS = 5
MAX_FPS = 144
icon_image = pygame.image.load('./img/Logo.png')
pygame.display.set_icon(icon_image)
HIGH_SCORE_FILE = "./db/high_scores.pkl"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

pygame.mixer.init()
pygame.mixer.music.load('./Sounds/background_music.mp3')
pygame.mixer.music.play(-1)

collect_sound = pygame.mixer.Sound('./Sounds/collect_sound.wav')

clock = pygame.time.Clock()


def load_high_scores():
    try:
        with open(HIGH_SCORE_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def save_high_scores(scores):
    with open(HIGH_SCORE_FILE, "wb") as file:
        pickle.dump(scores, file)


def draw_snake(snake_body):
    rainbow_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130),
                      (238, 130, 238)]
    num_colors = len(rainbow_colors)
    color_index = 0
    for block_index, block in enumerate(snake_body):
        color = rainbow_colors[(color_index + block_index) % num_colors]
        pygame.draw.rect(screen, color, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def generate_food():
    food_color = (0, 0, 255)
    food_x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
    food_y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)
    pygame.draw.rect(screen, food_color, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
    return food_x // BLOCK_SIZE * BLOCK_SIZE, food_y // BLOCK_SIZE * BLOCK_SIZE


def game_over_screen(score):
    high_scores = load_high_scores()
    if score > high_scores.get("high_score", 0):
        high_scores["high_score"] = score
        save_high_scores(high_scores)

    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    game_over_text = font.render("Game Over", True, WHITE)
    score_text = font.render("Score: " + str(score), True, WHITE)
    high_score_text = font.render("High Score: " + str(high_scores.get("high_score", 0)), True, WHITE)
    play_again_text = font.render("Press Space to Play Again", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def start_screen():
    mute = False
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    start_text = font.render("Press Space to Start", True, WHITE)

    # Highlight color based on mute status
    mute_text_color = (0, 255, 0) if mute else WHITE
    mute_text = font.render("Press M to Mute/Unmute", True, mute_text_color)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(mute_text, (SCREEN_WIDTH // 2 - mute_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return mute
                elif event.key == pygame.K_m:
                    mute = not mute
                    # Update text color based on mute status
                    mute_text_color = RED if mute else (0, 255, 0)
                    mute_text = font.render("Press M to Mute/Unmute", True, mute_text_color)

                    if mute:
                        pygame.mixer.music.set_volume(0)
                        collect_sound.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(1)
                        collect_sound.set_volume(1)
                    screen.fill(BLACK)
                    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
                    screen.blit(mute_text, (SCREEN_WIDTH // 2 - mute_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))
                    pygame.display.update()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def generate_food_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def main():
    watermark_font = pygame.font.Font(None, 24)
    watermark_text = watermark_font.render("PHANS", True, WHITE)
    food_color = generate_food_color()
    mute = start_screen()
    if mute:
        pygame.mixer.music.set_volume(0)
        collect_sound.set_volume(0)
    else:
        pygame.mixer.music.set_volume(1)
        collect_sound.set_volume(1)
    snake_body = [[200, 200], [210, 200], [220, 200]]
    food_x, food_y = generate_food()

    direction = 'RIGHT'

    fps = MIN_FPS

    bg_color = LIGHT_BLACK

    score = 0

    font = pygame.font.Font(None, 36)
    background_image = pygame.image.load(os.path.join('img', 'bg.jpg'))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'
        screen.blit(background_image, (0, 0))
        if direction == 'UP':
            snake_head = [snake_body[0][0], snake_body[0][1] - BLOCK_SIZE]
        elif direction == 'DOWN':
            snake_head = [snake_body[0][0], snake_body[0][1] + BLOCK_SIZE]
        elif direction == 'LEFT':
            snake_head = [snake_body[0][0] - BLOCK_SIZE, snake_body[0][1]]
        elif direction == 'RIGHT':
            snake_head = [snake_body[0][0] + BLOCK_SIZE, snake_body[0][1]]

        snake_body.insert(0, snake_head)

        if (snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or
                snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT):
            print("Game Over")
            if game_over_screen(score):
                # Reset game variables
                snake_body = [[200, 200], [210, 200], [220, 200]]
                food_x, food_y = generate_food()
                direction = 'RIGHT'
                fps = MIN_FPS
                score = 0
            else:
                pygame.quit()
                sys.exit()

        if snake_head[0] == food_x and snake_head[1] == food_y:
            food_x, food_y = generate_food()
            food_color = generate_food_color()
            fps = min(MAX_FPS, fps + 1)
            score += 10
            collect_sound.play()
        else:
            snake_body.pop()

        #screen.fill(LIGHT_WHITE)
        draw_snake(snake_body)
        pygame.draw.rect(screen, food_color, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(watermark_text, (SCREEN_WIDTH - watermark_text.get_width() - 10, 10))
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    main()
