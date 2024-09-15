import os
import pytesseract  # Tesseract OCR Engine installation + pip install pytesseract
from PIL import Image  # pip install pillow

def validate_path(path, folder = "./data/"):
    if len(path.split("/")) > 1:
        validated_path = path
    elif len(path.split("\\")) > 1:
        validated_path = path
    else:
        validated_path = folder + path
    return validated_path


def image_to_text(image="image.jpg", language="eng", output_file: str = None):

    folder = "./data/"
    input_path = validate_path(image, folder=folder)

    # Open the image file
    try:
        image = Image.open(input_path)
    except FileNotFoundError as er:
        print(er)
        return er


    # tesseract.exe path
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # Perform OCR using PyTesseract
    text = pytesseract.image_to_string(image, lang=language)  # lang="rus" or "rus+eng"

    # The extracted text outut
    if output_file is None:
        print(text)
    elif isinstance(output_file, str):
        output_path = validate_path(output_file, folder = folder)
        try:
            with open(output_path, mode="w", encoding="utf-8") as f:
                f.write(text)
                print(f"Done.\nOutput file path:\n{os.path.abspath(output_path)}")
        except OSError as er:
            print(er)
            return er
    
    return None


def main():
    print(f"\n{__file__.split("\\")[-1]}:")
    print("-" * 100)
    ###
    #

    ### Examples:
    image_to_text()
    # image_to_text(language="rus")

    # image_to_text(output_file="./data/example1.txt")
    # image_to_text(output_file=".\data\example2.txt")
    # image_to_text(
    #     output_file=r"D:\...\data\example3.txt"
    # )
    # image_to_text(
    #     output_file="D:/.../data/example4.txt"
    # )

    #
    ###
    print("-" * 100)


if __name__ == "__main__":
    main()
