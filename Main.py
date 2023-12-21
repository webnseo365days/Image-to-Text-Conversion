# Imports the OpenCV library, which is a popular computer vision library used for image processing tasks.
import cv2
# Imports the pytesseract library, which is a Python wrapper for Google's Tesseract-OCR Engine. It allows you to use Tesseract for optical character recognition (OCR) in Python.
import pytesseract
# Specifies the path of the image file to be processed. In this case, it's a JPEG image file named "2.jpg."
image_path = "2.jpg"
# Reads the image from the specified file path using OpenCV's imread function and stores it in the variable image. The image is loaded as a NumPy array.
image = cv2.imread(image_path)
# Sets the path to the Tesseract executable. This line is necessary for pytesseract to locate the Tesseract OCR engine on your system. Adjust the path accordingly.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Converts the loaded color image (image) to grayscale using the OpenCV function cvtColor. Grayscale images are often used for text extraction because they simplify the data.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Uses pytesseract to perform OCR on the grayscale image (gray_image) and extracts the text. The extracted text is stored in the variable text.
text = pytesseract.image_to_string(gray_image)
# Prints the header "Extracted Text:" to the console
print("Extracted Text:")
#  Prints the extracted text obtained from OCR to the console.
print(text)
