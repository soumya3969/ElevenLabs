"""
Image Resizer Tool
Batch resize and convert images in a folder
"""

import os
import sys
from PIL import Image
from pathlib import Path


class ImageResizer:
    """Class to handle batch image resizing operations"""
    
    # Supported image formats
    SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp', '.tiff')
    
    def __init__(self, input_folder, output_folder, width=800, height=600, maintain_aspect=True):
        """
        Initialize the Image Resizer
        
        Args:
            input_folder: Path to input images folder
            output_folder: Path to output folder for resized images
            width: Target width in pixels
            height: Target height in pixels
            maintain_aspect: Whether to maintain aspect ratio
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.width = width
        self.height = height
        self.maintain_aspect = maintain_aspect
        self.processed_count = 0
        self.error_count = 0
        
    def get_image_files(self):
        """
        Get all image files from input folder
        
        Returns:
            List of image file paths
        """
        if not os.path.exists(self.input_folder):
            print(f"Error: Input folder '{self.input_folder}' does not exist!")
            return []
        
        image_files = []
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(self.SUPPORTED_FORMATS):
                image_files.append(filename)
        
        return image_files
    
    def resize_image(self, input_path, output_path):
        """
        Resize a single image
        
        Args:
            input_path: Path to input image
            output_path: Path to save resized image
        """
        try:
            with Image.open(input_path) as img:
                # Get original dimensions
                original_width, original_height = img.size
                print(f"  Original size: {original_width}x{original_height}")
                
                if self.maintain_aspect:
                    # Maintain aspect ratio using thumbnail
                    img.thumbnail((self.width, self.height), Image.Resampling.LANCZOS)
                    new_width, new_height = img.size
                else:
                    # Resize to exact dimensions (may distort)
                    img = img.resize((self.width, self.height), Image.Resampling.LANCZOS)
                    new_width, new_height = self.width, self.height
                
                # Save the resized image
                img.save(output_path, quality=95, optimize=True)
                print(f"  Resized to: {new_width}x{new_height}")
                print(f"  Saved: {output_path}")
                
                self.processed_count += 1
                
        except Exception as e:
            print(f"  Error processing image: {str(e)}")
            self.error_count += 1
    
    def batch_resize(self):
        """
        Process all images in the input folder
        """
        # Create output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)
        
        # Get all image files
        image_files = self.get_image_files()
        
        if not image_files:
            print("No image files found in the input folder!")
            return
        
        print(f"\nFound {len(image_files)} image(s) to process")
        print(f"Target dimensions: {self.width}x{self.height}")
        print(f"Maintain aspect ratio: {self.maintain_aspect}")
        print("="*60)
        
        # Process each image
        for idx, filename in enumerate(image_files, 1):
            print(f"\n[{idx}/{len(image_files)}] Processing: {filename}")
            
            input_path = os.path.join(self.input_folder, filename)
            output_path = os.path.join(self.output_folder, filename)
            
            self.resize_image(input_path, output_path)
        
        # Print summary
        print("\n" + "="*60)
        print("PROCESSING COMPLETE")
        print("="*60)
        print(f"Successfully processed: {self.processed_count} image(s)")
        print(f"Errors encountered: {self.error_count} image(s)")
        print(f"Output folder: {self.output_folder}")
    
    def convert_format(self, output_format='PNG'):
        """
        Convert images to a different format
        
        Args:
            output_format: Target format (PNG, JPEG, WEBP, etc.)
        """
        os.makedirs(self.output_folder, exist_ok=True)
        image_files = self.get_image_files()
        
        if not image_files:
            print("No image files found!")
            return
        
        print(f"\nConverting {len(image_files)} image(s) to {output_format}")
        print("="*60)
        
        for idx, filename in enumerate(image_files, 1):
            print(f"\n[{idx}/{len(image_files)}] Converting: {filename}")
            
            input_path = os.path.join(self.input_folder, filename)
            
            # Change file extension
            name_without_ext = os.path.splitext(filename)[0]
            new_filename = f"{name_without_ext}.{output_format.lower()}"
            output_path = os.path.join(self.output_folder, new_filename)
            
            try:
                with Image.open(input_path) as img:
                    # Convert RGBA to RGB if saving as JPEG
                    if output_format.upper() == 'JPEG' and img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    img.save(output_path, format=output_format)
                    print(f"  Converted to: {new_filename}")
                    self.processed_count += 1
                    
            except Exception as e:
                print(f"  Error: {str(e)}")
                self.error_count += 1
        
        print(f"\n✓ Conversion complete: {self.processed_count} image(s)")


def main():
    """Main function to run the image resizer"""
    
    print("="*60)
    print("IMAGE RESIZER TOOL")
    print("="*60)
    
    # Default values
    input_folder = "images"
    output_folder = "output"
    width = 800
    height = 600
    maintain_aspect = True
    
    # Check if input folder exists, create example if not
    if not os.path.exists(input_folder):
        print(f"\nInput folder '{input_folder}' not found.")
        create = input("Create sample folders? (y/n): ").lower()
        if create == 'y':
            os.makedirs(input_folder, exist_ok=True)
            print(f"✓ Created '{input_folder}' folder")
            print(f"  Please add some images to the '{input_folder}' folder and run again.")
            return
        else:
            print("Exiting...")
            return
    
    # Get user preferences
    print("\nConfiguration:")
    print(f"1. Input folder: {input_folder}")
    print(f"2. Output folder: {output_folder}")
    
    try:
        width_input = input(f"\nEnter target width (default: {width}): ").strip()
        if width_input:
            width = int(width_input)
        
        height_input = input(f"Enter target height (default: {height}): ").strip()
        if height_input:
            height = int(height_input)
        
        aspect_input = input("Maintain aspect ratio? (y/n, default: y): ").strip().lower()
        if aspect_input == 'n':
            maintain_aspect = False
        
    except ValueError:
        print("Invalid input! Using default values.")
    
    # Create resizer and process images
    resizer = ImageResizer(input_folder, output_folder, width, height, maintain_aspect)
    
    print("\nOptions:")
    print("1. Resize images")
    print("2. Convert format")
    
    choice = input("\nSelect option (1 or 2, default: 1): ").strip()
    
    if choice == '2':
        format_input = input("Enter target format (PNG, JPEG, WEBP, default: PNG): ").strip().upper()
        output_format = format_input if format_input else 'PNG'
        resizer.convert_format(output_format)
    else:
        resizer.batch_resize()
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
