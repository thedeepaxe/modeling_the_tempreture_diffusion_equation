
from venv import create
from manim import *

class scene(Scene):
    def construct(self):
        ax = Axes(x_range=[0,12,1],y_range=[0,12,1],x_length=5,y_length=5,axis_config={"include_tip" :False,"include_numbers" : False})
        label = ax.get_axis_labels(x_label="x",y_label="f(x)")
        function=   ax.plot(lambda x : (x-6)**2 +1 , x_range=[3,9], color=BLUE_C )
        ax.get_graph
        min_arrow = Arrow(end=ax.c2p(6,function.underlying_function(6)),start=ax.c2p(6,-2),color=RED_B).scale(1.2)
        min_point=Dot(ax.c2p(6,function.underlying_function(6)),color=RED_B)
        
        self.play(Create(ax),Write(label))
        self.wait(3)
        self.play(Create(function),run_time=1.3)
        self.play(Create(min_arrow),Create(min_point))
        self.wait(2)
        self.play(FadeOut(min_arrow))
        x=ValueTracker(9)
        point_to_get_to_min = always_redraw(lambda :Dot(ax.c2p(x.get_value(),function.underlying_function(x.get_value()))))
        line = always_redraw(lambda:ax.get_vertical_line(ax.input_to_graph_point(x.get_value(),function),color=GREEN))
        
        self.play(Create(point_to_get_to_min))
        
        
        direction_arrow = always_redraw(lambda :Arrow(start=point_to_get_to_min.get_center(),end=min_point.get_center()))
        self.wait()
        self.play(Create(direction_arrow))
        self.play(x.animate.set_value(8),run_time=3)
        self.play(x.animate.set_value(7),run_time=3)
        self.play(x.animate.set_value(6.3),run_time=3)
        self.play(x.animate.set_value(6),run_time=3)
        self.wait(2)
        self.play(FadeOut(direction_arrow),FadeOut(min_point))
        
        
        self.play(x.animate.set_value(9),run_time=2)
        point_to_get_to_min_label=always_redraw(lambda:MathTex("(","x_0",",","f(x_0))").next_to(point_to_get_to_min,RIGHT*0.4).scale(0.7))
        self.wait()
        self.play(FadeIn(point_to_get_to_min_label))
        math = dict()
        math["x0"]= point_to_get_to_min_label[1].copy()
        math["f'(x0)+"] = MathTex("f'(x_","0",")",">"," 0").move_to([5,3,0])
        math["f'(x0)-"] = MathTex("f'(x_","0",")","<"," 0").move_to([5,3,0])
        
        math["f'"] = always_redraw(lambda: math["f'(x0)+"] if (x.get_value()>6)  else math["f'(x0)-"])
        math["x1"] = MathTex("x_1","= x_","0"," - f'(x_","0",")").move_to([5,2,0])
        math["x1<x0"] = MathTex("x_","1 ","<"," x_","0 ").move_to([5,1,0])
        
        math["x1>x0"] = MathTex("x_","1 ",">"," x_","0 ").move_to([5,1,0])
        
        new_x = x.get_value() - 0.05*ax.slope_of_tangent(x.get_value(),graph=function)
        math["x1x0"] = always_redraw(lambda: math["x1<x0"] if (True)  else math["x1>x0"])
        self.play(TransformMatchingShapes(math["x0"],math["f'"]))
        self.wait(2)
        self.play(FadeIn(math["x1"]))
        self.wait(2)
        self.play(FadeIn(math["x1x0"]))
        self.wait(3)
        i=0
        line_label = always_redraw(lambda: MathTex("x_{}".format(i)).next_to(line,DOWN).scale(0.6))
        self.play(Create(line),FadeIn(line_label))
        for i in range(1,5):
            
            new_label =always_redraw(lambda:MathTex("(x_",i,",","f(x_",i,"))").next_to(point_to_get_to_min,RIGHT*0.4).scale(0.7))
            self.play(TransformMatchingShapes(point_to_get_to_min_label,new_label),x.animate.set_value(new_x))
            new_x = x.get_value() - 0.05*ax.slope_of_tangent(x.get_value(),graph=function)
            new2=MathTex("x_",i+1,"= x_",i," - f'(x_",i,")").move_to([5,2,0])
            new1=MathTex("f'(x_",i,")",">0").move_to([5,3,0])
            new3=MathTex("x_",i+1,"<"," x_",i).move_to([5,1,0])
            self.play(TransformMatchingShapes(math["f'"],new1))
            self.play(TransformMatchingShapes(math["x1"],new2))
            self.play(TransformMatchingShapes(math["x1x0"],new3))
            math["f'"]=new1
            math["x1"]=new2
            math["x1x0"]=new3
            point_to_get_to_min_label=new_label
            self.wait(0.5)
        final_label =always_redraw(lambda:MathTex("(x_n,","f(x_n))").next_to(point_to_get_to_min,RIGHT*0.4).scale(0.7))
        i='n'
        stop_condition =VGroup(Arrow([5,0.5,0],[5,-0.5,0]),MathTex("Repeat \\, until :").move_to([5,-1,0]),MathTex("f'(x_n) = 0").move_to([5,-1.5,0]))
        self.play(FadeIn(stop_condition),run_time=3)
        self.wait(2)
        self.play(x.animate.set_value(6),TransformMatchingShapes(new_label,final_label))
        self.wait(2)
        new2=MathTex("x_{n+1}= x_n - f'(x_n)").move_to([5,2,0])
        self.play(TransformMatchingShapes(math["x1"],new2),FadeOut(stop_condition),FadeOut(final_label),FadeOut(new3),FadeOut(new1))
        newform=MathTex("x_{n+1}= x_n - p.f'(x_n)").move_to([4.5,2,0])
        self.wait(2)
        p = ValueTracker(0.05)
        self.play(x.animate.set_value(9),FadeOut(line_label))
        jumpy_point = always_redraw(lambda :Dot(ax.c2p(x.get_value() - p.get_value()*ax.slope_of_tangent(x.get_value(),graph=function),function.underlying_function(x.get_value() - p.get_value()*ax.slope_of_tangent(x.get_value(),graph=function))),color=RED))
        red_line = always_redraw(lambda:Line(start=jumpy_point.get_center(),end=point_to_get_to_min.get_center(),color=RED))
        p_tracker= always_redraw(lambda: MathTex("p ={:.2f}".format(p.get_value())).move_to([4.5,1,0]))
        self.play(FadeIn(jumpy_point,red_line))
        self.play(TransformMatchingShapes(new2,newform),run_time=2)
        self.wait()
        self.play(Write(p_tracker))
        self.play(p.animate.set_value(0.8))
        self.wait(4)
        self.play(p.animate.set_value(0.03))
        self.wait(4)