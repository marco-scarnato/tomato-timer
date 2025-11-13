import tkinter as tk
import pygame
import sys
import os

# ============== INIZIALIZZAZIONE ==============
pygame.mixer.init()

# ============== FUNZIONE PER PERCORSI RISORSE ==============
def resource_path(relative_path):
    """Ottiene il percorso assoluto della risorsa, funziona sia in dev che in eseguibile"""
    try:
        # PyInstaller crea una cartella temporanea e salva il path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# ============== COSTANTI ==============
WORK_TIME = 25 * 60  # Timer di lavoro in secondi (25 minuti)
BREAK_TIME = 5 * 60  # Timer di pausa in secondi (5 minuti)

# Colori tema
BG_COLOR = "#0B1E3F"  # Blu notte come sfondo
WORK_COLOR = "#FF6A00"  # Arancione brillante per lavoro
BREAK_COLOR = "#4CAF50"  # Verde per pausa
WORK_GLOW = "#FF8C33"   # Alone arancione
BREAK_GLOW = "#6FD68F"  # Alone verde chiaro
BUTTON_BG = "#2D2D2D"
BUTTON_FG = "#FFFFFF"

# ============== VARIABILI GLOBALI ==============
time_left = WORK_TIME
timer_running = False
timer_id = None
is_work_session = True  # True = lavoro, False = pausa
canvas = None  # Canvas per il cerchio progressivo

# ============== FUNZIONI HELPER ==============
def format_time(seconds):
    """Converte secondi in formato MM:SS"""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"

def play_pause_music():
    """Avvia la musica di pausa in loop"""
    try:
        pygame.mixer.music.load(resource_path("assets/pause-theme.ogg"))
        pygame.mixer.music.play(-1)  # -1 = loop infinito
    except Exception as e:
        print(f"Errore: impossibile caricare assets/pause-theme.ogg - {e}")

def stop_pause_music():
    """Ferma la musica di pausa"""
    pygame.mixer.music.stop()

def draw_progress_ring():
    """Disegna il cerchio progressivo basato sul tempo rimanente"""
    canvas.delete("all")
    
    # Dimensioni
    width = 280
    height = 280
    center_x = width // 2
    center_y = height // 2
    radius = 120
    ring_width = 12
    
    # Calcola il progresso
    total_time = WORK_TIME if is_work_session else BREAK_TIME
    progress = time_left / total_time
    
    # Colori in base alla sessione
    if is_work_session:
        ring_color = WORK_COLOR
        glow_color = WORK_GLOW
    else:
        ring_color = BREAK_COLOR
        glow_color = BREAK_GLOW
    
    # Disegna alone (glow) - cerchio più grande sotto
    canvas.create_oval(
        center_x - radius - 8, center_y - radius - 8,
        center_x + radius + 8, center_y + radius + 8,
        outline=glow_color, width=6, fill=""
    )
    
    # Disegna cerchio di sfondo (grigio scuro)
    canvas.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        outline="#1A1A1A", width=ring_width, fill=""
    )
    
    # Disegna arco progressivo
    if progress > 0:
        extent = 360 * progress
        canvas.create_arc(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            start=90, extent=-extent,
            outline=ring_color, width=ring_width,
            style=tk.ARC, fill=""
        )

def switch_session():
    """Cambia tra sessione di lavoro e pausa"""
    global is_work_session, time_left
    
    is_work_session = not is_work_session
    
    if is_work_session:
        time_left = WORK_TIME
        time_label.config(fg=WORK_COLOR)
        session_label.config(text="Sessione di Lavoro")
        stop_pause_music()  # Ferma la musica quando torna al lavoro
    else:
        time_left = BREAK_TIME
        time_label.config(fg=BREAK_COLOR)
        session_label.config(text="Pausa")
        if timer_running:  # Avvia musica solo se il timer è in esecuzione
            play_pause_music()
    
    time_label.config(text=format_time(time_left))
    draw_progress_ring()  # Ridisegna il cerchio con i nuovi colori

# ============== FUNZIONI TIMER ==============
def update_timer():
    """Aggiorna il timer ogni secondo"""
    global time_left, timer_running, timer_id
    
    if timer_running and time_left > 0:
        time_left -= 1
        time_label.config(text=format_time(time_left))
        draw_progress_ring()  # Aggiorna il cerchio
        timer_id = window.after(1000, update_timer)
    elif time_left == 0:
        # Timer finito, passa alla sessione successiva
        switch_session()
        # Riavvia automaticamente il timer
        update_timer()

def toggle_timer():
    """Avvia o ferma il timer"""
    global timer_running
    
    if timer_running:
        # Ferma il timer
        stop_timer()
    else:
        # Avvia il timer
        start_timer()

def start_timer():
    """Avvia il timer"""
    global timer_running
    timer_running = True
    control_button.config(text="■")  # Cambia simbolo a stop
    
    # Se è una sessione di pausa, avvia la musica
    if not is_work_session:
        play_pause_music()
    
    update_timer()

def stop_timer():
    """Ferma il timer"""
    global timer_running, timer_id
    timer_running = False
    control_button.config(text="▶")  # Cambia simbolo a play
    stop_pause_music()  # Ferma la musica se in esecuzione
    if timer_id:
        window.after_cancel(timer_id)

# ============== SETUP UI ==============
# Crea la finestra principale
window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("450x550")
window.configure(bg=BG_COLOR)

# Imposta il logo come icona della finestra
try:
    logo = tk.PhotoImage(file=resource_path("assets/logo.png"))
    window.iconphoto(True, logo)
except Exception as e:
    print(f"Errore: impossibile caricare assets/logo.png - {e}")

# Label per indicare il tipo di sessione
session_label = tk.Label(
    window,
    text="Sessione di Lavoro",
    font=("Arial", 16),
    bg=BG_COLOR,
    fg="#AAAAAA"
)
session_label.pack(pady=(20, 10))

# Frame contenitore per canvas e label tempo
timer_frame = tk.Frame(window, bg=BG_COLOR)
timer_frame.pack(pady=20)

# Canvas per il cerchio progressivo
canvas = tk.Canvas(
    timer_frame,
    width=280,
    height=280,
    bg=BG_COLOR,
    highlightthickness=0
)
canvas.pack()

# Etichetta per mostrare il tempo (sovrapposta al canvas)
time_label = tk.Label(
    timer_frame, 
    text=format_time(time_left), 
    font=("Arial", 56, "bold"),
    bg=BG_COLOR,
    fg=WORK_COLOR
)
time_label.place(in_=canvas, relx=0.5, rely=0.5, anchor=tk.CENTER)

# Disegna il cerchio iniziale
draw_progress_ring()

# Frame per i pulsanti
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=30)

# Pulsante principale Start/Stop (più ovale con padding)
control_button = tk.Button(
    button_frame,
    text="▶",  # Simbolo play
    command=toggle_timer,
    font=("Arial", 28),
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    width=8,
    height=2,
    relief=tk.FLAT,
    borderwidth=0,
    highlightthickness=0,
    cursor="hand2"
)
control_button.pack()

# Avvia il loop principale
window.mainloop()