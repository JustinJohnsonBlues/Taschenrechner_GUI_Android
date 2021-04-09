# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:26:06 2021
A VERSITALE CALCULATOR-APP
@author: Leo
leo.michel@physik.uni-hamburg.de
"""
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

import math

# Fenstergröße:
# Window.size = (450,600)

Builder.load_file('maindesing.kv')


class TheGrid(Widget):
    
    def testpress(self):
        data= self.input.text
        print(f'Works! {data}')
        
    def clear(self):
        self.ids.input.text = "0"
    
    def act(self, action):
        tex_old = self.ids.input.text
        if tex_old == "0" or "ERROR" in tex_old:
            tex_old = ""
            self.ids.input.text = f'{action}'
        else:
            self.ids.input.text = f'{tex_old}{action}'

    def dot(self):
        # print("GO")
        tex_old = self.ids.input.text
        if tex_old[len(tex_old)-1].isdecimal():
            # print(tex_old[len(tex_old)-1])
            if len(tex_old) == 1:
                self.ids.input.text = f'{tex_old}.'
            for i in range(len(tex_old)-1, -1, -1):
                # print("GO LOOP")
                # print(f'The I is {str(i)}')
                # print(tex_old[i])
                if i == 0:
                    # print("IS LAST")
                    self.ids.input.text = f'{tex_old}.'
                    break
                if (tex_old[i].isdecimal() == False) and (tex_old[i] != "."):
                    # print("Found OTHER")
                    self.ids.input.text = f'{tex_old}.'
                    break
                if tex_old[i] == ".":
                    # print("Found Dot")
                    break
        else:
            pass

    def remove(self):
        tex_old = self.ids.input.text
        tex_old = tex_old[:-1]
        self.ids.input.text = tex_old

    def equals(self):
        tex = self.ids.input.text
        try:
            sol = eval(tex)
            self.ids.input.text = str(sol)
        except:
            self.ids.input.text = "ERROR"


class TR(App):
    def build(self):
        return TheGrid()


if __name__ == "__main__":
    app = TR()
    app.run()
