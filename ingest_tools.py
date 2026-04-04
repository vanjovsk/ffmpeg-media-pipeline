import ffmpeg
import os

def create_review_proxy(input_file):
    # Get the filename without the extension for the watermark
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"{base_name}_PROXY.mp4"

    print(f"🎬 Processing: {input_file}")

    try:
        (
            ffmpeg
            .input(input_file)
            # 1. Scale to 720p (standard for review)
            .filter('scale', 1280, -1)
            # 2. Burn in the filename at the bottom center
            .drawtext(text=base_name, x='(w-tw)/2', y='h-40', fontsize=24, fontcolor='white', box=1, boxcolor='black@0.5')
            # 3. Encode using Apple Hardware Acceleration (VideoToolbox)
            .output(output_file, vcodec='h264_videotoolbox', b='2M', acodec='aac')
            .overwrite_output()
            .run()
        )
        print(f"✅ Created: {output_file}")
    except ffmpeg.Error as e:
        print(f"❌ Error: {e.stderr.decode()}")

# To test this, uncomment the line below and put a video file name inside
# create_review_proxy('YOUR_VIDEO_HERE.mov')