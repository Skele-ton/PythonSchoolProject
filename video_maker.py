import cv2
import os

# Path to the directory containing the image files
image_directory = "/mnt/c/Users/natha/projects/graphs"

# Get the list of image files in the directory
image_files = sorted([file for file in os.listdir(image_directory) if file.endswith('.png')])

# Define the output video file path and properties
output_video = "output_video.mp4"
fps = 10  # Frames per second
frame_size = (640, 480)  # Width, height

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
video_writer = cv2.VideoWriter(output_video, fourcc, fps, frame_size)

# Iterate over the image files and write each frame to the video
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)

# Release the VideoWriter and close the video file
video_writer.release()