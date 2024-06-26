from PIL import Image
import os
import traceback

def main():
    try:
        # Set the working directory to the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)
        print(f"Working directory set to: {script_dir}")

        input("Press Enter to start...")

        # Define valid image extensions
        valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        
        # Get all image files in the current directory
        image_files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
        print(f"Found {len(image_files)} image files: {image_files}")

        # Sort files to maintain a consistent order
        image_files.sort()
        input("Press Enter 1...")

        # Load images
        images = []
        for img in image_files:
            try:
                image = Image.open(img)
                images.append(image)
                print(f"Loaded image: {img} (size: {image.size})")
            except Exception as e:
                print(f"Failed to load image {img}: {e}")
        input("Press Enter 2...")

        # Check if there are valid images to process
        if not images:
            print("No valid images found to process.")
            input("Press Enter to exit...")
            return

        # Calculate the total height and the maximum width
        total_height = sum(img.height for img in images)
        max_width = max(img.width for img in images)
        print(f"Total height: {total_height}, Max width: {max_width}")
        input("Press Enter 3...")

        # Create a new image with the appropriate size
        stitched_image = Image.new('RGB', (max_width, total_height))
        print("Created new blank image for stitching.")
        input("Press Enter 4...")

        # Paste all images into the new image
        current_height = 0
        for img in images:
            stitched_image.paste(img, (0, current_height))
            print(f"Pasted image at height: {current_height}")
            current_height += img.height
        input("Press Enter 5...")

        # Save the resulting image
        try:
            stitched_image.save('stitched_image.jpg')
            print("Images have been stitched together and saved as 'stitched_image.jpg'")
        except Exception as e:
            print(f"Failed to save the stitched image: {e}")
            traceback.print_exc()
        
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()
    finally:
        # Keep the command prompt window open
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
