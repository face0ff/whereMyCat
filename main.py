
# -*- coding: utf-8 -*-
import kivy
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


Builder.load_file(os.path.join ("my.kv"))


Window.fullScreen = True
	
		
		



class MenuScreen(Screen):
	
	pass
	



	

	

sm.add_widget(MenuScreen(name='menu'))


class TestApp(App):
	

	
	def build(self):
		
		return sm
if __name__ == '__main__':
	TestApp().run()

