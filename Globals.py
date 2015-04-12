import pygame

# Constants
application_name = "Scurvy"  # Adjust this to change the name of the Application
LEFT = 1  # This is the value for the mouse left button press

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Text Files
high_score_file = "highscores.txt"
settings_file = "sound_and_cheat.txt"
credits_file = "copyright.txt"

# Font Stuff
font_file = "Resources/font2.otf"
menu_font = "Resources/font.otf"
menu_item_font_size = 50

# Sound stuff
correct_press_sound = 'Resources/correct_press.wav'
incorrect_press_sound = 'Resources/incorrect_press.wav'
crash_sound = 'Resources/crash.wav'
background_sound = 'Resources/background_music1.wav'

# Menu buttons
button_size = 60
play_button_image = "Resources/StartButton.png"
back_button_image = "Resources/backButton.png"
restart_button_image = "Resources/Restart.png"
home_button_image = "Resources/Home.png"

# Text boxes
textbox_image = "Resources/textBox.png"
textbox_highlighted_image = "Resources/textBoxHighlighted.png"

# Check boxes
checkbox_image = "Resources/UncheckedBox.png"
checkbox_selected_image = "Resources/CheckedBox.png"
checkbox_size = 40

# Backgrounds
background_image = "Resources/Background.png"  # Adjust this to change the background image.
menu_background_image = "Resources/MenuBackground.png"
back_overlap = 5  # Adjust this to change how much the two backgrounds overlap so that there are no creases.

# py game initialization
background = pygame.image.load(background_image)
background_rect = background.get_rect()
WIDTH = background_rect.width
HEIGHT = 3 * background_rect.height / 2
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Health Stuff
healthbar_image = "Resources/healthbar.png"
health_image = "Resources/health.png"
initial_health = 200

# Ship Property Customization
classic_ship_location = "Resources/Classic/"
maize_and_blue_ship_location = "Resources/Michigan"
neon_ship_location = "Resources/Neon"
ship_scale = 150  # Adjust this to change the size of the ship.

# Gameplay Motion Customization
standard_velocity = -1.0  # Adjust this to change the starting velocity. WARNING: Must be negative for rightwards motion
standard_easy_velocity = -0.5  # Adjust this to change the starting velocity for easy mode.
max_velocity = -5.1  # Adjust to change the upper bound of the velocity. WARNING: Must be less than standard_velocity
acceleration = -0.1  # Adjust this to change how much the velocity changes per instruction got correct.
friction_ratio = 0.25  # Adjust this value to change the dynamic friction proportion
angle_deviations = 22.5  # Adjust this value if we get more images.
max_y_vel = 2.5  # Adjust this value to change the fastest a boat can move.
min_y_vel = -max_y_vel  # DO NOT adjust this value. It is determined dynamically based on the max velocity
move_amount = 0.3  # Adjust this value to change the acceleration of the boat.

# Fuel Stuff
fuel_amount = 50  # Adjust this to change how much time to give to the player after correctly performing an instruction
collision_fuel_punishment = 20  # Adjust this to change how much fuel gets deducted on collisions.
reduce_fuel = 1  # Adjust this to change amount control time changes per round. Usually just change control_time
max_fuel = 200  # Adjust this to change the maximum storage of fuel.

# Explosions and Rocks
rock_damage = 40  # Adjust this to change the amount of damage a Rock does.
explosion_image = "Resources/explosion.png"
size_of_explosion = 128  # Adjust this to change the size of the explosion animation thingy.
rock_image = "Resources/rock_single.png"
bad_instruction_damage = 10  # Adjust this to change the damage entering a bad instruction does.

# Cheat code constants
score_cheat_multiplier = 2
rock_damage_cheat_multiplier = 0.5
initial_cheat_score = 200
initial_cheat_fuel = 200