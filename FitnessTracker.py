from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static

from pages.Menu import Menu
from pages.Workout import Workout

class FitnessTracker(App):
    """A Textual app for tracking works."""

    BINDINGS = [("d", "toggle_dark", "Dark Mode")]
    SCREENS = {"menu": Menu(), "workout": Workout()}

    def on_mount(self) -> None:
        self.push_screen('menu')

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = FitnessTracker()
    app.run()

