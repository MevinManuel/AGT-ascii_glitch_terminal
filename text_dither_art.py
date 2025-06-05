import random
from PIL import Image, ImageEnhance
import numpy as np
import os

def apply_crt_effect(text_art, intensity=1.0):
    """
    Apply CRT/VHS-like effects to text art
    """
    lines = text_art.split('\n')
    result = []
    
    # VHS noise characters
    noise_chars = ".:;-~= "
    
    for i, line in enumerate(lines):
        # Add scan line effect
        if i % 2 == 0:
            # Slightly dim even lines
            line = ''.join([char if char != ' ' else '.' for char in line])
        
        # Add random noise/interference
        if random.random() < 0.1 * intensity:
            noise_pos = random.randint(0, len(line)-1)
            noise_len = random.randint(1, 5)
            noise = ''.join(random.choice(noise_chars) for _ in range(noise_len))
            line = line[:noise_pos] + noise + line[noise_pos+noise_len:]
        
        # Add vertical color bleeding effect
        if random.random() < 0.05 * intensity:
            line = ''.join(['|' if random.random() < 0.2 else char for char in line])
        
        result.append(line)
    
    # Add horizontal interference lines
    for _ in range(int(3 * intensity)):
        pos = random.randint(0, len(result)-1)
        interference = ''.join(random.choice('-=~') for _ in range(len(result[0])))
        result.insert(pos, interference)
    
    return '\n'.join(result)

def get_brightness_map():
    """Generate a more precise brightness map for ASCII characters"""
    return {
        ' ': 0.0,    '.': 0.10,   '`': 0.15,   ',': 0.20,   ':': 0.25,   
        ';': 0.30,   '!': 0.35,   'i': 0.40,   '|': 0.45,   'r': 0.50,
        't': 0.55,   'f': 0.60,   'n': 0.65,   'v': 0.70,   'c': 0.75,
        'z': 0.80,   'Y': 0.85,   'U': 0.87,   'J': 0.90,   'C': 0.92,
        'L': 0.95,   'Q': 1.0,    '0': 0.96,   'O': 0.98,   'Z': 0.99,
        'm': 0.75,   'w': 0.80,   'q': 0.85,   'p': 0.90,   'd': 0.95,
        'b': 0.80,   'k': 0.85,   'h': 0.90,   'a': 0.85,   'o': 0.90,
        '*': 0.95,   '#': 0.98,   'M': 0.99,   'W': 1.0,    '&': 0.98,
        '8': 0.95,   '%': 0.98,   'B': 0.99,   '@': 1.0,    '$': 0.98
    }

def detailed_text_dither(image_path, output_width=300, invert=False, contrast=1.8, sharpness=1.5):
    """Convert an image to highly detailed text dither art"""
    try:
        img = Image.open(image_path).convert('L')
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Sharpness(img).enhance(sharpness)
    except IOError:
        print(f"Error: Could not open image file '{image_path}'")
        return None
    
    aspect_ratio = img.height / img.width
    output_height = int(output_width * aspect_ratio * 0.42)
    img = img.resize((output_width, output_height), Image.Resampling.LANCZOS)
    
    img_array = np.array(img, dtype=float) / 255.0
    if invert:
        img_array = 1 - img_array
    
    brightness_map = get_brightness_map()
    chars = list(brightness_map.keys())
    brightness_levels = list(brightness_map.values())
    
    # Apply Sierra dithering
    for y in range(output_height-2):
        for x in range(1, output_width-2):
            old_pixel = img_array[y, x]
            nearest_idx = min(range(len(brightness_levels)), 
                            key=lambda i: abs(brightness_levels[i] - old_pixel))
            new_pixel = brightness_levels[nearest_idx]
            img_array[y, x] = new_pixel
            error = old_pixel - new_pixel
            
            # Sierra dithering pattern
            if x < output_width-2:
                img_array[y, x+1] += error * 5/32
                img_array[y, x+2] += error * 3/32
            if y < output_height-2:
                if x >= 2:
                    img_array[y+1, x-2] += error * 2/32
                if x >= 1:
                    img_array[y+1, x-1] += error * 4/32
                img_array[y+1, x] += error * 5/32
                if x < output_width-1:
                    img_array[y+1, x+1] += error * 4/32
                if x < output_width-2:
                    img_array[y+1, x+2] += error * 2/32
                if x >= 1 and y < output_height-2:
                    img_array[y+2, x-1] += error * 2/32
                    img_array[y+2, x] += error * 3/32
                    if x < output_width-1:
                        img_array[y+2, x+1] += error * 2/32
    
    # Convert to text with enhanced mapping
    text_output = []
    for row in img_array:
        text_row = []
        for pixel in row:
            nearest_idx = min(range(len(brightness_levels)), 
                            key=lambda i: abs(brightness_levels[i] - pixel))
            text_row.append(chars[nearest_idx])
        text_output.append(''.join(text_row))
    
    return '\n'.join(text_output)

def save_and_preview(text_art, filename, apply_crt=False, crt_intensity=1.0):
    """Save text art to file and print a preview"""
    if apply_crt:
        text_art = apply_crt_effect(text_art, crt_intensity)
    
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text_art)
    
    # Print a preview (first 30 lines)
    print("\nPreview of the first 30 lines:")
    print("\n".join(text_art.split('\n')[:30]))
    print(f"\nFull output saved to '{filename}'")

def main():
    print("=== High Detail Text Dither Art Generator ===")
    print("Converts images to ultra-detailed text-based art\n")
    print("Tips for best results:")
    print("- Use high contrast images")
    print("- Images with clear edges work best")
    print("- Portraits and landscapes are ideal\n")
    
    image_path = input("Enter image file path (or drag file here): ").strip('"')
    
    if not os.path.exists(image_path):
        print(f"Error: File not found at '{image_path}'")
        return
    
    print("\nProcessing image with advanced detail settings...")
    result = detailed_text_dither(
        image_path,
        output_width=300,
        invert=False,
        contrast=1.8,
        sharpness=1.5
    )
    
    if result:
        output_file = os.path.splitext(image_path)[0] + "_hd_dither.txt"
        save_and_preview(result, output_file, apply_crt=False, crt_intensity=1.0)

if __name__ == "__main__":
    main()