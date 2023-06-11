import cv2
import os


def create_video_formatter(function_name):
    video_name = "videos/" + function_name + "_function_video.mp4"
    window_size = (640, 480)
    fps = 10

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, window_size)
    return video_writer


def add_frame(video_writer, function_name):
    # Read the frame image
    frame_path = function_name + "_plot.png"
    frame = cv2.imread(frame_path)

    # Write the frame to the video
    video_writer.write(frame)

    # Remove the frame image file
    os.remove(frame_path)


def release_video(video_writer):
    # Release the VideoWriter and close the video file
    video_writer.release()
