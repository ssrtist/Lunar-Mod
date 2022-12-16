import cv2
import pygame

# Initialize pygame
pygame.init()

# Set up the pygame window
#window_size = (640, 480)
#screen = pygame.display.set_mode(window_size)

# Initialize the gamepad using pygame
pygame.joystick.init()

# Try to get the first gamepad
try:
    gamepad = pygame.joystick.Joystick(0)
    gamepad.init()
    print("Found gamepad:", gamepad.get_name())
except pygame.error:
    print("No gamepad found.")
    gamepad = None

# Main game loop
while True:
    # Check for events
    #for event in pygame.event.get():
    #    if event.type == pygame.QUIT:
    #        pygame.quit()
        #    exit()

    pygame.event.get()
    # Get the state of the gamepad's buttons and axes
    # buttons = [gamepad.get_button(i) for i in range(gamepad.get_numbuttons())]
    # axes = [gamepad.get_axis(i) for i in range(gamepad.get_numaxes())]
    l2 = gamepad.get_axis(4)
    
    if l2 > -0.25:
        print('L2 Down')
    else:
        print('L2 Up')

    # Update the pygame window
    #pygame.display.flip()
