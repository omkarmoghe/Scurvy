# from Globals import *
# from ControlBox import ControlBox
# from pygame.locals import *
# from pygame import movie
from Globals import *
from subprocess import Popen
from os import getcwd
from os import name

def show_tutorial():
    if name == "posix":
        Popen(['open', getcwd() + '/' + tutorial_movie_file_name])
    elif name == 'nt':
        Popen(["\"" + getcwd() + '/' + tutorial_movie_file_name + "\""])
    else:
        print "The operating system type " + name + " that you are using is not supported to display videos."
        assert(False)

    # pygame.display.set_caption('Tutorial')
    #
    # movie_running = 1
    # back_button = ControlBox(back_button_image, None, (50, 50), (button_size, button_size))
    # movie = pygame.movie.Movie(tutorial_movie_file_name)
    # movie.set_display(screen)
    # movie.play()
    # is_paused = False
    # while movie_running:
    #
    #     screen.blit(back_button.get_image(), back_button.rect)
    #
    #     m_pos = pygame.mouse.get_pos()
    #     # checks to see if the movie is over
    #     if not is_paused and not movie.get_busy():
    #         return
    #     for event in pygame.event.get():
    #         if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
    #             return
    #         if event.type == KEYDOWN and event.key == K_SPACE:
    #             if movie.get_busy:
    #                 movie.pause()
    #                 is_paused = True
    #             else:
    #                 movie.play()
    #                 is_paused = False
    #         if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
    #             if back_button.is_mouse_selection(m_pos):
    #                 movie.stop()
    #                 return
    #     pygame.display.update()