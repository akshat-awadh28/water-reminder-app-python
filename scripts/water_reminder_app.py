from pathlib import Path
import time
from plyer import notification

if __name__ == "__main__":

    # Get the main project directory
    project_dir = Path(__file__).resolve().parent.parent

    # Path to the notification icon
    icon_path = project_dir / "app_icons" / "water_glass_icon.ico"

    while True:

        notification.notify(
            title="Please drink water",
            message="Water is very essential for health",
            app_icon=str(icon_path),
            timeout=7
        )

        time.sleep(60 * 60)