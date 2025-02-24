
import os
import fitz  # PyMuPDF
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

def extract_requirements(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_requirements(text):
    components = {
        'labels': [],    # Store text/descriptions
        'inputs': [],    # Store input fields
        'buttons': [],   # Store buttons
        'calculations': [] # Store calculation functions
    }
    
    # Basic requirement analysis
    lines = text.lower().split('\n')
    for line in lines:
        # Look for input requirements
        if any(word in line for word in ['input', 'enter', 'type']):
            components['inputs'].append(line.strip())
            
        # Look for button actions
        if any(word in line for word in ['button', 'click', 'press']):
            components['buttons'].append(line.strip())
            
        # Look for calculations
        if any(word in line for word in ['calculate', 'compute', 'sum']):
            components['calculations'].append(line.strip())
            
        # Look for display requirements
        if any(word in line for word in ['display', 'show', 'output']):
            components['labels'].append(line.strip())
    
    return components

class DynamicApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Get PDF content and analyze
        pdf_folder = "mypdf"
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        
        if not pdf_files:
            layout.add_widget(Label(text="No PDF files found in 'mypdf' folder"))
            return layout
            
        pdf_path = os.path.join(pdf_folder, pdf_files[0])
        requirements_text = extract_requirements(pdf_path)
        components = analyze_requirements(requirements_text)
        
        # Create UI based on analysis
        # Add title
        layout.add_widget(Label(
            text="Dynamic App Generated from PDF Analysis",
            size_hint_y=None, height=50
        ))
        
        # Create input fields
        for input_req in components['inputs']:
            input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            input_layout.add_widget(Label(text=input_req, size_hint_x=0.3))
            input_layout.add_widget(TextInput(multiline=False, size_hint_x=0.7))
            layout.add_widget(input_layout)
            
        # Create buttons with actions
        for button_req in components['buttons']:
            btn = Button(
                text=button_req,
                size_hint_y=None,
                height=40
            )
            layout.add_widget(btn)
            
        # Add calculation results area
        if components['calculations']:
            layout.add_widget(Label(
                text="Calculation Results:",
                size_hint_y=None,
                height=30
            ))
            for calc in components['calculations']:
                layout.add_widget(Label(
                    text=calc,
                    size_hint_y=None,
                    height=30
                ))
        
        # Create scrollable output area
        scroll = ScrollView(size_hint=(1, None), size=(400, 200))
        results_label = Label(size_hint_y=None, text='Results will appear here')
        results_label.bind(width=lambda *x: setattr(results_label, 'text_size', (results_label.width, None)))
        results_label.bind(texture_size=lambda *x: setattr(results_label, 'height', results_label.texture_size[1]))
        scroll.add_widget(results_label)
        layout.add_widget(scroll)
        
        return layout

if __name__ == '__main__':
    DynamicApp().run()
