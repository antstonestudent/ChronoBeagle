from kivy.uix.accordion import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class TaskSched(Screen):  
    def __init__(self, **kwargs):
        super(TaskSched, self).__init__(**kwargs)

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        # BoxLayout for the toolbar
        toolbar = BoxLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Add left icon (logo)
        left_icon_layout = BoxLayout(padding=(5, 5, 0, 0))
        left_icon = Image(source='assets/icon/cb-icon-128.png', size_hint=(None, 1), width=50)

        toolbar.add_widget(left_icon)
        toolbar.add_widget(left_icon_layout)

        # Add title label
        title_label = Label(text='ChronoBeagle', halign='center', valign='middle', color=(0, 0, 0, 1), bold=True, font_size='24sp', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        toolbar.add_widget(title_label)

        # Add right icon (settings gear)
        right_icon_layout = BoxLayout(padding=(0, 5, 5, 0))
        right_icon = Image(source='assets/icon/gear.png', size_hint=(None, 1), width=50)

        toolbar.add_widget(right_icon_layout)
        toolbar.add_widget(right_icon)

        self.layout.add_widget(toolbar)