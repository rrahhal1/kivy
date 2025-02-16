import os
import fitz  # PyMuPDF

# Define the folder containing PDFs
pdf_folder = "mypdf"

# List all PDFs inside "myfolder"
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

if not pdf_files:
    print("No PDF files found in 'myfolder'. Please add a PDF.")
    exit()

# Display available PDFs
print("Available PDF files:")
for i, file in enumerate(pdf_files):
    print(f"{i+1}. {file}")

# Let the user select a file
choice = int(input("Select a file (enter number): ")) - 1
pdf_path = os.path.join(pdf_folder, pdf_files[choice])  # Full path

print(f"Using file: {pdf_path}")


# Function to extract text from the PDF
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text("text") for page in doc)
    return text


# Extract requirements from selected PDF
requirements = extract_text(pdf_path)
print(f"Extracted Requirements:\n{requirements}")


# Function to generate a Kivy app dynamically
def generate_kivy_app(requirements):
    with open("generated_app.py", "w") as f:
        f.write(f"""
from kivy.app import App
from kivy.uix.label import Label

class GeneratedApp(App):
    def build(self):
        return Label(text="{requirements}")

if __name__ == "__main__":
    GeneratedApp().run()
""")
    print("App code generated successfully!")


# Generate the app with extracted requirements
generate_kivy_app(requirements)
