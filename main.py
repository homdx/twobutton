from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.text import Label as CoreLabel

class MyApp(App):
    def build(self):

        fl = FloatLayout(size = (300,300))
        fl.add_widget(Button(
            text = "This is first button",
            font_size = 16,
            on_press = self.btn_press1,
            background_color = [1, 0, 0, 1],
            background_normal = '',
            size_hint = (.5, .25),
            pos = (0, 10)));

        fl.add_widget(Button(
            text = "This is second button",
            font_size = 16,
            on_press = self.btn_press2,
            background_color = [1, 0, 0, 1],
            background_normal = '',
            size_hint = (.5, .25),
            pos = (0, 150)));


        return fl

    def btn_press1(self, instance):
        print('Button one pressed')
        instance.text = 'Button one pressed'

    def btn_press2(self, instance):
        print('Button second pressed')
        instance.text = 'Button second pressed'

if __name__ == "__main__":
    MyApp().run()
