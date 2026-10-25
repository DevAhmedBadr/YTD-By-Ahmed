# 🎬 YTD By Ahmed

**A Python-based YouTube video downloader with quality selection and a colorful console interface.**

YTD By Ahmed is a command-line project built with Python to practice programming, working with external libraries, and creating a simple, interactive downloading tool.

## ✨ Features

- 🔗 Accepts YouTube video URLs.
- 🎥 Offers multiple video quality options:
  - Best available quality
  - Up to 720p
  - Up to 480p
  - Lowest available quality
- 📁 Allows users to choose the download directory.
- 🌈 Provides a colorful console interface using Colorama.
- 🔄 Supports downloading multiple videos in one session.
- 🛠️ Uses FFmpeg when separate audio and video streams need to be merged.

## 🧰 Technologies Used

- **Python** — Core programming language.
- **yt-dlp** — Video downloading and format selection.
- **Colorama** — Colored terminal output.
- **FFmpeg** — Audio and video merging when required.

## 📋 Requirements

Before running the project, make sure you have:

- Python 3.10 or later.
- `yt-dlp`
- `colorama`
- FFmpeg available on your system when required for merging video and audio streams.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/iz8ldk/YTD-By-Ahmed.git
```

### 2. Navigate to the project directory

```bash
cd YTD-By-Ahmed
```

### 3. Install the required Python packages

```bash
python -m pip install yt-dlp colorama
```

### 4. Install FFmpeg

Install FFmpeg if it is not already available on your system. Make sure it can be detected through your system's `PATH`.

## ▶️ Usage

Run the program from your terminal:

```bash
python main.py
```

Follow the interactive prompts to:

1. Enter a YouTube video URL.
2. Choose a directory for the downloaded video, or press Enter to use the default directory.
3. Select the desired video quality.
4. Wait for the download to finish.
5. Choose whether to download another video or exit.

## 📂 Output

Downloaded videos are saved in the directory you specify. If no directory is provided, the program uses the `downloads` directory.

## ⚠️ Disclaimer

This project is intended for educational purposes and personal use with content you own or are authorized to download.

Users are responsible for complying with applicable laws, copyright restrictions, and YouTube's Terms of Service.

## 🎯 Project Goals

This project was created as a hands-on Python learning experience, focusing on:

- User input and conditional statements.
- Loops and program flow control.
- Functions and code organization.
- Working with third-party libraries.
- Handling file paths and external processes.
- Building a more user-friendly command-line interface.

## 👨‍💻 Author

**Ahmed**

GitHub: [@iz8ldk](https://github.com/iz8ldk)

---

⭐ If you find this project useful, consider giving the repository a star!
