import os
from gtts import gTTS
from PyPDF2 import PdfReader
from tkinter import filedialog
import subprocess

# ouvre l'exploateur de fichier
path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")])
if not path:
    print("Pas de fichier sélectionné.")
    exit()

# lis le contenu du fichier pdf ou txt
text = 'Audio généré à partir du fichier PDF ou txt\n\n'
if path.endswith('.pdf'):
    pdf = PdfReader(path)
    for page in pdf.pages:
        text += page.extract_text()
elif path.endswith('.txt'):
    with open(path, 'r') as f:
        text += f.read()

# sauvegarde le contenu dans un fichier txt
txt_path = os.path.splitext(path)[0] + '.txt'
with open(txt_path, 'w') as f:
    f.write(text)

# Convertit le texte en audio
tts = gTTS(text, lang='fr', tld='fr')
mp3_path = 'hello.mp3'
tts.save(mp3_path)

# Joue l'audio
subprocess.run(['start', mp3_path], shell=True, check=True)

print('Audio généré avec succès !')