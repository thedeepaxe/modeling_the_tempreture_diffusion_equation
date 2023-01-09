from manim import *
from numpy import *

class scene2 (Scene):

    def construct (self):

        self.wait(2)
        function_to_min = MathTex("f(X) = \\frac {1}{2}<AX,X>-<X,B>").move_to([0,-1,0])
        function_to_solve = MathTex("AX=B").move_to([0,1,0])
        final_function_to_solve= MathTex("AX-B=0_n").move_to([0,1,0])
        function_to_min_der= MathTex("\\nabla f(X) = AX-B = 0").move_to([0,1,0])
        self.play(Create(function_to_solve))
        self.wait(2)
        self.play(TransformMatchingShapes(function_to_solve,final_function_to_solve))
        self.wait(2)
        self.play(FadeIn(function_to_min))
        self.wait(2)
        self.play(TransformMatchingShapes(final_function_to_solve,function_to_min_der))
        self.wait(3)
        self.play(FadeOut(function_to_min_der),function_to_min.animate.move_to([3.5,-1,0]).scale(0.6))
        self.wait()



        ax = Axes(y_range=[0,1000,1],x_range=[0.01,0.59,1],x_length=5,y_length=5,axis_config={"include_tip" :True,"include_numbers" : False,"include_ticks":False}).move_to([-2,-1,0])
        label = ax.get_axis_labels(x_label="step",y_label="iterations")
        self.wait(2)
        self.play(Create(ax),FadeIn(label))
     
        
        
        #
        l = zeros(3)
        l[0] = 2
        l[1] = -1
        A = zeros((3,3))
        A[0] = l
        
        for i in range (1,3-1):
            l = zeros(3)
            l[i] = 2
            l[i-1] = -1
            l[i+1] = -1
            A[i] = l
        A[3-1][3-2] = -1
        A[3-1][3-1] = 2
        val = linalg.eigvals(A)
        vpmax = max(val)
        vpmin = min(val)
        x = ones (3)
        #choose B here 
        B = ones (3)
        B[0] = 5
        B[3-1] = 7
        axe1 , axe2 = [],[]
        
        for k in range(5,200):
            p = k*0.005
            if (p > 2/(vpmax)):
                break
            x = ones (3)
            i=0
            while True :
                i+=1
                d = matmul(A,x)-B
                x = x - p*d
                if all( abs(d) <= 1e-4)  :
                    break      
            
            axe1.append(p)
            axe2.append(i)
        iterations = ValueTracker(0)
        pas =  ValueTracker(0)
        print(axe1)
        
        iter_tracker =MathTex("number \\, of \\, iterations : ",iterations.get_value()).move_to([3,3,0])
        p_tracker =MathTex("the \\,step\\,p :",pas.get_value()).move_to([3,2,0])
        self.play(Create(iter_tracker),Create(p_tracker))
        for k in range(len(axe1)):
            
            pas.set_value(axe1[k])
            iterations.set_value(axe2[k])
            self.remove(iter_tracker)
            iter_tracker =MathTex("number" , "of "," iterations : ",iterations.get_value()).move_to([3,3,0])
            self.add(iter_tracker)
            self.remove(p_tracker)
            p_tracker =MathTex("the ","step","p:" ,"{:.3f}".format(pas.get_value())).move_to([3,2,0])
            self.add(p_tracker)
            self.add(Point(ax.c2p(axe1[k],axe2[k]),color=RED))
            self.wait(max(3/(k+1),0.1))

        self.wait(4)