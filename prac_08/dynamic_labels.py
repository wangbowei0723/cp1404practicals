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

    def build(self):
        """Build the kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root

DynamicLabelsApp().run()