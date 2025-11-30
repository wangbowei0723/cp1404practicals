"""
dynamic_labels
Estimate: 60 minutes
Actual:  minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Define the data"""
        super().__init__(**kwargs)
        self.names = ["John", "Lily", "Clara", "Rose"]

DynamicLabelsApp().run()