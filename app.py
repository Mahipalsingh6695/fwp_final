import gradio as gr
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path

def classify_image(uploaded_file_path):
    try:
        if uploaded_file_path is not None:
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
            image = Image.open(uploaded_file_path)
            
            # Apply the transformations
            input_tensor = trans(image)
            
            # Adjust the tensor shape
            input_tensor = input_tensor.unsqueeze(0)
            
            # Perform inference
            output = model(input_tensor)
            
            # Get the prediction
            prediction = torch.argmax(output.data, 1).item()
            
            # Return the prediction
            if prediction == 0:
                return "Original"
            elif prediction == 1:
                return "Fake"
        else:
            return "No file uploaded."
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=classify_image, 
    inputs=gr.Image(type="filepath"), 
    outputs="text",
    title="Original vs Fake Classifier"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=8080, share=True)
