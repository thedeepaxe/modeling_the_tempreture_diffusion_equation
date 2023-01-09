from cmath import sqrt
from tkinter import CENTER, Grid
from tracemalloc import start
from turtle import down
from manim import *
class introduction (Scene):
    def construct(self):
        supcom = ImageMobject('SUPCOM.png').move_to([0,-3,0])
        name = Tex("Feki Karim")
        ocupation= Tex("Supcom student").move_to([0,-2,0])
        self.play (FadeIn(name),run_time=3)
        self.play (FadeIn(ocupation),run_time=3)
        self.play (FadeIn(supcom),run_time=3)
        self.play(FadeOut(name,ocupation),supcom.animate.move_to([4,3,0]).scale(0.4),run_time=3)
        manim = ImageMobject('manim.png').move_to([-2,-1,0]).scale(0.6)
        self.play(FadeIn(manim),run_time=6)
        self.wait()
        self.play(manim.animate.scale(0.6).move_to([-3,-1,0]),run_time=1.5)
        self.wait(10)

class firstScene (Scene):
    def construct(self):
        obj= Square(side_length=2,fill_color=BLUE,fill_opacity=1,stroke_color=BLUE)
        grid=NumberPlane().set_opacity(0.2).set_color(GREEN)           
        self.play(Create(grid),run_time=(3))
        self.wait(1)
        self.play(FadeIn(obj))
        self.wait(2)
        arrows=[]
        arrows.append(Arrow(stroke_width=2).next_to(obj,LEFT))
        arrows.append(Arrow(stroke_width=2,start=RIGHT,end=LEFT).next_to(obj,RIGHT))
        arrows.append(Arrow(stroke_width=2,start=UP,end=DOWN).next_to(obj,UP))
        arrows.append(Arrow(stroke_width=2,start=DOWN,end=UP).next_to(obj,DOWN))
        arrows.append(Tex("HEAT : f").next_to(arrows[1],RIGHT+UP))
        self.play(FadeIn(*arrows),run_time=4)
        self.play(obj.animate.set_color(RED_A).set_fill_color(RED_A),run_time=4)
        lilsquare = Square(side_length=0.2,fill_color=RED,stroke_color=RED,fill_opacity=1).move_to([-0.5,-0.5,0])
        
        work= lilsquare.copy()
        condition= [Tex("given f",color=BLUE).move_to([-3.5,-1,0])]
        condition.append(Tex("initial metal tempreture T0",color=BLUE).next_to(condition[0],DOWN))
        condition.append(Tex("given the point coordinates",color=BLUE).next_to(condition[1],DOWN))
        self.play(FadeIn(*condition),run_time=3)
        self.play(FadeIn(lilsquare))
        problem = Tex("T"," ","=  ?").move_to([3,-2,0])
        self.play(FadeIn(problem),work.animate.move_to(problem[0].get_center()+RIGHT*0.25+DOWN*0.2).scale(0.3),run_time=3)




        self.wait(12)












