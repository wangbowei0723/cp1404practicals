class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar ."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"



