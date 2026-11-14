# Discord-Bot: Musik · Vers des Tages · Audit-Log

## Start
1. `.env.example` nach `.env` kopieren und ausfüllen (alle Einstellungen stehen dort).
2. FFmpeg installieren (`winget install ffmpeg` / `sudo apt install ffmpeg` / `brew install ffmpeg`).
3. `pip install -r requirements.txt`
4. `python bot.py`

## Discord Developer Portal
Unter **Bot → Privileged Gateway Intents** aktivieren:
- Server Members Intent
- Message Content Intent

Bot-Rechte beim Einladen (Scopes `bot` + `applications.commands`):
Audit-Log anzeigen, Nachrichten senden, Links einbetten, Nachrichtenverlauf lesen, Verbinden, Sprechen.

## Befehle
| Befehl | Funktion |
|---|---|
| `/play song:` | Song suchen/abspielen, Now-Playing-Panel mit Buttons |
| `/skip` `/stop` `/queue` `/volume` `/leave` | Musiksteuerung |
| `/likes` | Deine gelikten Songs |
| `/vers [religion]` | Vers aus Bibel, Koran, Tanakh |

Täglich zur eingestellten Uhrzeit (Standard 0:00) wird der Vers in `VERSE_CHANNEL_ID` gepostet.

## Logs (`LOG_CHANNEL_ID`)
Slash-Commands, Kick, Ban, Unban, Timeout, Rollenänderungen, Kanal/Rolle erstellt/gelöscht,
Nachricht gelöscht (inkl. wer gelöscht hat) und bearbeitet, Beitritt/Austritt, Sprachkanal-Wechsel.

## Quellen
- Bibel & Tanakh: Lutherbibel 1912 (gemeinfrei), lokal in `data/luther1912.json.gz`
- Koran: api.alquran.cloud (arabisch + Bubenheim)
- Lyrics: lrclib.net
