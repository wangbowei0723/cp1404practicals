"""
convert_m_km_solution
Estimate: 65 minutes
Actual: 55 minutes
"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION_FACTOR = 1.60934


class MilesToKmApp(App):
    """GUI App: Convert miles to kilometres using Kivy."""
    def build(self):
        """Set up the main interface from kv file."""
        self.title = "Miles to Km Converter"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def calculate_km(self):
        """Update label with converted km value."""
        miles = self.get_miles_input()
        km = miles * CONVERSION_FACTOR
        self.root.ids.km_output.text = str(km)

    def adjust_input(self, delta):
        """Adjust miles input value by delta, then update result."""
        current = self.get_miles_input()
        new_value = current + delta
        self.root.ids.miles_input.text = str(new_value)
        self.calculate_km()

    def get_miles_input(self):
        """Try to get miles as float, if invalid return 0 ."""
        try:
            return float(self.root.ids.miles_input.text)
        except ValueError:
            return 0


MilesToKmApp().run()
