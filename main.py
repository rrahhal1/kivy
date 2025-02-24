import os
import fitz  # PyMuPDF

# Define the folder containing PDFs
pdf_folder = "mypdf"

# List all PDFs inside the folder
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

if not pdf_files:
    print("No PDF files found in the folder. Please add a PDF.")
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


# Function to parse the requirements and generate components for the app
def parse_requirements(requirements):
    app_components = {
        'text':
        [],  # Collects all text-based components (labels, descriptions)
        'input':
        [],  # Collects all input-related components (text fields, sliders)
        'button': [],  # Collects all button-related components
        'action': [],  # Collects actions (API calls, calculations, etc.)
    }

    # Parsing logic: Look for certain keywords or phrases that describe components
    if "input" in requirements.lower() or "enter" in requirements.lower():
        app_components['input'].append("TextInput")

    if "button" in requirements.lower() or "click" in requirements.lower():
        app_components['button'].append("Button")

    if "calculate" in requirements.lower() or "sum" in requirements.lower():
        app_components['action'].append("calculate")

    if "display" in requirements.lower() or "show" in requirements.lower():
        app_components['text'].append("Label")

    # You can extend this logic to cover more patterns, features, or requirements
    return app_components


# Function to generate a Kivy app based on parsed requirements
def generate_kivy_app(components):
    app_code = "from kivy.app import App\nfrom kivy.uix.label import Label\nfrom kivy.uix.textinput import TextInput\nfrom kivy.uix.button import Button\nfrom kivy.uix.boxlayout import BoxLayout\n"

    app_code += "class DynamicApp(App):\n"
    app_code += "    def build(self):\n"
    app_code += "        layout = BoxLayout(orientation='vertical')\n"

    # Generate text (Labels) based on requirements
    for text in components['text']:
        app_code += f"        label = Label(text='{text} - Dynamic content')\n"
        app_code += "        layout.add_widget(label)\n"

    # Generate inputs (TextInputs) based on requirements
    for _ in components['input']:
        app_code += "        text_input = TextInput(hint_text='Enter something')\n"
        app_code += "        layout.add_widget(text_input)\n"

    # Generate buttons based on requirements
    for _ in components['button']:
        app_code += "        button = Button(text='Click Me')\n"
        app_code += "        layout.add_widget(button)\n"

    # Action logic (e.g., calculations or API calls)
    if "calculate" in components['action']:
        app_code += """
        def calculate_sum(instance):
            # Logic for sum calculation
            print('Calculating sum...')
        """
        app_code += "        button = Button(text='Calculate Sum', on_press=calculate_sum)\n"
        app_code += "        layout.add_widget(button)\n"

    # Finalize the app
    app_code += "        return layout\n"

    app_code += "if __name__ == '__main__':\n"
    app_code += "    DynamicApp().run()\n"

    # Write generated code to a file
    with open("generated_dynamic_app.py", "w") as f:
        f.write(app_code)
    print("App code generated successfully!")


# Parse the extracted requirements
components = parse_requirements(requirements)

# Generate the app based on parsed components
generate_kivy_app(components)
