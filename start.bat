@echo
call %~dp0bot\venv\Scripts\activate
cd %~dp0bot\bot
set TOKEN=Your_token
python sakura.py
pause
