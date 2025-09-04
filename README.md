## Project: Speech Assistant and Text Summarizer

A small Python project with two parts:
- A simple voice assistant that listens via microphone and speaks responses.
- A desktop GUI app to summarize text from input, files, or URLs using multiple NLP methods (spaCy, NLTK, Gensim, Sumy).

### Features
- **Speech assistant** (`Speech/speech.py`):
  - Listens with your microphone using Google Speech Recognition.
  - Responds to prompts like "how are you", "who are you", "time now", "where is <place>", and "exit".
  - Uses gTTS to synthesize speech.
- **Text summarizer GUI** (`Text summarization/app.py`):
  - Tabs for Text, File, URL, Compare, and About.
  - Summarization backends: **spaCy**, **NLTK**, **Gensim**, **Sumy (LexRank)**.
  - Save summaries to a timestamped file.

### Project structure
```
Project-master/
  README.md
  Speech/
    speech.py
  Text summarization/
    app.py
    nltk_summarization.py
    spacy_summarization.py
    notes
```

### Prerequisites
- Python 3.8+ recommended
- pip
- A working microphone (for the speech assistant)
- On Windows, ensure microphone permissions are granted to the terminal/IDE

### Installation
1) Create and activate a virtual environment
```bash
python -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
# CMD
.\.venv\Scripts\activate.bat
```

2) Install Python packages
```bash
pip install --upgrade pip
pip install speechrecognition pyaudio gTTS spacy gensim nltk beautifulsoup4 lxml sumy
```

3) Download spaCy English model
```bash
python -m spacy download en_core_web_sm
```

4) Download NLTK data (first run will try to use these)
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Platform notes
- The speech assistant currently plays audio using `mpg321` via `os.system` (Linux/macOS). On Windows, `mpg321` is not available by default.
  - Quick workaround: Replace the `os.system("mpg321 audio.mp3")` line in `Speech/speech.py` with one of:
    - `os.startfile("audio.mp3")` (Windows-only), or
    - use `playsound` (`pip install playsound`) and then `from playsound import playsound; playsound("audio.mp3")`.

### How to run
- Speech assistant
```bash
python "Speech/speech.py"
```
Say one of the supported phrases. Say "exit" to quit.

- Text summarizer GUI
```bash
python "Text summarization/app.py"
```
Use the tabs to paste text, open a file, fetch from a URL, or compare summarizers.

### Troubleshooting
- Microphone not found / `pyaudio` install issues:
  - On Windows, install PyAudio wheels from a reputable source if `pip install pyaudio` fails.
- spaCy model error `OSError: [E050] Can't find model 'en_core_web_sm'`:
  - Re-run: `python -m spacy download en_core_web_sm`.
- NLTK `LookupError` for `punkt` or `stopwords`:
  - Run the NLTK download commands in Python as shown above.
- Gensim summarizer returns empty output:
  - Provide longer input text; Gensim needs sufficient length to extract sentences.
- Audio playback on Windows:
  - Use `os.startfile("audio.mp3")` or the `playsound` package.

### Security and API notes
- Google Speech Recognition in `speech_recognition` sends audio to Google for transcription per the library's behavior.

### License
Provide license details here if applicable.

### Acknowledgments
- `speech_recognition`, `gTTS`, `spaCy`, `NLTK`, `Gensim`, `Sumy`, `BeautifulSoup` communities and maintainers.
