# cdieview.py


from dieview import DieView

class ColorDieView(DieView):

    def setValue(self, value):
        self.value = value      # remember this value
        DieView.setValue(self, value) # call setValue from parent class

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

