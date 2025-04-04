import cv2
import os
def hide_text(image_path, secret_message, output_image):
    img = cv2.imread("maa.png")
    if img is None:
        print("Error: Unable to read the image file.")
        return
    secret_message += chr(0)

    n, m, z = 0, 0, 0

    for char in secret_message:
        img[n, m, z] = ord(char)  
        z += 1
        if z == 3:  
            z = 0
            n += 1

        if n >= img.shape[0]:  
            n = 0
            m += 1
        if m >= img.shape[1]:  
            print("Message is too long to hide in this image.")
            return

    cv2.imwrite(output_image, img)
    print(f"Secret message hidden successfully in {output_image}")
    
    try:
        os.startfile(output_image)  
    except AttributeError:
        print("Automatic opening not supported on this OS. Open the image manually.")

def extract_text(image_path):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Unable to read the image file.")
        return
    
    n, m, z = 0, 0, 0
    extracted_message = ""

    while True:
        char_code = img[n, m, z]  
        if char_code == 0:  
            break
        extracted_message += chr(char_code)
        
        z += 1
        if z == 3:  
            z = 0
            n += 1

        if n >= img.shape[0]:  
            n = 0
            m += 1
        if m >= img.shape[1]:  
            break

    print("Extracted Message:", extracted_message)

def main():
    print("Steganography - Hide and Extract Text in Images")
    print("1. Hide a secret message")
    print("2. Extract the hidden message")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_image = input("Enter the input PNG image filename (e.g., input.png): ")
        secret_message = input("Enter the message to hide: ")
        output_image = input("Enter the output PNG image filename (e.g., output.png): ")
        hide_text(input_image, secret_message, output_image)
    
    elif choice == "2":
        encoded_image = input("Enter the encoded PNG image filename (e.g., output.png): ")
        extract_text(encoded_image)
    
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()


    
    
    