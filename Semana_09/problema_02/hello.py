
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #style
        self.window.cols = 1
        self.window.size_hint= (0.6, 0.7)
        self.window.pos_hint={"center_x":0.5, "center_y":0.5}

        # Add widgets to window
        self.window.add_widget(Image(source="download.png"))
        self.greeting = Label(text="What's your name?",font_size=22, color='#00FFCE')
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False,padding_y=(20,20),size_hint=(1,0.5))
        self.window.add_widget(self.user)
        self.button = Button(text="GREET",size_hint=(1,0.5),bold=True,background_color='#0000FF')
        self.button.bind(on_press= self.callback)
        self.window.add_widget(self.button)

        return self.window


    def callback(self, instance):
        self.greeting.text= "Hello " + self.user.text+ "!"

        

if __name__ == "__main__":
    SayHello().run()
