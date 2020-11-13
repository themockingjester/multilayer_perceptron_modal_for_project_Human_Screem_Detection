import datetime

from kivy.uix.checkbox import CheckBox
from kivymd.uix.bottomsheet import MDListBottomSheet
import shutil
import pandas as pd
import pytz
import requests
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivymd.icon_definitions import md_icons
from kivy.clock import Clock
from kivy.graphics.opengl import *
from kivy.graphics import *
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivymd.uix.button import MDFlatButton
from kivy.uix.textinput import TextInput
import threading
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
import os,threading,time
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.behaviors import ButtonBehavior

class ImageButton(ButtonBehavior, Image):
    pass

class MainWindow(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass
class uiApp(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Pink"

        self.theme_cls.theme_style = "Dark"  # "Light"


        self.screen_manager = ScreenManager()
        self.mainscreen = MainWindow()
        screen = Screen(name='mainscreen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)
        return self.screen_manager

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Engine is currently Running!!",
                buttons=[
                    MDFlatButton(
                        text="Ok", text_color=self.theme_cls.primary_color,on_press= lambda x: self.dialog.dismiss(),
                    )
                ],

            )
        self.dialog.open()
if __name__ == '__main__':
    LabelBase.register(name='second',fn_regular='FFF_Tusj.ttf')
    LabelBase.register(name='first',fn_regular='Pacifico.ttf')


    uiApp().run()