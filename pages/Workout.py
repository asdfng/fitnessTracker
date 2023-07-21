from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    pass

class Footer(Placeholder):
    pass

class Workout(Screen):
    """A screen for displaying the exercises for that day."""
     
    #TODO: Think of some keybindings for making navigation easier?

    def compose(self) -> None:
        yield Header(id="Header")
        yield Footer(id="Footer")

    