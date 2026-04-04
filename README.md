# Cloud-Integrated-Media-Proxy-Engine
Cloud-Integrated Media Proxy Engine

Here I managed the environment setup and dependencies by myself.


🚀 Features

Hardware Accelerated: Optimized for Apple Silicon using h264_videotoolbox.

Automated Overlays: Dynamic filename burn-in for easy review identification.

Cloud-Ready: Lightweight output suitable for S3/Frame.io uploads.



"Install FFmpeg via Homebrew"

Open terminal and paste the code for homebrew install: 

homebrew:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

use administrator password>press enter/return to continue 

copy and paste this command to make possible find the command:

echo >> /Users/vanja/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/vanja/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv zsh)"

ckeck the version:
brew --version

open terminal and instal FFMPEG:
brew install ffmpeg


#############################
IN VS code:

Step 1: Create the Project Folder
create a fresh space for your automation tools. Run these in your terminal:

cd ~
mkdir media-automation-toolkit
cd media-automation-toolkit

step 2: Initialize Git (The "Memory")
tell your computer to start tracking this folder. This creates that hidden .git folder

git init

(You should see a message saying: "Initialized empty Git repository.")

Step 3: Move Your Files
Now, move your new Python files (ingest_tools.py and requirements.txt) into this new media-automation-toolkit folder.

Run these commands one by one in your VS Code terminal. (Make sure you have created the repository on GitHub.com first!)

# 1. Prepare the files
git add .

# 2. Save the milestone
git commit -m "feat: initial ffmpeg proxy engine with hardware acceleration"

# 3. Ensure we are on the 'main' branch
git branch -M main

# 4. Link to YOUR GitHub (Replace 'githubname' with your actual GitHub username if different)
git remote add origin https://github.com/githubame/media-automation-toolkit.git

# 5. Push to the cloud!
git push -u origin main

generating a "Review Proxy" with a burned-in filename.


