from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from sympy import *
class CalculusApp(App):
    def build(self):
        layout1=BoxLayout(orientation="vertical")
        def evaluate1(self):
            try:
                x=symbols(str(text2.text))
                ans=diff(str(text1.text),x)
                popup1=Popup(title="The answer is",content=Label(text=str(ans)),size_hint=(None,None),size=(300,100))
                popup1.open()
            except:
                popup1=Popup(title="Error!",content=Label(text="Please enter a valid expression"),size_hint=(None,None),size=(300,100))
                popup1.open()
        def evaluate2(self):
            try:
                x=symbols(str(text2.text))
                lower=str(text3.text)
                upper=str(text4.text)
                ans=integrate(str(text1.text),(x,lower,upper))
                popup1=Popup(title="The answer is",content=Label(text=str(ans)),size_hint=(None,None),size=(300,100))
                popup1.open()
            except:
                popup1=Popup(title="Error!",content=Label(text="Please enter a valid expression"),size_hint=(None,None),size=(300,100))
                popup1.open()
            
        label1=Label(text="Differentiator and Integrator",top=layout1.top,font_size=20,size_hint_y=0.2)
        layout1.add_widget(label1)
        label2=Label(text="Type the expression here!",size_hint_y=0.2,font_size=15)
        layout1.add_widget(label2)
        text1=TextInput(size_hint_y=0.15,multiline=False,font_size=20)
        label4=Label(text="Independent variable",size_hint_y=0.2,font_size=15)
        text2=TextInput(size_hint_y=0.1,font_size=20,multiline=False)
        label5=Label(text="Enter the lower limit(for integration)",size_hint_y=0.2,font_size=15)
        text3=TextInput(size_hint_y=0.1,font_size=15)
        label6=Label(text="Enter the upper limit(for integration)",size_hint_y=0.2,font_size=15)
        text4=TextInput(size_hint_y=0.1,font_size=15)
        label7=Label(text="",size_hint_y=0.1,font_size=15)
        layout1.add_widget(text1)
        layout1.add_widget(label4)
        layout1.add_widget(text2)
        layout1.add_widget(label5)
        layout1.add_widget(text3)
        layout1.add_widget(label6)
        layout1.add_widget(text4)
        Button1=Button(text="Differentiate",size_hint=(None,0.1),font_size=15,width=100,on_press=evaluate1)
        Button2=Button(text="Integrate",size_hint=(None,0.1),font_size=15,width=100,on_press=evaluate2)
        label8=Label(text="",size_hint_y=0.1,font_size=15,size_hint_x=0.2)
        label9=Label(text="",size_hint_y=0.1,font_size=15,size_hint_x=0.2)
        layout1.add_widget(label7)
        layout1.add_widget(Button1)
        layout1.add_widget(label8)
        layout1.add_widget(Button2)
        layout1.add_widget(label9)
        return layout1
if __name__=="__main__":
    CalculusApp().run()
