# Video Frame Extractor

This Python script extracts frames from a video file, focusing on frames that show significant changes from the previous ones. It's particularly useful for reducing redundancy in frame extraction, ensuring only distinct frames are saved.

## Features

- **Frame Difference Detection**: Extracts frames based on histogram differences to identify significant changes.
- **Customizable Threshold**: Allows setting a threshold for frame extraction to control sensitivity.
- **First Frame Inclusion**: Ensures the first frame of the video is always extracted.
- **Command Line Interface**: Easy-to-use command line arguments for input video, output directory, and threshold setting.

## Requirements

- Python 3
- OpenCV library for Python
- NumPy

## Installation

1. Ensure Python 3 is installed on your system.
2. Install OpenCV and NumPy using pip:

   ```bash
   pip install opencv-python numpy
   ```

## Usage

Run the script from the command line, providing the path to the video file, the output directory for frames, and an optional threshold value.

```bash
python vfe.py path_to_video.mp4 output_folder [--threshold THRESHOLD]
```

- `path_to_video.mp4`: Path to the input video file.
- `output_folder`: Directory where extracted frames will be saved.
- `--threshold` or `-t`: (Optional) Threshold for frame similarity. Default is 0.7.

### Example

```bash
python vfe.py my_video.mp4 extracted_frames -t 0.5
```

This command extracts frames from `my_video.mp4`, saving them to the `extracted_frames` folder, with a threshold of 0.5 for frame similarity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Show Your Support

If you found this project helpful or interesting, please give it a star :star: to show your support!
