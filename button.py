import pygame


class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, pos, floor, in_or_out, font, screen, onclickFunction=None):
        self.x, self.y = pos

        self.onclickFunction = onclickFunction
        # Pressed or not.
        self.pressed = False

        self.floor = floor

        # Inside of the elevator or not.
        self.in_or_out = in_or_out

        self.width = 40
        self.height = 40

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
 
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(str(floor), True, (20, 20, 20))
        self.screen = screen

    def __str__(self) -> str:
        return f"id, {self.floor}" 

    def process(self):
        self.buttonSurface.fill(self.fillColors['normal'])
        
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)


    def press(self):
        self.pressed = True
        self.buttonSurface.fill(self.fillColors['pressed'])
                
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)

        # add to elevator queue
        
    def unpress(self):
        self.pressed = False
        self.buttonSurface.fill(self.fillColors['normal'])

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.screen.blit(self.buttonSurface, self.buttonRect)