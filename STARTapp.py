from kivy.app import App
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class ScrollApp(App):
    def build(self):
        # создать ScrollView
        scroll_view = ScrollView(size_hint=(1, None),
                                 size=(Window.size[0], Window.size[1]))

        # создать Label и добавить его в ScrollView
        label = Label(text="Привет Денис")

        scroll_view.add_widget(label)
        return scroll_view


scroll = ScrollApp()
scroll.run()