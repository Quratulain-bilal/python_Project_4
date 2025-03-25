import os

# STEP 1: Set your folder path and new name pattern
folder = "C:/Users/YourName/Pictures"  # ← Change this
prefix = "vacation"                   # ← Change this

# STEP 2: Run the script
for i, filename in enumerate(os.listdir(folder)):
    # Get file extension (.jpg, .png etc.)
    ext = os.path.splitext(filename)[1]
    
    # Create new name (vacation_1.jpg, vacation_2.png etc.)
    new_name = f"{prefix}_{i+1}{ext}"
    
    # Rename the file
    os.rename(
        os.path.join(folder, filename),
        os.path.join(folder, new_name)
    )
    
    print(f"Renamed {filename} to {new_name}")