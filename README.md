## 🎬 Cloud-Integrated Media Proxy Engine

This toolkit bridges the gap between high-end film editorial workflows and cloud-native technical infrastructure. I designed this to automate the "ingest" phase of post-production, optimizing media for rapid review.

## 🚀 Engineering Highlights
* **Hardware Accelerated:** Custom FFmpeg configuration utilizing `h264_videotoolbox` for Apple Silicon (M1/M2/M3) acceleration.
* **Metadata Burn-in:** Automated Python logic to overlay source filenames, crucial for VFX and conform tracking.
* **Environment Architecture:** Built from the ground up using Homebrew for dependency management.

---

## 🛠️ Environment Setup & Installation

A professional media pipeline starts with a clean environment. 

### 1. Dependency Management (Homebrew)
Install the Homebrew package manager:
\`\`\`bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
\`\`\`

Configure the Shell Environment (ZSH):
\`\`\`bash
echo >> /Users/vanja/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv zsh)"' >> /Users/vanja/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv zsh)"
\`\`\`

### 2. Media Engine (FFmpeg)
Install the FFmpeg binary:
\`\`\`bash
brew install ffmpeg
\`\`\`



### 📂 Project Architecture
To maintain a clean repository structure:
1. **Initialize Git:** \`git init\`
2. **Stage Assets:** \`git add .\`
3. **Commit:** \`git commit -m "feat: initial ffmpeg proxy engine"\`
4. **Deploy:** \`git push -u origin main\`




💻 Technical Stack
Language: Python 3.12

Engine: FFmpeg 8.1

VCS: Git / GitHub

Target: Cloud-Native Ingest Pipelines
