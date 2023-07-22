from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.containers import ScrollableContainer, Container
from textual.widgets import Placeholder, Header, Footer, Button, Static, Input
from .sqlite_interface import DBManager


class WOName(Static):
    """Widget for displaying workoutnames."""

    #TODO: Grab the workouts from SQlite DB

class Workouts(Static):
    """Widget for displaying workouts"""

    def compose(self) -> ComposeResult:
        """Create child widgets for the workouts."""
        yield Container( 
        Button("Start", id="start"),
        Button("Export", id="export"), id='buttons')
        yield WOName("Testing")

class Menu(Screen):
    """A screen for displaying the available workouts."""

    #TODO: Move the css path to here once you're done editing it in the main py file

    BINDINGS = [
        ('a','add_workout','Add Workout'),
        ('r','remove_workout','Remove Workout'),
        ]

    def compose(self) -> None:
        yield Header()
        yield Footer()
        yield ScrollableContainer(id="workout_list")

    def action_remove_workout(self) -> None:
        """Remove selected workout."""

        #TODO: Remove the selected workout, not just the last added

        workouts = self.query("Workouts")
        if workouts:
            workouts.last().remove()