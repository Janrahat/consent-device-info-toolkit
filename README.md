# Consent-Based Device Info Demo

A small Flask project for learning how browser permissions and explicit consent work.

## Safety and privacy design
- No disguised prize/phishing page.
- No automatic collection on page load.
- No IP-address or request-header logging.
- No canvas/WebGL fingerprinting, battery collection, or plugin enumeration.
- Location is optional and requires a separate browser prompt.
- The server binds to `127.0.0.1` for local testing.

## Run on Kali Linux
```bash
sudo apt update
sudo apt install -y python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:8080` in your browser. The local demo dashboard is at
`http://127.0.0.1:8080/live`.

## Run in Termux
```bash
pkg update
pkg install python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## GitHub upload
Create a new repository on GitHub, then from this project folder run:
```bash
git init
git add app.py templates/index.html requirements.txt README.md .gitignore
git commit -m "Add consent-based device info demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the example remote with your own repository address. Do not publish real collected records or secrets.
