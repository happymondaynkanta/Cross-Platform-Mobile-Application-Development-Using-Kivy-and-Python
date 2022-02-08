# Step 1 - Create the App
# Step 2 - Create the Game
# Step 3 - Build the Game
# Step 4 - Run the App


from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector 
from kivy.clock import Clock 
from random import randint


class PongPaddle(Widget):
# Collision detection
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.1


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0) 
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest position = current velocity + current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# On_touch_down() - When our fingers/mouse touches the screen
# On_touch_up() - When we lift our fingers/mouse of the  after touching the screen
# On_touch_move() - When we drag our fingers/mouse on the screen

# Update - Moving the ball by calling the move and other stuff
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)


    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1


        #bounce off left and increase score
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player1.score += 1


        #bounce off right and increase score
        if self.ball.x > self.width - 50:
            self.ball.velocity_x *= -1
            self.player2.score += 1


        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)



    def on_touch_move(self, touch):
        if touch.x < self.width / 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y
    
       

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


PongApp().run()