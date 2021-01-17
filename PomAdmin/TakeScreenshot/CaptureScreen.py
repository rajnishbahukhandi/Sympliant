import pyautogui


class capture():
    def captureInvalidEMailAddress():
        screenshot1 = pyautogui.screenshot()
        screenshot1.save(r'/Users/ray.rajnish/PycharmProjects/SympliantAdmin/PomAdmin/TakeScreenshot/UpdateScreenshots/captureInvalidEMailAddress.png')

    def captureInvalidPassword():
        screenshot2 = pyautogui.screenshot()
        screenshot2.save(r'/Users/ray.rajnish/PycharmProjects/SympliantAdmin/PomAdmin/TakeScreenshot/UpdateScreenshots/captureInvalidPassword.png')

    def captureNullCredentials():
        screenshot3 = pyautogui.screenshot()
        screenshot3.save(r'/Users/ray.rajnish/PycharmProjects/SympliantAdmin/PomAdmin/TakeScreenshot/UpdateScreenshots/captureNullCredentials.png')

    def captureValidCredentials():
        screenshot4 = pyautogui.screenshot()
        screenshot4.save(r'/Users/ray.rajnish/PycharmProjects/SympliantAdmin/PomAdmin/TakeScreenshot/UpdateScreenshots/captureValidCredentials.png')


# def capture():
#     for i in range(4):
#         screenshot1 = pyautogui.screenshot()
#         screenshot1.save(f'screenshot1 {i}.png')