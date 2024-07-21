import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path

def save_image(uploaded_file):
    if uploaded_file is not None:
        # Ensure the directory exists
        os.makedirs("images", exist_ok=True)
        save_path = os.path.join("images", "input.jpeg")
        
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image saved to {save_path}")
        
        # Load the model
        model = torch.load(Path('model/model.pt'))
        
        # Define the image transformations
        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize((244, 244)),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
        ])
        
        # Open the image
        image = Image.open(save_path)
        
        # Apply the transformations
        input_tensor = trans(image)
        
        # Adjust the tensor shape
        input_tensor = input_tensor.unsqueeze(0)
        
        # Perform inference
        output = model(input_tensor)
        
        # Get the prediction
        prediction = torch.argmax(output.data, 1).item()
        print(prediction)
        
        # Display the prediction
        if prediction == 0:
            st.text_area(label="Prediction:", value="Original", height=100)
        elif prediction == 1:
            st.text_area(label="Prediction:", value="Fake", height=100)

if __name__ == "__main__":
    st.title("Original vs Fake Classifier")
    uploaded_file = st.file_uploader("Upload an image")
    save_image(uploaded_file)