class secondScene (Scene):
    def construct(self):
        equation=MathTex("\\frac{\partial T}{\partial t}", "-","\\nabla . (\\lambda \\nabla T) ","+","  \\nu . \\nabla T", "="," f ",color=GREEN_A)
        b,t=[],[None]*6
        for i in range (4):
            if i %2 ==0 :
                b.append (Brace(equation[i*2],DOWN))
            else:
                b.append (Brace(equation[i*2],UP))
        t[0]=b[0].get_text("tempreture variation over time")
        t[1]=b[1].get_text("tempreture diffused from the object")
        t[2]=b[2].get_text("convection")
        t[3]=b[3].get_text("the heat source")
        dev1 = MathTex("0= \\frac{\partial}{\partial x}\left(k \\frac{\partial T}{\partial x}\\right)+r").move_to([0,1,0])
        self.play(Write(equation),run_time= 6)
        self.wait(7)
        for i in range (4):
            self.play(equation[i*2].animate.set_color(RED),FadeIn(b[i]),FadeIn(t[i]))
            self.wait(2)
            self.play(equation[i*2].animate.set_color(GREEN),FadeOut(b[i]),FadeOut(t[i]))
        self.play (equation.animate.move_to(UP*2))
        heateq=Tex("Heat Equation",color=GREEN_C).next_to(equation,UP)
        self.play(equation.animate.scale(1.4),FadeIn(heateq))
        workterm = equation[0].copy()
        self.play(workterm.animate.move_to([-3,-1,0]))
        self.play(FadeIn(t[0].next_to(workterm,UP)))
        explanation=["after a certaint t=t0 \n f = cst","Nature of the material: \n $\\nu . \\nabla T  \\approx$ 0","if $\\lambda$ = cst"]
        explain=Tex(explanation[0]).move_to([3,-1,0])
        #explaining first term
        self.play(FadeIn(explain))
        self.wait()
        result=MathTex("\\frac{\partial T}{\partial t} = 0",color=GREEN).move_to(workterm.get_center()).scale(1.4)
        self.wait(1)
        self.play(ReplacementTransform(workterm,result))
        explainout=VGroup(explain,t[0])
        self.wait(3)
        self.play(result.animate.move_to([0,-1,0]),FadeOut(explainout),run_time=3)
        cross=Cross(equation[0])
        cross.set_color(RED)
        self.play(Create(cross),run_time=0.5)
        self.play(FadeOut(cross,result,equation[0]))
        workterm=equation[4].copy()
        self.play(workterm.animate.move_to([-3,-1,0]))
        self.play(FadeIn(t[2].next_to(workterm,UP)))
        explain=Tex(explanation[1]).move_to([3,-1,0])
        self.play(FadeIn(explain))
        cross= Cross(equation[4])
        self.play(Create(cross))
        self.play(FadeOut(cross,explain,workterm,t[2],equation[4]))
        new_equation=MathTex("-","\\nabla . (\\lambda \\nabla T) ", "="," f ",color=GREEN).scale(1.4)
        old_equation=VGroup(equation[1],equation[2],equation[3],equation[5],equation[6])
        self.play(TransformMatchingShapes(old_equation,new_equation),FadeOut(heateq),run_time=2)
        self.wait(5)
        old_equation=new_equation
        new_equation=MathTex("-","\\lambda \\Delta T   ", "="," f ",color=GREEN).scale(1.4)
        explain=Tex(explanation[2]).next_to(old_equation,UP,buff=3)
        self.play(FadeIn(explain))
        self.play(TransformMatchingShapes(old_equation,new_equation),FadeOut(explain),run_time=6)
        self.wait(8)
        

        self.wait(2)


