# Python Automation

A collection of Python automation scripts.

---

## Projects

### 1. Currency Converter (`currency.py`)

Fetches live exchange rates and converts between currencies interactively in the terminal.

**Features**
- Enter any base currency and see rates for USD, CAD, EUR, AUD, and CNY
- Pulls live data from a currency exchange API
- Loops until you type `q` to quit

**Setup**

Create a `.env` file in the project root:
```
API_KEY=your_api_key_here
BASE_URL=your_base_url_here
```

**Usage**
```bash
python3 currency.py
```
```
Enter the base currency (q for quit): USD
CAD: 1.36
EUR: 0.92
AUD: 1.53
CNY: 7.24
```

---

### 2. Automated Folder Backup (`backup.py`)

Automatically backs up a folder once per day at a scheduled time, organized by date.

**Features**
- Copies the source folder to a destination directory
- Names each backup by today's date (e.g. `Backups/2026-06-05`)
- Skips the backup if one already exists for today
- Runs continuously in the background using a scheduler

**Usage**
```bash
python3 backup.py
```

The script will run silently and back up your folder daily at the configured time. Keep the terminal open (or run it as a background process) for it to stay active.

**Configuration**

Edit these variables at the top of `backup.py` to change the source/destination:
```python
source_dir = "/path/to/your/folder"
destination_dir = "/path/to/your/backups"
```

---

## Requirements

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Project Structure

```
python_automation/
├── currency.py       # Currency converter
├── backup.py         # Automated folder backup
├── requirements.txt  # Dependencies
├── .env              # API keys (not committed)
└── .gitignore
```
