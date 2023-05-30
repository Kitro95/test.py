from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    def create_button(self, text):
        # создание кнопки
        button = Button(text=text)
        button.bind(on_press=self.button_pressed)
        self.add_widget(button)

    def button_pressed(self, instance):
        print(f"Кнопка {instance.text} была нажата")


class MyApp(App):
    def build(self):
        # создание главного экрана приложения
        boxlayout = MyBoxLayout()
        boxlayout.create_button('Кнопка 1')
        boxlayout.create_button('Кнопка 2')
        boxlayout.create_button('Кнопка 3')
        return boxlayout


if __name__ == '__main__':
    MyApp().run()