import ffmpeg
import os
from dotenv import load_dotenv

# 1. LOAD CONFIGURATION (.env file)
load_dotenv() 

# 2. THE TOOLS (The Suites)

def run_ffmpeg_proxy(input_file):
    """Generates a 720p proxy with filename burn-in using Hardware Acceleration."""
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_PROXY.mp4"

    print(f"🎬 Processing: {input_file}")

    try:
        (
            ffmpeg
            .input(input_file)
            .filter('scale', 1280, -1)
            .filter('drawtext', text=base_name, x='(w-tw)/2', y='h-40', 
                    fontsize=24, fontcolor='white', box=1, boxcolor='black@0.5')
            .output(output_file, vcodec='h264_videotoolbox', b='2M', acodec='aac')
            .overwrite_output()
            .run()
        )
        print(f"✅ Created: {output_file}")
        return output_file # We return the filename so the 'Supervisor' knows what to upload
    except ffmpeg.Error as e:
        print(f"❌ FFmpeg Error: {e.stderr.decode()}")
        return None

def upload_to_frameio(file_path):
    # This is our next project! We will add the Frame.io SDK code here.
    print(f"🎬 [MOCK] Sending {file_path} to Frame.io for Review...")

def upload_to_s3(file_path):
    # This is for your AWS S3 integration.
    print(f"☁️ [MOCK] Uploading {file_path} to AWS S3 Storage...")

# 3. THE LOGIC (The Supervisor)

def main():
    # Replace 'test_video.mov' with a real file on your Mac to test
    input_video = "test_video.mov" 
    
    if not os.path.exists(input_video):
        print(f"⚠️ File '{input_video}' not found. Please check the path.")
        return

    # Phase 1: Create the Proxy
    proxy_result = run_ffmpeg_proxy(input_video)
    
    # Phase 2: Deliver the Proxy
    if proxy_result:
        destination = os.getenv("EXPORT_DESTINATION")

        if destination == "FRAMEIO":
            upload_to_frameio(proxy_result)
        elif destination == "S3":
            upload_to_s3(proxy_result)
        else:
            print(f"📂 Process Complete. Local proxy saved: {proxy_result}")

# 4. START THE SCRIPT
if __name__ == "__main__":
    main()
    