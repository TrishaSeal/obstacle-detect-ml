import cv2
import os

def convert_video_to_jpg(video_path, target_directory):
	# Open the video file
	video = cv2.VideoCapture(video_path)

	# Check if the video file was opened successfully
	if not video.isOpened():
		print("Error opening video file")
		return

	# Create output directory if it doesn't exist
	os.makedirs(target_directory, exist_ok=True)

	# Initialize variables
	frame_count = 0
	skip_counter = 60

	# Read video frames and save as JPG images
	while True:
		# Read the next frame
		success, frame = video.read()

		# If no more frames are available, exit the loop
		if not success:
			break

		# Construct the output image path
		if skip_counter < 0:
			output_path = os.path.join(target_directory, f"frame{frame_count}.jpg")
			cv2.imwrite(output_path, frame)
			frame_count += 1
			skip_counter = 60
			print("Frame:", frame_count, "processed")

		# Increment the frame count
		skip_counter -= 1
		

	# Release the video object and close the output window
	video.release()

# Example usage
video_path = "/run/media/darshk/OS/Users/darsh/Videos/Forza Horizon 4/Forza Horizon 4 2023.06.22 - 22.31.48.04.mp4"
output_directory = "../Dataset/Testing Frames"

convert_video_to_jpg(video_path, output_directory)