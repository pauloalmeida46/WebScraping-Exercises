@echo off
chcp 65001 >nul
cd /d "%~dp0"
python rodar_todos.py
pause
