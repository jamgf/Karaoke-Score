import random
import time
import tkinter as tk
from tkinter import Label, Button
from playsound import playsound


class RandomScoreGeneratorApp:
    botaocalcular = "normal"
    botaoouvir = "disable"
    def __init__(self, root):
        self.root = root
        self.root.title("Pontuação de Karaoke")
        self.root.geometry("500x500")
        
        self.score_label = Label(root, text="Sua pontuação total é:", font=("Helvetica", 18))
        self.score_label.pack(pady=20)

        self.score_value_label = Label(root, text="", font=("Helvetica", 24, "bold"))
        self.score_value_label.pack()

        self.message_label = Label(root, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=10)

        self.generate_button = Button(root, text="Calcule sua pontuação", command=self.generate_random_score, font=("Helvetica", 14), state= "normal")
        self.generate_button.pack()
        self.generate_button = Button(root, text="Solte a música", command=self.nada, font=("Helvetica", 14))
        self.generate_button.pack()
    
    def nada(self):
        self.message_label.config(text="Ouvindo você cantar")
        self.root.update() 
        time.sleep(30)
    def generate_random_score(self):
        random_score = random.randint(40, 105)
        self.message_label.config(text="Calculando")
        self.root.update() 
        time.sleep(1.3)
        
        self.score_label.config(text=f"Sua pontuação é: {random_score} !")
        if random_score < 50:
            message="Nossa, essa foi doída de ouvir!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/40.mp3"
        elif random_score < 60:
            message="Parabéns, mas tente melhorar!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/60.mp3"
        elif random_score < 70:
            message="Parabéns, mais ainda não chegou lá!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/60.mp3"
        elif random_score < 80:
            message="Parabéns, isso aí!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/60.mp3"
        elif random_score < 90:
            message="Parabéns, você canta no coral?"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/90.mp3"
        elif random_score < 100:
            message= "Parabéns, quase um Sinatra!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/90.mp3"
        elif random_score == 100:
            message="Parabéns, você é excelente!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/100.mp3"
        elif random_score > 100:
            message="Excelente, acima de todas as expectativas!"
            som ="C:/Users/jmfil/OneDrive/Documentos/score karaoke/100.mp3"

        self.message_label.config(text=message)
        
        self.root.update() 
        playsound(som)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomScoreGeneratorApp(root)
    root.mainloop()
