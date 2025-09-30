import replicate
import os

# Set your API token
os.environ["REPLICATE_API_TOKEN"] = "___________________________"  # Replace with your actual token

try:
    if "REPLICATE_API_TOKEN" not in os.environ:
        raise ValueError("Please set the REPLICATE_API_TOKEN environment variable")

    # Direct image URL
    image_url = "https://i.pinimg.com/1200x/2c/53/3a/2c533a83d7d78400e1daebafa93b2738.jpg" #Replace with your image URL
    
    output = replicate.run(
        "topazlabs/image-upscale",
        input={
            "image": image_url,  # Pass URL directly
            "enhance_model": "High Fidelity V2", #"Standard V2"; General Purpose; "Low Resolution V2"; Low-res images; "CGI"; for digital art, & "High Fidelity V2"; preserves detail
            "output_format": "jpg",  # "png" or "jpg"
            "upscale_factor": "None", #"None", "2x", "4x", "6x"
            "face_enhancement": True,
            "subject_detection": "Foreground", #"None", "All", "Foreground", "Background"
            "face_enhancement_strength": 0.5, #0 to 1
            "face_enhancement_creativity": 0.3 #0 to 1
        }
    )

    # To write the file to disk:
    output_path = "enhanced-image.jpg"
    with open(output_path, "wb") as file:
        file.write(output.read())
    print(f"Image saved as: {output_path}")

except ValueError as ve:
    print(f"Authentication Error: {ve}")
except Exception as e:
    print(f"Error: {str(e)}")