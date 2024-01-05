def activate(self):
    "Sets this button to 'active' . "
    self.label.setFill('black')
    self.rect.setWidth(2)
    self.active = True


def deactivate(self, win=None, button1=None, button2=None, button3=None):
    "Sets this button to 'inactive' . "
    self.label.setFill('darkgrey')
    self.rect.setWidth(1)
    self.active = False

    pt = win.getMouse()
    if button1.clicked(pt):
        # Do button! stuff
    elif button2.clicked(pt):
        # Do button2 stuff
    elif button3.clicked(pt):



# Do button3 stuff

def clicked(self, p):
    "Returns true if button is active and p is inside"
    return (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)
