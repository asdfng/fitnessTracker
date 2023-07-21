from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import ScrollableContainer
from textual.widgets import Placeholder, Header, Footer, Button, Static

class WOName(Static):
    """Widget for displaying workoutnames."""

class Workouts(Static):
    """Widget for displaying workouts"""

    def compose(self) -> ComposeResult:
        """Create child widgets for the workouts."""
        yield Button("Start", id="start")
        yield Button("Export", id="export")
        yield WOName("Testing")

class Menu(Screen):
    """A screen for displaying the available workouts."""

    #TODO: Think of some keybindings for making navigation easier?
    CSS_PATH = "./css/menu.css"

    def compose(self) -> None:
        yield Header()
        yield Footer()
        yield ScrollableContainer(Workouts(), Workouts(), Workouts(), Workouts(), id="workout_list")
