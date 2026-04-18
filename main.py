from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.behaviors import FocusBehavior
from kivy.core.window import Window
from kivy.clock import Clock

class TVButton(FocusBehavior, Button):
    def on_focus(self, instance, value):
        if value:
            self.background_color = [0.2, 0.6, 1, 1] # Modrá při výběru
        else:
            self.background_color = [1, 1, 1, 1]

class TestApp(App):
    def build(self):
        # Tato řádka je pro TV build klíčová
        Window.focus_behavior = True
        
        self.btn = TVButton(text="TEST FOCUSU", size_hint=(0.5, 0.3), pos_hint={'center_x': .5, 'center_y': .5})
        self.btn.bind(on_release=self.akce)
        
        Clock.schedule_once(self.nastav_focus, 1.0)
        return self.btn

    def nastav_focus(self, dt):
        self.btn.focus = True

    def akce(self, instance):
        instance.text = "FUNGUJE TO V APK!"
        instance.background_color = [0, 1, 0, 1]

if __name__ == '__main__':
    TestApp().run()
