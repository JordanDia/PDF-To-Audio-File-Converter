@echo off

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call .\venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Additional setup commands (if needed)
REM ...

echo Setup complete. Virtual environment activated.
