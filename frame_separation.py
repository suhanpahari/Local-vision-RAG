import cv2
import os

def save_frames(video_path, output_folder):
    
    video_capture = cv2.VideoCapture(video_path)

    
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    
    os.makedirs(output_folder, exist_ok=True)

    
    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break  

        
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

       
        cv2.imwrite(frame_filename, frame)
        print(f"Saved: {frame_filename}")
        frame_count += 1

    
    video_capture.release()
    print(f"All frames saved in '{output_folder}'.")

video_file_path = 'video.mp4'  
output_directory = 'img'  
save_frames(video_file_path, output_directory)
