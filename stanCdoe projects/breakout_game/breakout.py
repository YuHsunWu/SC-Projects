"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    num_lives = NUM_LIVES
    while num_lives != 0:
        graphics.getdx()
        graphics.getdy()
        graphics.move_ball()
        graphics.wall_collisions()
        graphics.ball_hit_object()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.die()
            num_lives -= 1
        pause(FRAME_RATE)
    graphics.gameover()



    # Add animation loop here!


if __name__ == '__main__':
    main()
