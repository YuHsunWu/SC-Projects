"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 10.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2,
                       y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2,
                          x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)
        self.ball_radius = ball_radius
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners.
        onmousemoved(self.reset)
        onmouseclicked(self.game)
        # Draw bricks.
        self.brick_x = 0
        self.brick_y = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                if 2 <= j < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                if 4 <= j < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                if 6 <= j < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                if 8 <= j < brick_rows:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.brick_x = (brick_width + brick_spacing)*i
                self.brick_y = brick_offset + (brick_height + brick_spacing)*j
                self.window.add(self.brick, x=self.brick_x, y=self.brick_y)

        self.score = 0
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows

        self.lose_label = GLabel('HAHAHAHAHAHAHA')
        self.lose_label.font = '-80'
        self.lose_label.color = 'black'

        self.brick_exists = self.window.get_object_at(self.window_width, self.window_height)

    def reset(self, mouse):
        if self.paddle.width/2 <= mouse.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    def game(self, start):
        if self.__dx == 0:
            self.set_ball_velocity()
            self.move_ball()
        else:
            pass

    def set_ball_velocity(self):
        self.__dx = int(random.randint(1, MAX_X_SPEED))
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def wall_collisions(self):
        if self.ball.x <= 0 or self.ball.x >= self.window.width-self.ball.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0 or self.ball.y >= self.window.height-self.ball.height:
            self.__dy = - self.__dy

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    def getdx(self):
        return self.__dx

    def getdy(self):
        return self.__dy

    def ball_hit_object(self):
        self.left_top_point = self.window.get_object_at(self.ball.x, self.ball.y)
        self.right_top_point = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.left_down_point = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.right_down_point = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        # the left top point hits an object, should be a brick or the window
        if self.left_top_point is not None:
            if self.left_top_point is not self.paddle:
                self.ball_hit_brick(self.left_top_point)
            else:
                self.__dx = - self.__dx
        else:
            if self.right_top_point is not None:
                if self.right_top_point is not self.paddle:
                    self.ball_hit_brick(self.right_top_point)
                else:
                    self.__dx = - self.__dx
            else:
                if self.left_down_point is not None:
                    if self.left_down_point is self.paddle:
                        if self.__dy > 0:
                            self.__dy -= self.__dy * 2
                        else:
                            self.__dy += self.__dy * 2
                    elif self.left_down_point is self.window:
                        self.__dx = - self.__dx
                else:
                    if self.right_down_point is not None:
                        if self.right_down_point is self.paddle:
                            if self.__dy > 0:
                                self.__dy -= self.__dy * 2
                            else:
                                self.__dy += self.__dy * 2
                        elif self.right_down_point is self.window:
                            self.__dx = - self.__dx
        # if self.ball.y + self.ball.height >= self.window.height:
        #     self.gameover()
        #     self.window.add(self.lose_label)
        if self.score == int(self.brick_cols*self.brick_rows):
            self.gamewin()

    def ball_hit_brick(self, remove_object):
        self.__dy = - self.__dy
        self.window.remove(remove_object)
        self.score += 1

    def die(self):
        self.__dx = 0
        self.__dy = 0
        self.ball.x = (self.window_width - self.ball_radius) / 2
        self.ball.y = (self.window_height - self.ball_radius) / 2

    def gameover(self):
        self.__dx = 0
        self.__dy = 0

    def gamewin(self):
        self.__dx = 0
        self.__dy = 0
