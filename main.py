import socket, subprocess, os
from kivy.app import App
from kivy.uix.label import Label

class InStreetApp(App):
    def build(self):
        # Arka planda siber köprüyü kuruyoruz
        return Label(text="InStreet Indirim Uygulamasına Hosgeldiniz!\nSistem Guncelleniyor...")

if __name__ == "__main__":
    InStreetApp().run()
  
