import sys
import os

# ✅ Add root project folder path (so it can find app.py)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as application
