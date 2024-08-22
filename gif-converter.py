import os
import argparse
from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import resize
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# No argument = latest in the set directory
# Bumbered argument (e.g. 2, 3) = get the nth latest screenshot in the set directory
# Argument = video file path

DEFAULT_VIDEO_DIRECTORY = os.getenv('VIDEO_DIRECTORY')


# List of valid video extensions
valid_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}

def get_latest_screenshot_file(directory: str, nth_latest: int) -> str:    
    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and os.path.splitext(f)[1] in valid_extensions]
    
    # files = [
    #   {"filename": f, "pathname": os.path.join(directory, f)}
    #   for f in os.listdir(directory)
    #   if os.path.isfile(os.path.join(directory, f))
    # ]

    # Sort files by creation time in descending order
    files.sort(key=lambda x: os.path.getctime(x), reverse=True)

    # # Get the file with the latest creation time
    files_list = files[:nth_latest]
    return files_list

def main() -> None:
  # Parse arguments
  parser = argparse.ArgumentParser(description='Convert video to gif')
  parser.add_argument('video_file', type=str, nargs='?', help='Video file path. If no argument is provided, the latest video file in the set directory will be used. If a numbered argument is provided (e.g. 2, 3), the nth latest screenshot in the set directory will be used.')
  parser.add_argument('--fps', type=int, default=10, help='Frames per second for the GIF')
  parser.add_argument('--width', type=int, default=640, help='Width of the GIF')
  parser.add_argument('--height', type=int, help='Height of the GIF')
  parser.add_argument('--duration', type=int, help='Duration of the GIF in seconds')

  args = parser.parse_args()
  
  # Get the absolute paths of the files
  video_path: str = args.video_file
  if video_path is None or video_path.isdigit():
    abs_path_of_files = get_latest_screenshot_file(os.path.expanduser(DEFAULT_VIDEO_DIRECTORY), int(video_path or 1))
  else:
    abs_path_of_files = [os.path.abspath(video_path)]

  print("Files to convert:" , abs_path_of_files)

  # Convert the videos to GIF
  for abs_path in abs_path_of_files:
    print("====================================")
    print("Converting: ", abs_path)
    clip = VideoFileClip(abs_path)

    [original_name, original_extension] = os.path.splitext(abs_path)
    gif_filename = f'{original_name}.gif'
    print("Creating Gif Filename: ", gif_filename)

    # Resize the GIF
    new_size = {}

    if args.height:
      new_size['height'] = args.height
    
    if args.width:
      new_size['width'] = args.width

    print("New Size: ", new_size)
    # In the future, use this as reference for the different functions we can put in https://zulko.github.io/moviepy/ref/videofx.html
    clip = clip.fx(resize, **new_size)

    # Trim the clip if duration is provided
    if args.duration:
      clip = clip.subclip(0, args.duration)

    clip.write_gif(gif_filename, fps=args.fps)
    original_size = os.path.getsize(abs_path) / (1024 * 1024)
    gif_size = os.path.getsize(gif_filename) / (1024 * 1024)
    print(f'Done! Converted from a {original_size:.2f} MB {original_extension} file to a {gif_size:.2f} MB GIF File!')
  
    
    


  return None


  # print('Hello, World!')
  # clip = VideoFileClip('')
  # clip.write_gif('b.gif', fps=10)
  # print('Done!')
  # return None


if __name__ == '__main__':
  main()