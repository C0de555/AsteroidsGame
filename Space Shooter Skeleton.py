# Unit 4/End-of-unit-game SKELETON

import arcade
import random

# GAME CONSTANTS - change to change difficulty
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 50

LASER_SCALE = 0.5
SPRITE_SCALE = 0.5

PLAYER_SPEED = 5
PLAYER_LASER_SPEED = 6
ENEMY_SPEED = -2.5
ENEMY_LASER_SPEED = -6
METEOR_SPEED = -2

# Top portion of code is classes for all of our 'sprites' or objects in the game (player, enemy ships, meteors, etc.)
# The first couple classes are given to you. See if you can fill in the others (or add your own) based on these.


# Player uses inheritance by taking in arcade.Sprite as a parameter.
# 'Sprite' is the parent class, which includes many more fields and funcions than
# we need, but is still useful (i.e., see the update function).
# Since the Sprite class isn't defined in this file, we use the module name 'arcade'
# which holds the Sprite class.

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__("SpaceShooterRedux/PNG/playerShip1_orange.png", SPRITE_SCALE)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 30
        self.delta_x = 0
        self.laser_list = arcade.SpriteList()

    def update(self):
        # Only change x position
        self.center_x += self.delta_x

        # See if we've gone beyond the border. If so, reset our position back to the border.
        if self.center_x < RECT_WIDTH // 2:
            self.center_x = RECT_WIDTH // 2
        if self.center_x > SCREEN_WIDTH - (RECT_WIDTH // 2):
            self.center_x = SCREEN_WIDTH - (RECT_WIDTH // 2)

class Player_Laser(arcade.Sprite):

    def __init__(self):
        super().__init__("SpaceShooterRedux/PNG/Lasers/laserBlue01.png", LASER_SCALE)

    def update(self):
        self.center_y += PLAYER_LASER_SPEED

        # If laser flies off top of screen, remove it
        if self.bottom > 600:
            self.kill()

# TODO: Create an enemy ship
class Enemy(arcade.Sprite):
    # TODO: initialize enemy ship in __init__ the same way the player laser is initialized
    def __init__(self):
        super().__init__("SpaceShooterRedux/PNG/Enemies/enemyBlack3.png", SPRITE_SCALE)

    # If you scroll down to where enemy ships are created in Game.update(), you'll see that
    # their position on the screen gets defined. This means you won't have to do this here.

    def update(self):
    # TODO: Fill in the update() method, which tells the enemy how to move
        self.center_y += ENEMY_SPEED
        # if the ship flies off the bottom of the screen, remove it
        if self.top < 0:
            self.kill()

    # (hint: look at the constants defined at the top of the file, and look at how the player's laser works)

# TODO: Create an enemy laser
class Enemy_Laser(arcade.Sprite):
    # TODO: Look at how Player_Laser is defined, and do something very similar!
    def __init__(self):
        super().__init__("SpaceShooterRedux/PNG/Lasers/laserRed13.png", LASER_SCALE)

    def update(self):
        self.center_y += ENEMY_LASER_SPEED
        # if the laser flies off the bottom of screen, remove it.
        if self.top < 0:
            self.kill()
    # (again, use the constants at the top of the page to change self.center_y)

# TODO: Create a meteor
class Meteor(arcade.Sprite):
    # TODO: Create an __init__() and update() methods like you did for Enemy and Enemy_Laser
    def __init__(self):
        super().__init__("SpaceShooterRedux/PNG/Meteors/meteorGrey_med2.png", SPRITE_SCALE)

    def update(self):
        self.center_y += METEOR_SPEED
        # if the meteor flies off the bottom of the screen, remove it
        if self.top < 0:
            self.kill()

'''
Game class. Responsible for all of the game logic.
'''
class Game(arcade.Window):

    def __init__(self, width, height):

        # Initialize the window using the parent class and set the background color
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        # Initialize game information
        self.score = 0 # Score starts at 0
        self.game_over = False

        # Initialize sprites here
        self.player = Player()
        self.enemy_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()
        self.all_sprites_list = arcade.SpriteList()

    '''
    TODO:
    1) Randomly create meteors using Meteor()
    2) Randomly create enemies using Enemy()
    3) Loop through the enemy list and randomly create lasers
    4) Check if any of the player's lasers hit meteors or enemy ships
    5) Check if any objects hit the player, end the game if so
    '''
    def update(self, delta_time):

        if not self.game_over:

            # TODO: Call update on self.player and self.all_sprites_list
            self.player.update()
            self.all_sprites_list.update()

            # 1) TODO: Randomly create meteors by calling random.randrange()
            # (hint: use an if-statement, and only enter if it randrange(200) returns a specific number)
            # (that would mean that once every 200 calls to update, you'd create a meteor)

            if random.randrange(200) == 0:
                # TODO: Create a new Meteor object by calling Meteor()
                meteor = Meteor()
                # Below code sets starting position of the meteor to a random place at the top of the screen
                meteor.center_x = random.randint(1, 600)
                meteor.bottom = self.height

                # TODO: append the meteor object to the meteor list and the all sprites list
                # (this is so that we can keep track of them in the class and perform actions on them)
                self.meteor_list.append(meteor)
                self.all_sprites_list.append(meteor)

            # 2) TODO: Randomly create enemy ships by calling random.randrange()
            # (if you want more enemies to be created than meteors, call randrange() with a smaller number)

            if random.randrange(200) == 0:
                # TODO: Create a new Enemy object by calling Enemy()
                enemy = Enemy()
                # Below code sets starting position of the enemy to a random place at the top of the screen
                enemy.center_x = random.randint(1, 600)
                enemy.bottom = self.height

                # TODO: append the enemy object to the enemy list and the all sprites list
                self.enemy_list.append(enemy)
                self.all_sprites_list.append(enemy)

            # 3) TODO: Loop through the enemy list
            for enemy in self.enemy_list:
            # TODO: Randomly create lasers for the enemy to shoot by calling random.randrange()
                if random.randrange(100) == 0:
                    # TODO: Create a new laser by calling Laser()
                    laser = Enemy_Laser()
                    # Below code sets starting position of laser to bottom of enemy
                    laser.center_x = enemy.center_x
                    laser.angle = 180
                    laser.top = enemy.bottom

                    # TODO: append the laser to the all sprites list
                    self.all_sprites_list.append(laser)

            # 4) TODO: Loop through self.player's laser list
            for laser in self.player.laser_list:

                # Below code checks for collisions with the laser and the meteors and enemies and puts the 'hit' items into lists
                meteor_hit_list = arcade.check_for_collision_with_list(laser, self.meteor_list)
                enemy_hit_list = arcade.check_for_collision_with_list(laser, self.enemy_list)

                # TODO: Loop through the meteor_hit_list
                for meteor in meteor_hit_list:
                    # TODO: call kill() on the meteor and the laser (this removes them from the screen)
                    # TODO: Add to self.score
                    meteor.kill()
                    laser.kill()
                    self.score += 1

                    # TODO: Loop through the enemy_hit_list
                for enemy in enemy_hit_list:
                    # TODO: call kill() on the meteor and the laser (this removes them from the screen)
                    # TODO: Add to self.score
                    enemy.kill()
                    laser.kill()
                    self.score += 1

            # 5) TODO: Loop through the all sprites list
            for sprite in self.all_sprites_list:
                # Below code returns true if the player collided with another sprite
                collision = arcade.check_for_collision(sprite, self.player)

                # TODO: If collision is True
                if collision:
                    # TODO: Call kill() on the player
                    self.player.kill()
                    # TODO: Set the game_over variable to True
                    self.game_over = True
                    # TODO: Print the player's final score to the terminal
                    print(self.score)

    ####################### DON'T TOUCH CODE BELOW HERE ##########################

    '''
    Draw the screen (after updating).
    '''
    def on_draw(self):

        # start_render() should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on the player and the all_sprites_list (which holds everything besides the player)
        self.player.draw()
        self.all_sprites_list.draw()

        # Print out the score
        arcade.draw_text(f"Score: {self.score}", 20, 570, arcade.color.WHITE, 12)

    '''
    Called whenever a key on the keyboard is pressed.
    '''
    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.LEFT:
            self.player.delta_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.delta_x = PLAYER_SPEED
        elif key == arcade.key.SPACE:
            # Create laser
            laser = Player_Laser()
            laser.center_x = self.player.center_x
            laser.angle = 0
            laser.bottom = self.player.top

            # Add laser to player's laser list AND sprite list
            self.player.laser_list.append(laser)
            self.all_sprites_list.append(laser)

    '''
    Called whenever the user releases a left or right key. Stops player's movement.
    '''
    def on_key_release(self, key, key_modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.delta_x = 0

# Set up the window and run the game
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()