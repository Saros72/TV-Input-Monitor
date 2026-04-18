import os
import time
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

from jnius import autoclass
from android.runnable import run_on_ui_thread

# 🔥 ANDROID TOAST
Toast = autoclass('android.widget.Toast')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
String = autoclass('java.lang.String')


@run_on_ui_thread
def android_toast(text):
    context = PythonActivity.mActivity
    jtext = String(text)
    Toast.makeText(context, jtext, Toast.LENGTH_SHORT).show()


class InputMonitorApp(App):
    def build(self):

        self.label = Label(
            text="MONITOR ACTIVE\nPress remote buttons...",
            font_size='25sp',
            halign='center',
            markup=True
        )

        self.last_back = 0

        # INPUT BINDING
        Window.bind(on_key_down=self._on_key_down)
        Window.bind(on_key_up=self._on_key_up)

        Window.bind(on_joy_button_down=self._on_joy_button_down)
        Window.bind(on_joy_hat=self._on_joy_hat)
        Window.bind(on_joy_axis=self._on_joy_axis)

        return self.label

    # -----------------------
    # KEY DOWN
    # -----------------------
    def _on_key_down(self, window, key, scancode, codepoint, modifiers):

        info = (
            f"TYPE: [color=00ff00]KEY DOWN[/color]\n"
            f"KEY: [b]{key}[/b]\n"
            f"SCANCODE: {scancode}"
        )

        print(f"DEBUG KEY DOWN: {key} / {scancode}")
        self.label.text = info

        # BACK nepouštíme systému
        if key in (27, 4, 1001):
            return True

        return False

    # -----------------------
    # KEY UP
    # -----------------------
    def _on_key_up(self, window, key, scancode):

        print(f"DEBUG KEY UP: {key} / {scancode}")

        # 🔙 BACK (mobile + Android TV)
        if key in (27, 1001):

            now = time.time()

            if now - self.last_back < 2:
                App.get_running_app().stop()
            else:
                self.last_back = now
                android_toast("Tap again to close the app")

            return True

        info = (
            f"TYPE: [color=00aa00]KEY UP[/color]\n"
            f"KEY: [b]{key}[/b]\n"
            f"SCANCODE: {scancode}"
        )

        self.label.text = info
        return True

    # -----------------------
    # JOY BUTTON
    # -----------------------
    def _on_joy_button_down(self, window, stick_id, button_id):

        print(f"DEBUG JOY BUTTON: {button_id}")

        # 🔙 BACK (TV / gamepad)
        if button_id == 4:
            now = time.time()

            if now - self.last_back < 2:
                App.get_running_app().stop()
            else:
                self.last_back = now
                android_toast("Tap again to close the app")

            return True

        info = (
            f"TYPE: [color=00ffff]JOY BUTTON[/color]\n"
            f"ID: [b]{button_id}[/b]\n"
            f"STICK: {stick_id}"
        )

        self.label.text = info
        return True

    # -----------------------
    # JOY HAT (DPAD)
    # -----------------------
    def _on_joy_hat(self, window, stick_id, hat_id, value):

        print(f"DEBUG JOY HAT: {value}")

        info = (
            f"TYPE: [color=ffff00]JOY HAT[/color]\n"
            f"HAT ID: {hat_id}\n"
            f"VALUE: {value}"
        )

        self.label.text = info
        return True

    # -----------------------
    # JOY AXIS
    # -----------------------
    def _on_joy_axis(self, window, stick_id, axis_id, value):

        print(f"DEBUG JOY AXIS: {axis_id} / {value}")

        info = (
            f"TYPE: [color=ff8800]JOY AXIS[/color]\n"
            f"AXIS: {axis_id}\n"
            f"VALUE: {value:.2f}"
        )

        self.label.text = info
        return True


if __name__ == '__main__':
    print("--- STARTING INPUT MONITOR ---")
    InputMonitorApp().run()