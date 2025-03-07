from dotenv import load_dotenv
load_dotenv()

# VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_for_gradio

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                audio_filepath=audio_filepath,
                                                stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, 
                                                  encoded_image=encode_image(image_filepath), 
                                                  model="llama-3.2-11b-vision-preview")
    else:
        doctor_response = "No image provided for me to analyze"

    # Generate audio but don't try to play it - just return the path for Gradio
    audio_path = text_to_speech_for_gradio(input_text=doctor_response, output_filepath="final.mp3")

    return speech_to_text_output, doctor_response, audio_path


# Custom CSS for enhanced styling
css = """
.gradio-container {
    font-family: 'Arial', sans-serif;
    background-color: #f0f8ff;
}

.main-header {
    background-color: #fca232;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 20px;
    text-align: center;
}

.input-panel {
    background-color: #ecf0f1;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.output-panel {
    background-color: #eaf5ff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.footer {
    text-align: center;
    margin-top: 20px;
    font-size: 0.8em;
    color: #7f8c8d;
}
"""

# Create the interface with improved styling
with gr.Blocks(css=css) as iface:
    with gr.Column():
        gr.HTML("""
            <div class="main-header">
                <h1>🩺 MediScan AI: Virtual Health Assistant 🌡️</h1>
                <p>Talk to our AI doctor and upload images for medical analysis</p>
            </div>
        """)
        
        with gr.Row():
            with gr.Column(elem_classes="input-panel"):
                gr.Markdown("### 🎤 Tell us what's bothering you")
                audio_input = gr.Audio(
                    sources=["microphone"], 
                    type="filepath",
                    label="Record your symptoms"
                )
                
                gr.Markdown("### 📷 Upload an image for analysis")
                image_input = gr.Image(
                    type="filepath",
                    label="Medical image"
                )
                
                submit_btn = gr.Button("🔍 Analyze", variant="primary")
            
        with gr.Column(elem_classes="output-panel"):
            gr.Markdown("### 📝 Consultation Results")
            speech_output = gr.Textbox(label="📋 Your described symptoms")
            response_output = gr.Textbox(label="👨‍⚕️ Doctor's diagnosis")
            audio_output = gr.Audio(label="🔊 Listen to the doctor's response")
            
        gr.HTML("""
            <div class="footer">
                <p>MediScan AI is for educational purposes only. Please consult with a real healthcare professional for medical advice.</p>
            </div>
        """)
    
    # Set up the click event
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_output, response_output, audio_output]
    )

if __name__ == "__main__":
    iface.launch(debug=True, pwa=True)