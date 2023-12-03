import pyttsx3
import PyPDF2
import glob

# Find pdf file
def find_files(extension):
    return glob.glob(f'*{extension}')
file_path = find_files(".pdf")[0]

# Initialize pdf reader and speaker
reader = PyPDF2.PdfReader(open(file_path, 'rb'))
speaker = pyttsx3.init()

# Change voice
voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty("voice", voice_id)

# Get pdf text
for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    text = page.extract_text()
    fresh_text = text.strip().replace('\n', ' ')

# Convert and save to mp3 file
speaker.save_to_file(fresh_text, "audio.mp3")
speaker.runAndWait()
speaker.stop()