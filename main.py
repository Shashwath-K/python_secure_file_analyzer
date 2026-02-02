from app.config import (
    APP_NAME,
    APP_VERSION,
    ensure_directories,
)
from app.ui.gradio_app import create_interface


def main() -> None:
    """
    Application entry point.
    """

    ensure_directories()

    interface = create_interface()

    interface.launch(
        server_name="127.0.0.1",
        share=False
    )


if __name__ == "__main__":
    print(f"{APP_NAME} | Version {APP_VERSION}")
    main()