class thirdScene (Scene):
    def construct(self):
        d3=MathTex("3D",color=RED).scale(2).move_to([-4,3,0])
        d1=MathTex("1D",color=RED).scale(2).move_to([4,3,0])
        obj3d = Cube(side_length=2,stroke_color=BLUE,fill_color=BLUE,fill_opacity=1).move_to([-4,0,0])
        eq3d = MathTex("-","\\lambda \\Delta T   ", "="," f ").scale(1.4).move_to([-4,-2,0])
        cor3d = MathTex("(x,y,z)").move_to([-4,2,0])
        arrows = []
        arrows.append(Arrow(start=LEFT,end=RIGHT).move_to(cor3d.get_center()+RIGHT*5))
        arrows.append(Arrow(start=LEFT,end=RIGHT).next_to(obj3d.get_center()+RIGHT*4))
        arrows.append(Arrow(start=LEFT,end=RIGHT).next_to(eq3d.get_center()+RIGHT*4))
        cor1d = MathTex("x").move_to([4,2,0])
        obj1d = Line(stroke_color=BLUE,fill_color=BLUE,fill_opacity=1).move_to([4,0,0])
        eq1d = MathTex("\\frac{\\partial^2}{\\partial x^2} T(x) =", "-\\frac{f}{\\lambda} ").scale(1.4).move_to([4,-2,0])
        self.wait(2)
        self.play(FadeIn(d3))
        self.wait()
        self.play(FadeIn(d1))
        self.play(Create(cor3d),run_time=2)
        self.play(GrowFromCenter(obj3d))
        self.play(Create(eq3d))
        self.play(FadeIn(arrows[0]))
        self.play(Create(cor1d),run_time=1)
        self.play(FadeIn(arrows[1]))
        self.play(Create(obj1d),run_time=1)
        self.play(FadeIn(arrows[2]))
        self.wait()
        self.play(Create(eq1d),run_time=1.5)
        self.wait(2)
        self.play(FadeOut(eq1d,d1,d3,*arrows,cor1d,obj3d,cor3d,eq3d),obj1d.animate.move_to([0,3,0]).set_length(7),run_time=2)
        

        linedot= Dot(color=RED_C).move_to(obj1d.get_start())
        self.play(Create(linedot))
        self.wait(2)
        self.play(linedot.animate.move_to(obj1d.get_end()),run_time=4)
        self.wait(2)
        self.play(linedot.animate.move_to((obj1d.get_end()+obj1d.get_start())/2),run_time=3)
        Tx=Tex("T(x)").next_to(linedot,DOWN).scale(0.6)
        linedoth1=Dot(color=RED_C).move_to(obj1d.get_center()+RIGHT)
        linedoth2=Dot(color=RED_C).move_to(obj1d.get_center()+LEFT)
        Txh1=MathTex("T(x+h)").next_to(linedoth1,DOWN).scale(0.6)
        Txh2=MathTex("T(x-h)").next_to(linedoth2,DOWN).scale(0.6)
        self.play(FadeIn(Tx),run_time=4)
        taylor1=MathTex("T(x+h)","=T(x)","+h \\frac{\\partial T}{\\partial x}","+\\frac{1}{2} h^2 \\frac{\\partial^2 T}{\\partial x^2}","+o(h^2)")
        taylor2=MathTex("T(x-h)","=T(x)","-h \\frac{\\partial T}{\\partial x}","+\\frac{1}{2} h^2 \\frac{\\partial^2 T}{\\partial x^2}","+o(h^2)").next_to(taylor1,DOWN)
        self.wait(3)
        self.play(FadeIn(Txh1,linedoth1),run_time=3)
        self.play(TransformMatchingShapes(Txh1.copy(),taylor1[0]),run_time=3)
        self.wait(2)
        self.play(Write(taylor1[1:]),run_time=3)
        
        self.play(FadeIn(Txh2,linedoth2),run_time=3)
        self.play(TransformMatchingShapes(Txh2.copy(),taylor2[0]),run_time=3)
        self.wait()
        self.play(Write(taylor2[1:]),run_time=2)
        self.wait(2)
        finaleq= MathTex("T(x+h)","+","T(x-h)","=2T(x)","+","h^2 \\frac{\\partial^2 T}{\\partial x^2}","+o(h^2)").next_to(taylor2,DOWN)
        self.play(TransformMatchingShapes(taylor1[0],finaleq[:3]),TransformMatchingShapes(taylor2[0],finaleq[:3]))
        self.play(TransformMatchingShapes(taylor1[1],finaleq[3]),TransformMatchingShapes(taylor2[1],finaleq[3]))
        self.play(TransformMatchingShapes(taylor1[3],finaleq[4:6]),TransformMatchingShapes(taylor2[3],finaleq[4:6]),TransformMatchingShapes(taylor2[4].copy(),finaleq[6]))
        self.wait()
        self.play(FadeOut(taylor1[2],taylor1[4],taylor2[2],taylor2[4]),finaleq.animate.move_to([0,0,0]))
        self.wait()
        finaleqdev1=  MathTex("\\frac{T(x+h)+T(x-h)-2T(x)}{h^2}","="," \\frac{\\partial^2 T}{\\partial x^2}","+o(h^2)")
        self.play(TransformMatchingShapes(finaleq,finaleqdev1))
        develop = dict()
        develop['oldeq'] = eq1d.move_to([0,-2,0])
        develop['N'] = MathTex("lets \\, consider \\, N ","\\in \\, \\mathbb{N}").move_to([-3,-2,0])
        develop['L'] =MathTex("L\\,  the \\, length \\, of \\, the \\,  stem").move_to([-3,-3,0])
        develop['h'] = MathTex('h = \\frac{L}{N}').move_to([3,-2,0])
        develop['new_equation'] =MathTex("\\frac{T(x+h)+T(x-h)-2T(x)}{h^2}","="," -\\frac{f}{\\lambda}","+o(h^2)")
        self.play(FadeIn(develop['oldeq']),run_time=2)
        self.wait(2)
        self.play(TransformMatchingShapes(develop["oldeq"][1].copy(),develop["new_equation"][2]),TransformMatchingShapes(finaleqdev1,develop["new_equation"]))
        self.play(FadeOut(develop["oldeq"]))
        self.wait()
        self.play(FadeIn(develop["N"]),FadeIn(develop["h"]),FadeIn(develop["L"]),run_time=2)
        self.wait()
        develop['new_equation2'] =MathTex("\\frac{T(x+\\frac{L}{N})+T(x-\\frac{L}{N})-2T(x)}{(\\frac{L}{N})^2}","="," -\\frac{f}{\\lambda}","+o((\\frac{L}{N})^2)")       
        self.play(TransformMatchingShapes(develop['new_equation'],develop['new_equation2']))
        self.wait(2)
        self.play(FadeOut(develop["N"]),FadeOut(develop["h"]),FadeOut(develop["L"]),run_time=1)
        develop['neglect']= MathTex("If\\, \\, N >>1 \\,\\,  ","then \\, \\, o((\\frac {L}{N})^2)\\, \\, <<1").move_to([0,-2,0])
        develop['new_equation3'] =MathTex("\\frac{T(x+\\frac {L}{N})+T(x-\\frac {L}{N})-2T(x)}{(\\frac {L}{N})^2}","="," -\\frac{f}{\\lambda}")
        self.play(FadeIn(develop["neglect"]))
        self.play(TransformMatchingShapes(develop["new_equation2"],develop["new_equation3"]))
        self.wait(2)
        self.play(FadeOut(develop["neglect"],develop["new_equation3"],Tx,Txh1,Txh2,linedot,linedoth1,linedoth2))
        point_list=VGroup()
        l= abs(obj1d.get_start()[0]-obj1d.get_end()[0])
        def add_points(n,point_list):
            time= 2/n
            if len(point_list)!= 0:
                old_point_list= point_list
               
                new_point_list =VGroup(*[Dot(color=RED_C).move_to(obj1d.get_start()+RIGHT*l*i/(n-1)).scale(sqrt(10/n)) for i in range(n)])
                self.play(ReplacementTransform(old_point_list,new_point_list),run_time=time)
            else:
                new_point_list =VGroup(*[Dot(color=RED_C).move_to(obj1d.get_start()+RIGHT*l*i/(n-1)).scale(sqrt(10/n))  for i in range(n)])
                self.play(FadeIn(new_point_list),run_time=time)
            return new_point_list
        nvalue=MathTex("n = \\,").move_to([0,-2,0])
        self.add(nvalue)
        for i in range (2,20):
            n=MathTex(i).next_to(nvalue,RIGHT)
            self.play(FadeIn(n),run_time=0.2)
            point_list=add_points(i,point_list)
            self.play(FadeOut(n),run_time=0.1)
        self.play(FadeOut(nvalue),run_time=0.2)
        self.wait(2)
        xdiscret= MathTex("so if \\,  x = \\frac {k.L}{N}\\,  where\\,  k \\, \\in \\, \\{1..N-1\\}")
        self.play (FadeIn(xdiscret))
        self.wait(2)
        self.play(xdiscret.animate.move_to([0,2,0]))
        self.play(FadeIn(develop["new_equation3"]))
        self.wait(2)
        develop["new_equation4"] = MathTex("\\frac{T(\\frac {k.L}{N}+\\frac {L}{N})+T(\\frac {k.L}{N}-\\frac {L}{N})-2T(\\frac {k.L}{N})}{(\\frac {L}{N})^2}","="," -\\frac{f}{\\lambda}").move_to([0,-2,0])
        self.play(TransformMatchingShapes(develop["new_equation3"],develop["new_equation4"]))
        self.wait(2)
        develop["T"]= MathTex(" considering \\,T(\\frac {k.L}{N}) = T_k ").move_to([0,-3,0])
        develop["new_equation5"] = MathTex("\\frac{T_{k+1}+T_{k-1}-2.T_k}{(\\frac {L}{N})^2}","="," -\\frac{f}{\\lambda}")
        self.play(FadeIn(develop["T"]))
        self.wait(2)
        self.play(TransformMatchingShapes(develop["new_equation4"],develop["new_equation5"]))
        remember =MathTex("k \\, \\in \\, \\{1..N-1\\}").move_to([-3,-1,0])
        nbreq = MathTex("we\\, will\\, have\\, a \\,system\\, of\\, N-1 \\,equations ").move_to([3,-1,0])
        self.play(FadeIn(remember),run_time=2)
        self.wait(3)
        self.play(FadeIn(nbreq),run_time=2)
        
        self.wait(5)