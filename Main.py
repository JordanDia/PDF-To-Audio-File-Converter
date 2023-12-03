import pyttsx3
import PyPDF2

file_path = "test.pdf"
reader = PyPDF2.PdfReader(open(file_path, 'rb'))
speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate)
voice_id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

speaker.setProperty("voice", voice_id)

for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    text = page.extract_text()
    fresh_text = text.strip().replace('\n', ' ')

    speaker.say(fresh_text)

speaker.save_to_file(fresh_text, "audio.mp3")
speaker.runAndWait()
speaker.stop()