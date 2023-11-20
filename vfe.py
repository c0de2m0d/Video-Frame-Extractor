"""EXTRACT FRAMES FROM A VIDEO"""
import os
import argparse
import numpy as np
import cv2


def extract_frames(video_path, output_folder, threshold=0.7):
    '''extract the frames'''
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open the video file: {video_path}")

    frame_count = 0
    save_count = 0
    prev_hist = None

    while True:
        # Read a frame
        success, frame = cap.read()

        # Break the loop if there are no more frames
        if not success:
            break

        # Convert frame to grayscale for histogram comparison
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray_frame], [0], None, [256], [0, 256])

        # Save the first frame and compare the rest
        if prev_hist is None or frame_count == 0:
            frame_filename = f"{output_folder}/frame_{frame_count}.jpg"
            cv2.imwrite(frame_filename, frame)
            save_count += 1
        elif prev_hist is not None:
            # Compare histograms using correlation
            similarity = cv2.compareHist(prev_hist, hist, cv2.HISTCMP_CORREL)

            # Save the frame if similarity is below the threshold
            if similarity < threshold:
                frame_filename = f"{output_folder}/frame_{frame_count}.jpg"
                cv2.imwrite(frame_filename, frame)
                save_count += 1

        prev_hist = hist
        frame_count += 1

    cap.release()
    print(f"Extracted {save_count} relevant frames out of {frame_count}\
         total frames into {output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        Extract frames with significant changes from a video.
        Usage example: python script_name.py path_to_video.mp4 output_folder --threshold (-t) 0.7
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("video_path", type=str, help="path to the video file")
    parser.add_argument("output_folder", type=str, help="folder to save the extracted frames")
    parser.add_argument("-t","--threshold", type=float, default=0.7, \
        help="threshold for frame similarity (default: 0.7)\n\
the correlation value ranging from -1 (completely different) to 1 (exactly the same)\n\
lower values mean more difference is required to save a frame.")

    args = parser.parse_args()

    try:
        extract_frames(args.video_path, args.output_folder, args.threshold)
    except Exception as e:
        print(f"Error: {e}")
