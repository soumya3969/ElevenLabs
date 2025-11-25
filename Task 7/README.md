# Image Resizer Tool

A Python script for batch resizing and converting images with support for multiple formats and aspect ratio preservation.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pillow](https://img.shields.io/badge/Pillow-10.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- ✅ Batch process multiple images at once
- ✅ Resize to custom dimensions
- ✅ Maintain or ignore aspect ratio
- ✅ Convert between formats (PNG, JPEG, WebP, etc.)
- ✅ Support for common image formats
- ✅ Interactive command-line interface
- ✅ Progress tracking and error handling

## Installation

1. Install Python 3.8 or higher

2. Install required packages:
```bash
pip install -r requirements.txt
```

Or install Pillow directly:
```bash
pip install Pillow
```

## Usage

### Basic Usage

1. Create an `images` folder and add images to resize:
```bash
mkdir images
# Add your images to the images/ folder
```

2. Run the script:
```bash
python image_resizer.py
```

3. Follow the interactive prompts to:
   - Set target width and height
   - Choose whether to maintain aspect ratio
   - Select resize or format conversion

### Advanced Usage

You can also use the `ImageResizer` class directly in your code:

```python
from image_resizer import ImageResizer

# Resize images
resizer = ImageResizer(
    input_folder='images',
    output_folder='output',
    width=1920,
    height=1080,
    maintain_aspect=True
)
resizer.batch_resize()

# Convert format
resizer.convert_format('PNG')
```

## Supported Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- GIF (.gif)
- WebP (.webp)
- TIFF (.tiff)

## Project Structure

```
Task 7/
├── image_resizer.py    # Main script
├── requirements.txt    # Dependencies
├── README.md          # Documentation
├── images/            # Input folder (create this)
└── output/            # Output folder (auto-created)
```

## Examples

### Resize for Web

```bash
# Run the script
python image_resizer.py

# When prompted:
# Width: 1920
# Height: 1080
# Maintain aspect ratio: y
```

### Create Thumbnails

```bash
# Width: 150
# Height: 150
# Maintain aspect ratio: y
```

### Convert to WebP

```bash
# Choose option 2 (Convert format)
# Format: WEBP
```

## Features Explained

### Aspect Ratio Preservation
- **Enabled**: Images are scaled to fit within target dimensions without distortion
- **Disabled**: Images are stretched/compressed to exact dimensions

### Image Quality
- Output quality is set to 95% to maintain high quality
- Images are optimized during save for better file size

### Error Handling
- Corrupted images are skipped with error messages
- Processing continues even if some images fail
- Summary shows successful and failed operations

## Requirements

- Python 3.8+
- Pillow 10.0.0+

## 📚 Learning Resources

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Python os module](https://docs.python.org/3/library/os.html)
- [Image Processing Tutorials](https://realpython.com/image-processing-with-the-python-pillow-library/)

## 📞 Support

For issues or questions, please open an issue on the GitHub repository.

---


## License

MIT License - Feel free to use and modify!

## Author

Built as part of the ElevenLabs task series.

**Built with ❤️ using Python and Pillow**