from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<MyActivity@BoxLayout>:
    orientation: 'vertical'

    TextInput:
        id: text_input

    Button:
        text: 'Button 1'
        on_press: app.press_button(self, self.text)

    Button:
        text: 'Button 2'
        on_press: app.press_button(self, self.text)
""")


class MyApp(App):
    def build(self):
        self.activity = Factory.MyActivity()
        return self.activity

    def press_button(self, instance, text):
        # instance.text = 'Я нажата'
        self.activity.ids.text_input.text = self.activity.ids.text_input.text + '%s\n' % text


if __name__ == "__main__":
    MyApp().run()
