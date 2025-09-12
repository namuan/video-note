# Video Note

A video annotation tool for taking notes on video content with built-in video playback

![](assets/video-note-screen.png)

## Features

Video Note is a powerful video annotation tool designed for taking notes while watching videos. Whether you're studying, researching, or just want to capture important moments from videos, Video Note makes it easy to:

- **Video Playback**: Open and play local video files in various formats (MP4, AVI, MOV, MKV, etc.)
- **Fullscreen Viewing**: Watch videos in fullscreen mode for an immersive experience
- **Playback Controls**: Play/pause videos using intuitive buttons or keyboard shortcuts
- **Timestamp Annotations**: Automatically capture video timestamps when creating notes (coming soon)
- **Rich Text Editing**: Format your notes with various text styles and formatting options (coming soon)
- **Tagging System**: Organize your annotations with custom tags for easy searching (coming soon)
- **Export Options**: Export your notes in multiple formats (PDF, Markdown, Text) (coming soon)
- **Search Functionality**: Quickly find specific annotations using keywords or tags (coming soon)
- **Customizable Interface**: Adjust the layout to suit your note-taking preferences (coming soon)

## Installation

Video Note requires Python 3.11+, PyQt6, and FFmpeg for video playback.

### Prerequisites

- uv
- FFmpeg (for video playback)

### Steps

1. Clone the repository:

   ```
   git clone https://github.com/namuan/video-note.git
   cd video-note
   ```

2. Install dependencies:

   ```
   make install
   ```

3. Run the application:

   ```
   make run
   ```

4. Install as an application (macOS only)
   ```
   make install-macosx
   ```

### Menu Options

- **File > Open** (Ctrl+O): Open a video file
- **File > Exit** (Ctrl+Q): Exit the application
- **View > Play/Pause** (Ctrl+P): Play or pause the video
- **View > Fullscreen** (F11): Toggle fullscreen mode

### Keyboard Shortcuts

- **Ctrl+Q**: Quit the application
- **F11**: Toggle fullscreen mode

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
