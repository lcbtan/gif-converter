# GIF Converter

A simple video file converter to gif using Python.

Rationale: Hate having to do a lot of manual steps to screenshot in mac and convert a mov file to gif

## Prerequisites

Before running this project, make sure you have the following prerequisites installed:

- Python (version 3.12.5)
- Pip (version 24.1.2)

Disclaimer: This project was built with these prerequisites and was not tested for lower and/or higher versions of the mentioned tools/technologies. 
## Installation

1. Clone the repository:

```bash
git clone https://github.com/lcbtan/gif-converter.git
```

2. Navigate to the project directory:

```bash
cd gif-converter
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To convert a video file to gif, you have two options:

### Option 1: Python Command

1. Activate the virtual environment.
2. Run the following command:

```bash
python gif-converter.py /path/to/your/video
```

To see further flags and help, type `-h` after the command.

The output file will be saved in the same directory as the input video file, with the same name but with a `.gif` extension.

### Option 2: Bash File

1. Make sure the bash file is set to executable. If not, run the following command:

```bash
chmod +x gif-converter.sh
```

2. Run the bash file using the following command:

```bash
./gif-converter.sh /path/to/your/video
```

The output file will be saved in the same directory as the input video file, with the same name but with a `.gif` extension.


### Convert latest video

To convert the latest video, follow these steps:

1. Set the `VIDEO_DIRECTORY` environment variable with the path of where to look for the videos.

2. Type the following command to convert only the latest video in the directory:

```bash
python gif-converter.py
```

Alternatively, you can specify the number of videos to be converted starting from the latest to the nth latest by using the following command:

```bash
python gif-converter.py n
```

Remember to replace `n` with the desired number.

The output file(s) will be saved in the same directory as the input video file(s), with the same name(s) but with a `.gif` extension.


## License

This project is licensed under the [MIT License](LICENSE).
