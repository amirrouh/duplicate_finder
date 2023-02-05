import subprocess

input_file = "/Users/amir/Documents/2019-09-09-amari-johnson-zoey-pippen-1080p.mp4"
output_file = "/Users/amir/Documents/output.mp4"

def using_cpu(input_file, output_file):
    # Use the '-crf' flag to set the quality level, where lower values result in higher quality
    # and larger file sizes
    crf = 18

    # Use the '-preset' flag to set the speed/compression tradeoff, where slower settings result in
    # better compression
    preset = "medium"

    # Use the '-pix_fmt' flag to set the pixel format, which can improve compression for some videos
    pix_fmt = "yuv420p"

    # Run the ffmpeg command to compress the video
    subprocess.run(
        [
            "ffmpeg",
            "-i", input_file,
            "-c:v", "libx264",
            "-crf", str(crf),
            "-preset", preset,
            "-pix_fmt", pix_fmt,
            output_file
        ]
    )

def using_gpu(input_file, output_file):
    # Compression settings
    crf = 18 # Constant Rate Factor (0-51, lower is better quality)
    preset = 'medium' # Compression preset (faster/slower)
    gpu = 0 # GPU to use (0-indexed)

    # Compress the video using FFmpeg
    subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'h264_cuvid', '-b:v', '0', '-crf', str(crf), '-preset', preset, output_file])


using_gpu(input_file, output_file)