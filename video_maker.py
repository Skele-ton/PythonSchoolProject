import cv2
import os


def make_video(fps, video_name, window_size, epochs):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, window_size)

# Write each frame to the video
    for epoch in range(epochs):
        # Read the frame image
        frame_path = f"sine_plot_{epoch:04d}.png"
        frame = cv2.imread(frame_path)

        # Write the frame to the video
        video_writer.write(frame)

        # Remove the frame image file
        os.remove(frame_path)

# Release the VideoWriter and close the video file
    video_writer.release()
