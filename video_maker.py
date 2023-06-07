import cv2
import os


def create_video_formatter(video_name, fps, window_size):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, window_size)
    return video_writer


def add_frame(video_writer):
    # Read the frame image
    frame_path = "sine_plot.png"
    frame = cv2.imread(frame_path)

    # Write the frame to the video
    video_writer.write(frame)

    # Remove the frame image file
    os.remove(frame_path)


def release_video(video_writer):
    # Release the VideoWriter and close the video file
    video_writer.release()
