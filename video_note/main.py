import sys

from PyQt6.QtCore import QPoint, Qt, QUrl
from PyQt6.QtGui import QAction, QKeyEvent, QMouseEvent
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import QApplication, QFileDialog, QMainWindow


class VideoNoteWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Video Note")
        self.setGeometry(100, 100, 1000, 700)

        # Make the window frameless
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # For window moving
        self.drag_position = QPoint()

        # Create media player
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        # Create video widget
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)

        # Set video widget as central widget
        self.setCentralWidget(self.video_widget)

        # Create menu bar
        self.create_menu_bar()

        # Connect media player signals
        self.media_player.playbackStateChanged.connect(self.media_state_changed)

        # Set initial state
        self.is_fullscreen = False

    def create_menu_bar(self) -> None:
        # Create menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("&File")

        # Open action
        open_action = QAction("&Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_video)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        # Exit action
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # View menu
        view_menu = menu_bar.addMenu("&View")

        # Play/Pause action
        self.play_action = QAction("&Play", self)
        self.play_action.setShortcut("Ctrl+P")
        self.play_action.triggered.connect(self.play_video)
        self.play_action.setEnabled(False)
        view_menu.addAction(self.play_action)

        view_menu.addSeparator()

        # Fullscreen action
        fullscreen_action = QAction("&Fullscreen", self)
        fullscreen_action.setShortcut("F11")
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        fullscreen_action.setEnabled(False)
        self.fullscreen_action = fullscreen_action
        view_menu.addAction(fullscreen_action)

    def open_video(self) -> None:
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Video",
            "",
            "Video Files (*.mp4 *.avi *.mov *.mkv *.wmv *.flv *.webm)",
        )

        if file_name:
            self.media_player.setSource(QUrl.fromLocalFile(file_name))
            self.play_action.setEnabled(True)
            self.fullscreen_action.setEnabled(True)
            self.media_player.play()

    def play_video(self) -> None:
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def media_state_changed(self, state: QMediaPlayer.PlaybackState) -> None:
        if self.play_action:
            if state == QMediaPlayer.PlaybackState.PlayingState:
                self.play_action.setText("Pause")
            else:
                self.play_action.setText("Play")

    def toggle_fullscreen(self) -> None:
        if self.is_fullscreen:
            self.showNormal()
            self.is_fullscreen = False
        else:
            self.showFullScreen()
            self.is_fullscreen = True

    def exit_fullscreen(self) -> None:
        if self.is_fullscreen:
            self.showNormal()
            self.is_fullscreen = False

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.MouseButton.LeftButton and not self.drag_position.isNull():
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        # Handle keyboard shortcuts
        # We're not handling any keys here, letting the menu shortcuts handle everything
        super().keyPressEvent(event)


def main() -> None:
    app = QApplication(sys.argv)
    window = VideoNoteWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
