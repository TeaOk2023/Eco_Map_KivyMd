from kivy.uix.gridlayout import GridLayout
from kivy_garden.mapview import MapView, MapMarker
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

Window.size = (450, 600)


class CustomMapMarker(MapMarker):
    def __init__(self, **kwargs):
        super(CustomMapMarker, self).__init__(**kwargs)
        self.source = 'assests/Trash2.png'
        self.size = (35, 35)
        self.on_press = self.show_popup

    def show_popup(self, *args):
        MDDialog(
            title="Ситиматик",
            type="simple",
            text="Тип принимаемого мусора: перерабатываемый, кроме твердых бытовых отходов.                     "
                 "Время работы: 08:00 - 17:00",  #Сюда кидай

        ).open()


class Marker2(MapMarker):
    def __init__(self, **kwargs):
        super(Marker2, self).__init__(**kwargs)
        self.source = 'assests/Niga2.png'
        self.size = (40, 40)
        self.on_press = self.show_popup

    def show_popup(self, *args):
        MDDialog(
            title="Привет!",
            type="simple",
            text="Вы находитесь здесь!",
        ).open()


class Marker3(MapMarker):
    def __init__(self, **kwargs):
        super(Marker3, self).__init__(**kwargs)
        self.source = 'assests/event.png'
        self.size = (50, 50)
        self.on_press = self.show_popup

    def show_popup(self, *args):
        MDDialog(
            title="Суботник",
            type="simple",
            text="Субботник - ждем всех желающих).                                "
                 "Время проведения: 08:00 - 11:00  17 мая",

        ).open()


class MyMap(GridLayout):
    def __init__(self, **kwargs):
        super(MyMap, self).__init__(**kwargs)
        self.cols = 1

        mapview = MapView(zoom=14, lat=56.14521, lon=47.22043)

        marker = CustomMapMarker(lat=56.13663, lon=47.15180)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.1192, lon=47.1878)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.1384, lon=47.2751)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.14415, lon=47.21716)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.13735, lon=47.27744)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.1467, lon=47.2021)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.13689, lon=47.15166)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.1064, lon=47.3058)
        mapview.add_marker(marker)

        marker = CustomMapMarker(lat=56.1291, lon=47.3167)
        mapview.add_marker(marker)

        #событие на карте
        marker = Marker3(lat=56.13648, lon=47.28726)
        mapview.add_marker(marker)

        marker = Marker3(lat=56.14552, lon=47.21117)
        mapview.add_marker(marker)
        # Ты на карте
        marker = Marker2(lat=56.14521, lon=47.22043)
        mapview.add_marker(marker)
        self.add_widget(mapview)


class EcoCity(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        Builder.load_file("bot_nav.kv")

        return MDBottomNavigation()

    def send_message(self):
        message_text = self.ids.message_input.text
        print(message_text)
        if message_text:
            message_label = MDLabel(text=message_text)
            self.ids.message_display.add_widget(message_label)
            self.ids.message_input.text = ''  # Clear input field after sending


if __name__ == '__main__':
    EcoCity().run()
