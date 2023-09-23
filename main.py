from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.camera import Camera


class Header(Widget):
    pass


class OpenCamera(Camera):
    pass


class CrackContainer(ScreenManager):
    pass


class CrackContainer1(Screen):
    pass


class CrackContainer2(Screen):
    start_cam = ObjectProperty(None)
    close_cam = ObjectProperty(None)

    def capture(self):
        camera = self.ids["camera"]
        camera.export_to_png("picture.png")
        print("Captured")


class CrackApp(App):
    def build(self):
        # Initialize container for whole app
        sm = ScreenManager(transition=NoTransition())
        screen1 = CrackContainer1(name="first")
        screen2 = CrackContainer2(name="second")

        sm.add_widget(screen1)
        sm.add_widget(screen2)

        return sm


if __name__ == "__main__":
    CrackApp().run()
