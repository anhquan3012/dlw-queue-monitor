import pygame
from pygame.locals import *
from button import Button
from check_region import in_region, count_in_regions

RED = (255, 0, 0)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# pygame.init()
# screen = pygame.display.set_mode((width, height))

pygame.font.init()
import math


def set_up_regions(screen, camera_height):
    
    running = True
    i = 0
    start_pos = None
    prev_pos = None
    first_pos = None
    
    set_up_button = Button(screen, "Press 'C' to Complete setting kiosk locations",
                           (10, camera_height-40), font=30, bg="green")
    
    regions = {}
    region_idx = 1
    
    while running:
        for event in pygame.event.get():
            set_up_button.click(event, regions)
            
            if event.type == QUIT:
                running = False
    
            elif event.type == MOUSEBUTTONDOWN:
                start_pos = event.pos
                pygame.draw.circle(screen, RED, event.pos, 6)
                if i == 0:
                    regions[region_idx] = {}
                i += 1
                regions[region_idx][f'x{i}']=event.pos[0]
                regions[region_idx][f'y{i}']=event.pos[1]
                if i == 1:
                    prev_pos = event.pos
                    first_pos = event.pos
                elif 3 >= i >= 2:
                    pygame.draw.line(screen, BLUE, prev_pos, event.pos, 4)
                    prev_pos = event.pos
                elif i == 4:
                    pygame.draw.line(screen, BLUE, prev_pos, event.pos, 4)
                    pygame.draw.line(screen, BLUE, event.pos, first_pos, 4)
                    i = 0
                    region_idx += 1
            
    
            # elif event.type == MOUSEBUTTONDOWN and 0< i <=3:
            #     pygame.draw.line(screen, BLUE, start_pos, event.pos, 4)
            
            elif event.type == KEYDOWN and event.key == pygame.K_c:
                running = False
                
        set_up_button.show()
        pygame.display.update() 
    print(regions)
        
    # print(f"\nRegion - counter: {count_in_regions(regions, points)}")
    return regions

def draw_regions(regions, screen, count):
    for k, v in regions.items():
        pygame.draw.lines(screen, GREEN, True, 
                        ((v["x1"], v["y1"]), (v["x2"], v["y2"]), (v["x3"], v["y3"]), (v["x4"], v["y4"])), 
                        4)
        font = pygame.font.SysFont("Arial", 20)
        y_text = max([v["y1"], v["y2"], v["y3"], v["y4"]]) + 10
        li=[(v["y1"],v["x1"]),(v["y2"],v["x2"]),(v["y3"],v["x3"]),(v["y4"],v["x4"])]
        li.sort()
        x_text=min(li[2][1],li[3][1])
        text = font.render(f"Kiosk {k}: {count[k]} people", 1, pygame.Color("Black"))
        size = text.get_size()
        surface = pygame.Surface(size)
        surface.fill(GREEN)
        surface.blit(text, (0, 0))
        screen.blit(surface, (x_text, y_text))

def display_text(screen, text_string, pos):
    font = pygame.font.SysFont("Arial", 50)
    text = font.render(f"{text_string}", 1, GREEN)
    size = text.get_size()
    surface = pygame.Surface(size)
    surface.fill(BLACK)
    surface.blit(text, (0, 0))
    screen.blit(surface, pos)