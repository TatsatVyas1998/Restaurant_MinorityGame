from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )
import  numpy  as  np 
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

     
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        
        QMainWindow . __init__ ( self )

        loadUi ( "simulation.ui" , self )

        self . setWindowTitle ( "PyQt5 & Matplotlib Example GUI" )

        self . runSim . clicked . connect ( self . update_graph )
        #self . stopSim . clicked . connect (self.stop_graph)

        self . addToolBar ( NavigationToolbar ( self . MplWidget . canvas ,  self ))



    def  update_graph ( self ):

        agents=self.agents.text()
        rounds=self.rounds.text()
        print("Successfully input ",agents," and ",rounds)


        x_vals=[1,2,3,4,5]
        y_vals=[1,2,3,2,4]

        index=count()

        def animate(i):
            #x_vals.append(next(index))
            #y_vals.append(random.randint(0,5))
            self . MplWidget . canvas . axes . clear () 
            self . MplWidget . canvas . axes . plot ( x_vals, y_vals ) 
            self . MplWidget . canvas . axes . set_title ( ' Agent Turnout ' ) 
            self . MplWidget . canvas . axes . set_xlabel( 'Round' ) 
            self . MplWidget . canvas . axes . set_ylabel( 'Agents') 
            self . MplWidget . canvas . draw ()
            #print("test1")
            self . stopSim . clicked . connect(stop_graph)
        
        
        def stop_graph(self):
            ani.event_source.stop()


        ani=animation.FuncAnimation(self.MplWidget,animate,interval=1000)
        
        #self . MplWidget . canvas . axes . legend (( 'cosinus'),loc = 'upper right' ) 
        #print("test")
        self . MplWidget . canvas . draw ()
        

app  =  QApplication ([]) 
window  =  MatplotlibWidget () 
window.setFixedWidth(1605)
window.setFixedHeight(1006)
window . show () 
app . exec_ ()
