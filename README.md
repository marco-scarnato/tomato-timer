# 🍅 Pomodoro Timer

Un'applicazione desktop multipiattaforma per la gestione del tempo basata sulla tecnica Pomodoro. Interfaccia moderna con tema blu notte, timer visivi circolari e musica rilassante durante le pause.

![Pomodoro Timer](assets/logo.png)

## ✨ Caratteristiche

- ⏱️ **Timer alternati**: 25 minuti di lavoro, 5 minuti di pausa
- 🎨 **Interfaccia moderna**: Tema scuro blu notte con cerchio progressivo animato
- 🎵 **Musica per le pause**: Traccia audio rilassante che parte automaticamente durante i break
- 🔄 **Cicli automatici**: Alterna automaticamente lavoro e pausa
- 🎯 **Indicatori visivi**: Colori diversi per lavoro (arancione) e pausa (verde)
- 💻 **Multipiattaforma**: Funziona su Windows, macOS e Linux

## 📸 Screenshot

L'app mostra:
- Timer digitale al centro di un cerchio progressivo
- Indicatore della sessione corrente (Lavoro/Pausa)
- Pulsante play/stop con simboli intuitivi
- Animazione del cerchio che si riduce con il passare del tempo

## 🚀 Installazione

### Prerequisiti

- Python 3.8 o superiore
- pip (gestore pacchetti Python)

### Setup

1. **Clona il repository**
```bash
git clone https://github.com/tuousername/pomodoro-timer.git
cd pomodoro-timer
```

2. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

3. **Aggiungi i file assets**

Assicurati di avere i seguenti file nella cartella `assets/`:
- `pause-theme.ogg` - Musica per le pause (formato OGG)
- `logo.png` - Logo dell'applicazione

## 🎮 Utilizzo

### Esecuzione da sorgente

```bash
python main.py
```

### Controlli

- **▶ Play**: Avvia il timer
- **■ Stop**: Mette in pausa il timer
- Il timer alterna automaticamente tra sessioni di lavoro e pause

### Personalizzazione

Puoi modificare la durata dei timer nel file `main.py`:

```python
WORK_TIME = 25 * 60  # 25 minuti (modificabile)
BREAK_TIME = 5 * 60  # 5 minuti (modificabile)
```

Per i test, puoi impostare valori più bassi (es. `5` secondi invece di `25 * 60`).

## 🔨 Creare un eseguibile

### Per Windows

```bash
pyinstaller --name="PomodoroTimer" --onefile --windowed --icon=assets/logo.png --add-data="assets;assets" main.py
```

L'eseguibile sarà in `dist/PomodoroTimer.exe`

### Per macOS

```bash
pyinstaller --name="PomodoroTimer" --onefile --windowed --icon=assets/logo.png --add-data="assets:assets" main.py
```

L'applicazione sarà in `dist/PomodoroTimer.app`

### Per Linux

```bash
pyinstaller --name="PomodoroTimer" --onefile --windowed --add-data="assets:assets" main.py
```

L'eseguibile sarà in `dist/PomodoroTimer`

> **Nota**: Gli eseguibili devono essere compilati sul sistema operativo di destinazione. Non è possibile creare un `.exe` per Windows da macOS o viceversa.

## 📁 Struttura del progetto

```
pomodoro-timer/
├── main.py              # File principale dell'applicazione
├── requirements.txt     # Dipendenze Python
├── README.md           # Questo file
└── assets/             # Risorse dell'applicazione
    ├── pause-theme.ogg # Musica per le pause
    └── logo.png        # Logo/icona dell'app
```

## 🛠️ Tecnologie utilizzate

- **Python 3** - Linguaggio di programmazione
- **Tkinter** - GUI (interfaccia grafica)
- **Pygame** - Gestione audio

## 🎨 Temi di colore

- **Background**: Blu notte (`#0B1E3F`)
- **Lavoro**: Arancione brillante (`#FF6A00`)
- **Pausa**: Verde (`#4CAF50`)

## 🤝 Contribuire

I contributi sono benvenuti! Per contribuire:

1. Fai un fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📝 Idee per miglioramenti futuri

- [ ] Statistiche delle sessioni completate
- [ ] Notifiche desktop alla fine dei timer
- [ ] Configurazione personalizzabile tramite interfaccia
- [ ] Suoni personalizzabili
- [ ] Modalità "lunga pausa" dopo 4 pomodori
- [ ] Salvataggio delle preferenze
- [ ] Temi di colore alternativi

## 📄 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

## 👤 Autore

Il tuo nome - [@tuousername](https://github.com/tuousername)

## 🙏 Ringraziamenti

- Tecnica Pomodoro ideata da Francesco Cirillo
- Ispirato dalla necessità di migliorare la produttività personale

---

⭐ Se questo progetto ti è stato utile, lascia una stella su GitHub!