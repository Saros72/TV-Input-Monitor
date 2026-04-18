import os
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label


class InputMonitorApp(App):
    def build(self):
        # Main screen label
        self.label = Label(
            text="MONITOR ACTIVE\nPress remote buttons...",
            font_size='25sp',
            halign='center',
            markup=True
        )

        # 📌 INPUT BINDING
        Window.bind(on_key_down=self._on_key_down)
        Window.bind(on_key_up=self._on_key_up)

        Window.bind(on_joy_button_down=self._on_joy_button_down)
        Window.bind(on_joy_hat=self._on_joy_hat)
        Window.bind(on_joy_axis=self._on_joy_axis)

        return self.label

    # -----------------------
    # KEYBOARD / REMOTE
    # -----------------------
    def _on_key_down(self, window, key, scancode, codepoint, modifiers):
        info = (
            f"TYPE: [color=00ff00]KEY DOWN[/color]\n"
            f"KEY: [b]{key}[/b]\n"
            f"SCANCODE: {scancode}"
        )

        print(f"DEBUG KEY DOWN: {key} / {scancode}")
        self.label.text = info
        return True

    def _on_key_up(self, window, key, scancode):
        info = (
            f"TYPE: [color=00aa00]KEY UP[/color]\n"
            f"KEY: [b]{key}[/b]\n"
            f"SCANCODE: {scancode}"
        )

        print(f"DEBUG KEY UP: {key} / {scancode}")
        self.label.text = info
        return True

    # -----------------------
    # JOYSTICK BUTTONS
    # -----------------------
    def _on_joy_button_down(self, window, stick_id, button_id):
        info = (
            f"TYPE: [color=00ffff]JOY BUTTON[/color]\n"
            f"ID: [b]{button_id}[/b]\n"
            f"STICK: {stick_id}"
        )

        print(f"DEBUG JOY BUTTON: {button_id} / stick {stick_id}")
        self.label.text = info
        return True

    # -----------------------
    # JOY HAT (DPAD)
    # -----------------------
    def _on_joy_hat(self, window, stick_id, hat_id, value):
        info = (
            f"TYPE: [color=ffff00]JOY HAT[/color]\n"
            f"HAT ID: {hat_id}\n"
            f"VALUE: {value}"
        )

        print(f"DEBUG JOY HAT: {hat_id} / {value}")
        self.label.text = info
        return True

    # -----------------------
    # JOY AXIS
    # -----------------------
    def _on_joy_axis(self, window, stick_id, axis_id, value):
        info = (
            f"TYPE: [color=ff8800]JOY AXIS[/color]\n"
            f"AXIS: {axis_id}\n"
            f"VALUE: {value:.2f}"
        )

        print(f"DEBUG JOY AXIS: axis {axis_id} / value {value}")
        self.label.text = info
        return True


if __name__ == '__main__':
    print("--- STARTING INPUT MONITOR ---")
    InputMonitorApp().run()
