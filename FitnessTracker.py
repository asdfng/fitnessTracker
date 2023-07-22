from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer, Grid
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static, Input
from textual.screen import ModalScreen
from textual.binding import Binding

from pages.Menu import Menu
from pages.Workout import Workout

class ExerciseField(Static):
    """Formated input field for exercise parameters"""

    def compose(self) -> ComposeResult:
        yield Grid(Input(placeholder = "Exercise Name", id='e_name'),
        Input(placeholder = "Category", id='e_cat'),
        Input(placeholder = "Sets",id='e_sets'),
        Input(placeholder = "Reps",id='e_reps'),
        id="exercise_info")

class AddWorkout(ModalScreen[list]):
    """Screen for entering new workout."""

    BINDINGS = [
        ('a', 'add_exercise', 'Add Exercise'),
        ('r', 'remove_exercise', 'Remove Exercise')]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Workout Name", id="new_name")
        yield ScrollableContainer(id="exercises")

    def action_add_exercise(self) -> None:
        """Add exercise to the add workout section."""
        new_exercise = ExerciseField()
        self.query_one("#exercises").mount(new_exercise)

    def action_remove_exercise(self) -> None:
        """Remove exercise from the workout section."""
        exercises = self.query("ExerciseField")
        if exercises:
            exercises.last().remove()


class FitnessTracker(App):
    """A Textual app for tracking works."""

    CSS_PATH = 'FitnessTracker.css'
    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=False, priority=True),
        ("d", "toggle_dark", "Dark Mode"),
    ]
    SCREENS = {
        "menu": Menu(),
        "workout": Workout(),
        "addworkout": AddWorkout(),
        }

    def on_mount(self) -> None:
        self.push_screen('menu')

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_add_workout(self) -> None:
        self.push_screen('addworkout')


if __name__ == "__main__":
    app = FitnessTracker()
    app.run()

