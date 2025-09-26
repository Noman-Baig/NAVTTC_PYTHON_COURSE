#  ++++ Create Env

# in windows
python -m venv myenv
# in Mac/Linux
python3 -m venv myenv

#  +++++ Activate ENV

# in windows 
myenv\Scripts\Activate.ps1 # powershell
myenv\Scripts\activate.bat # CMD

# in mac
source myenv/bin/activate

# ++++++ Deactivate (Exit Environment)

# Works on all
deactivate

# NOTE : If you’re on Mac/Linux and get “permission denied”,
chmod +x myenv/bin/activate
