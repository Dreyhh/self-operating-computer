import pyautogui
import platform
import time
import math

from operate.utils.misc import convert_percent_to_decimal


class OperatingSystem:
    def write(self, content):
        try:
            content = content.replace("\\n", "\n")
            for char in content:
                pyautogui.write(char)
        except Exception as e:
            print("[OperatingSystem][write] error:", e)

    def press(self, keys):
        try:
            is_shift = False
            for key in keys:
                pyautogui.keyDown(key)
            time.sleep(0.1)
            for key in keys:
                if key == "shift":
                    is_shift = True
                    continue
                pyautogui.keyUp(key)
            if is_shift:
                time.sleep(0.1)
                pyautogui.keyUp("shift")
        except Exception as e:
            print("[OperatingSystem][press] error:", e)

    def mouse(self, click_detail):
        return None
        

    def click_at_percentage(
        self,
        x_percentage,
        y_percentage,
        duration=0.2,
        circle_radius=50,
        circle_duration=0.5,
    ):
        try:
            screen_width, screen_height = pyautogui.size()
            x_pixel = int(screen_width * float(x_percentage))
            y_pixel = int(screen_height * float(y_percentage))

            pyautogui.moveTo(x_pixel, y_pixel, duration=duration)

            start_time = time.time()
            while time.time() - start_time < circle_duration:
                angle = ((time.time() - start_time) / circle_duration) * 2 * math.pi
                x = x_pixel + math.cos(angle) * circle_radius
                y = y_pixel + math.sin(angle) * circle_radius
                pyautogui.moveTo(x, y, duration=0.1)

            pyautogui.click(x_pixel, y_pixel)
        except Exception as e:
            print("[OperatingSystem][click_at_percentage] error:", e)
