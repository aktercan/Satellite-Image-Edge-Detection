# Satellite Image Edge Detection

This repository showcases a comprehensive Python-based project aimed at processing satellite images and extracting meaningful edge information using advanced image processing techniques. The pipeline is designed to handle grayscale aerial images, normalize them, reduce noise, and identify edges with precision.

## Features

- Satellite Image Normalization: Converts raw satellite image pixel values to a standard 0-255 range for meaningful visualization and further processing.
- Gaussian Blur for Noise Reduction: Smooths the image to eliminate noise and enhance edge detection accuracy.
- Canny Edge Detection: Applies one of the most robust edge detection algorithms to highlight significant boundaries in the image.
- Visualization Tools: Displays both the normalized image and the edge-detected output side by side for comparison.

## Why This Project?

Satellite image processing is a crucial aspect of remote sensing, urban planning, and environmental monitoring. This project demonstrates the potential of image processing techniques to extract valuable information from raw satellite data. Whether you're a researcher, student, or developer, this repository provides a practical example of edge detection in satellite images, an essential step for further analysis.

## How It Works

The project follows a structured pipeline:
1. **Image Loading**: The script loads a grayscale satellite image using the rasterio library.
2. **Normalization**: Ensures pixel values are in the range 0-255 for better visualization and further processing.
3. **Noise Reduction**: Applies Gaussian blur to smooth the image and suppress noise.
4. **Edge Detection**: Uses the Canny edge detector to identify boundaries in the image.
5. **Visualization**: Displays the normalized and edge-detected images side by side.

## Requirements

To run the project, ensure you have the following installed:
- Python 3.8+
- Libraries: numpy, rasterio, opencv-python, matplotlib

## Example Output

Below is an example of the processed satellite image:
- Left: Normalized Image
- Right: Detected Edges

## Challenges and Future Improvements

- Normalization Limitations: Handling images with maximum pixel values close to zero can be challenging.
- Noise Sensitivity: High-frequency noise can affect edge detection accuracy. Advanced denoising methods could further improve results.
- Scalability: Currently, the script processes one image at a time. Batch processing for multiple images is a potential improvement.

## Contribution

Feel free to fork this repository and contribute enhancements! Open a pull request with any improvements or feature additions.

## License

This project is open-source and available under the MIT License.

## Author

Created by Akifcan Tercan as part of a photogrammetric image processing project. For inquiries or collaborations, feel free to contact me via GitHub.
