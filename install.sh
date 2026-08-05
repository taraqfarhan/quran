#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting installation for Quran Tools..."

# Set up the virtual environment
echo "Creating Python virtual environment..."
python3 -m venv .venv

# Install dependencies
echo "Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt

# Get the absolute path of the repository
REPO_DIR=$(pwd)

# Create wrapper scripts in /usr/local/bin
# This ensures the scripts run with the venv Python even if the venv isn't activated
echo "Linking commands to /usr/local/bin (requires sudo)..."
sudo tee /usr/local/bin/quran > /dev/null << EOF
#!/bin/bash
exec "$REPO_DIR/.venv/bin/python3" "$REPO_DIR/quran" "\$@"
EOF

sudo tee /usr/local/bin/quran_wallpaper > /dev/null << EOF
#!/bin/bash
exec "$REPO_DIR/.venv/bin/python3" "$REPO_DIR/quran_wallpaper" "\$@"
EOF

# Make the wrapper scripts executable
sudo chmod +x /usr/local/bin/quran /usr/local/bin/quran_wallpaper
chmod +x quran quran_wallpaper

# Move the data to ~/.quran/data directory
mkdir -p ~/.quran/data   # ensure the directory exists
cp -R "$(pwd)/data" ~/.quran

echo ""
echo "Installation complete! You can now use 'quran' and 'quran_wallpaper' from anywhere."
echo ""
echo "Next steps:"
echo "1. Run 'quran 23 115'"
echo "2. Run 'quran_wallpaper start' to start the wallpaper daemon"
