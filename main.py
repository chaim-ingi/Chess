import game
import pygame
import front


def main():
    pygame.init()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.QUIT)
    surface_size = (front.SQUARE_SIZE * 8 + front.RIGHT_BAR + front.LEFT_BAR, front.SQUARE_SIZE * 8 + front.UP_BAR + front.DOWN_BAR)
    display_surface = pygame.display.set_mode(surface_size)
    two_players, level = front.Front.start_display()
    reset = False
    while True:
        if reset:
            two_players, level = front.Front.start_display()
        new_game = game.Game(display_surface, two_players, level)
        reset = new_game.game_manager()


main()
