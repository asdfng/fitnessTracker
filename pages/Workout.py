from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder, Header, Footer

class Workout(Screen):
    """A screen for displaying the exercises for that day."""
     
    #TODO: Think of some keybindings for making navigation easier?

    def compose(self) -> None:
        yield Header()
        yield Footer()

    