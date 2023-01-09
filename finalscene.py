from tkinter import Image
from manim import *

class scene3(Scene):
    def construct(self):
        credits_text1 = Tex("resources"," reference").move_to([0,3,0])
        credits_text2 = Tex("Find"," it"," in"," the ","description").move_to([0,-4,0])
        credits_pic = ImageMobject("finalproduct/saada.png").scale(0.7)
        self.play(FadeIn(credits_pic))
        self.wait(2)
        self.play(FadeIn(credits_text1),FadeIn(credits_text2))
        self.wait(3)
        self.play(FadeOut(credits_pic),FadeOut(credits_text1),FadeOut(credits_text2))
        thanls =Tex("thank"," you"," for ","Watching")
        self.play(FadeIn(thanls))
        self.wait(2)
        self.play(FadeOut(thanls))