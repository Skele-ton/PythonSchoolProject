import cv2


# Create initial video writer
def create_video_formatter(function_name):
    video_name = f"{function_name}_function_video.mp4"
    window_size = (640, 480)
    fps = 10

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, window_size)
    return video_writer


def add_frame(video_writer, cycle):
    # Read the frame image
    frame_path = f"plot_images/plot_{cycle}.png"
    frame = cv2.imread(frame_path)

    # Write the frame to the video
    video_writer.write(frame)


def release_video(video_writer):
    # Release the video writer and close the video file
    video_writer.release()
