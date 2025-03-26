from PIL import Image, ImageEnhance, ImageFilter

def apply_filter_interactive():
    # Get user inputs
    input_image = input("Enter the input image file name (e.g., example.jpg): ")
    output_image = input("Enter the output image file name (e.g., output.jpg): ")
    
    brightness_level = float(input("Enter brightness level (1.0 = no change, >1.0 = brighter, <1.0 = darker): "))
    contrast_level = float(input("Enter contrast level (1.0 = no change, >1.0 = higher contrast, <1.0 = lower contrast): "))
    blur_amount = float(input("Enter blur amount (0 = no blur, higher values = more blur): "))
    
    # Open the image
    img = Image.open(input_image)
    
    # Apply brightness adjustment
    if brightness_level != 1.0:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_level)
    
    # Apply contrast adjustment
    if contrast_level != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_level)
    
    # Apply blur
    if blur_amount > 0:
        img = img.filter(ImageFilter.GaussianBlur(blur_amount))
    
    # Save the modified image
    img.save(output_image)
    print(f"Image saved as {output_image}")

# Run the interactive version
if __name__ == "__main__":
    apply_filter_interactive()