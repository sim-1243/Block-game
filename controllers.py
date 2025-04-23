import pygame
class Pro_controller():
    def __init__(self,joystick_id):
        self.id=joystick_id
        self.joystick=pygame.joystick.Joystick(self.id)
        self.x_axe=self.joystick.get_axis(0)
        self.y_axe=self.joystick.get_axis(1)
        self.B=self.joystick.get_button(0)
        self.A=self.joystick.get_button(1)
        self.X=self.joystick.get_button(2)
        self.Y=self.joystick.get_button(3)
        self.l=self.joystick.get_button(5)
        self.Zl=self.joystick.get_button(7)
        self.r= self.joystick.get_button(6)
        self.Zr=self.joystick.get_button(8)
        self.plus=self.joystick.get_button(10)
        self.minus=self.joystick.get_button(9)
        self.home=self.joystick.get_button(11)
        self.left_stick=self.joystick.get_button(12)
        self.right_stick=self.joystick.get_button(13)
        self.capture=self.joystick.get_button(4)
        self.Dpad_y=self.joystick.get_hat(0)[0]
        self.Dpad_x=self.joystick.get_hat(0)[1]
    def get_state(self):
        self.joystick=pygame.joystick.Joystick(self.id)
        self.x_axe=self.joystick.get_axis(0)
        self.y_axe=self.joystick.get_axis(1)
        self.B=self.joystick.get_button(0)
        self.A=self.joystick.get_button(1)
        self.X=self.joystick.get_button(2)
        self.Y=self.joystick.get_button(3)
        self.l=self.joystick.get_button(5)
        self.Zl=self.joystick.get_button(7)
        self.r= self.joystick.get_button(6)
        self.Zr=self.joystick.get_button(8)
        self.plus=self.joystick.get_button(10)
        self.minus=self.joystick.get_button(9)
        self.home=self.joystick.get_button(11)
        self.left_stick=self.joystick.get_button(12)
        self.right_stick=self.joystick.get_button(13)
        self.capture=self.joystick.get_button(4)
        self.Dpad_y=self.joystick.get_hat(0)[0]
        self.Dpad_x=self.joystick.get_hat(0)[1]

class PdP_switch_controller():
    def __init__(self,joystick_id):
        self.id=joystick_id
        self.joystick=pygame.joystick.Joystick(self.id)
        self.x_axe=self.joystick.get_axis(0)
        self.y_axe=self.joystick.get_axis(1)
        self.B=self.joystick.get_button(0)
        self.A=self.joystick.get_button(1)
        self.X=self.joystick.get_button(3)
        self.Y=self.joystick.get_button(2)
        self.l=self.joystick.get_button(4)
        self.Zl=self.joystick.get_button(6)
        self.r= self.joystick.get_button(5)
        self.Zr=self.joystick.get_button(7)
        self.plus=self.joystick.get_button(9)
        self.minus=self.joystick.get_button(8)
        self.home=self.joystick.get_button(12)
        self.left_stick=self.joystick.get_button(10)
        self.right_stick=self.joystick.get_button(11)
        self.capture=self.joystick.get_button(13)
        self.Dpad_y=self.joystick.get_hat(0)[0]
        self.Dpad_x=self.joystick.get_hat(0)[1]
    def get_state(self):
        self.joystick=pygame.joystick.Joystick(self.id)
        self.x_axe=self.joystick.get_axis(0)
        self.y_axe=self.joystick.get_axis(1)
        self.B=self.joystick.get_button(0)
        self.A=self.joystick.get_button(1)
        self.X=self.joystick.get_button(3)
        self.Y=self.joystick.get_button(2)
        self.l=self.joystick.get_button(4)
        self.Zl=self.joystick.get_button(6)
        self.r= self.joystick.get_button(5)
        self.Zr=self.joystick.get_button(7)
        self.plus=self.joystick.get_button(9)
        self.minus=self.joystick.get_button(8)
        self.home=self.joystick.get_button(12)
        self.left_stick=self.joystick.get_button(10)
        self.right_stick=self.joystick.get_button(11)
        self.capture=self.joystick.get_button(13)
        self.Dpad_y=self.joystick.get_hat(0)[0]
        self.Dpad_x=self.joystick.get_hat(0)[1]
