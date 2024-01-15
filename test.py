import subprocess

def run_caption_script():
    # Ask the user for the image name
    image_name = input("Enter the image name: ")

    # Construct the full path of the image
    image_path = f"C:/Users/Asus/Downloads/ImagetoCaption-Project-/ImagetoCaption-Project-/Flicker8k_Dataset/{image_name}"

    # Define the rest of the command
    command = [
        "python",
        "C:/Users/Asus/Downloads/ImagetoCaption-Project-/ImagetoCaption-Project-/caption.py",
        "--img", image_path,
        "--model", "C:/Users/Asus/Downloads/ImagetoCaption-Project-/BEST_checkpoint_flickr8k_5_cap_per_img_5_min_word_freq.pth.tar",
        "--word_map", "C:/Users/Asus/Downloads/ImagetoCaption-Project-/ImagetoCaption-Project-/Flickr8k_preprocessed/WORDMAP_flickr8k_5_cap_per_img_5_min_word_freq.json",
        "--beam_size", "5"
    ]

    print("Command" + str(command))
    # Execute the command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if there was an error
    if result.returncode != 0:
        print("Error running the command:")
        print(result.stderr)
    else:
        print("Command output:")
        print(result.stdout)

if __name__ == "__main__":
    run_caption_script()
