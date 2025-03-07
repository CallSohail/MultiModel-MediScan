# MediScan AI: Virtual Health Assistant

Welcome to **MediScan AI**, a virtual health assistant that combines medical image analysis and speech recognition to help diagnose potential health issues. The system uses advanced AI models to analyze medical images and transcribe patient symptoms from audio. The goal is to provide educational insights and assistance, mimicking the interaction between a patient and a doctor.

## Features

- **Speech-to-Text**: Converts spoken patient descriptions into text for analysis.
- **Image Analysis**: Analyzes medical images (e.g., facial images) for potential health issues.
- **Text-to-Speech**: Provides spoken responses from the AI doctor.
- **Multimodal Processing**: Handles both audio and image inputs simultaneously.

## Components

1. **Voice-to-Text**: Uses the `groq` API to convert recorded audio into text.
2. **Image Analysis**: Utilizes Groq’s multimodal model to analyze images with queries.
3. **Text-to-Speech**: Converts the AI doctor's diagnosis into spoken language using either **Google Text-to-Speech (gTTS)** or **ElevenLabs API**.
4. **Gradio Interface**: Provides an interactive user interface to record symptoms and upload images.

## Setup

### Prerequisites

1. Python 3.x
2. Pip (Python's package installer)
3. Environment variables for APIs:
   - **GROQ_API_KEY** for Groq API access (for audio transcription and image analysis)
   - **ELEVENLABS_API_KEY** for ElevenLabs Text-to-Speech API

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mediscan-ai.git
   cd mediscan-ai
   

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:

   ```bash
   GROQ_API_KEY=your_groq_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

### Requirements

- **Groq**: A powerful model for speech-to-text and multimodal image analysis.
- **Google Text-to-Speech (gTTS)**: Converts text to speech using Google’s API.
- **ElevenLabs API**: Another option for generating speech from text with enhanced quality.

Install the necessary packages with the following command:

```bash
pip install gradio groq gtts elevenlabs SpeechRecognition pydub
```

### File Structure

- `main.py`: Main entry point for running the Gradio interface.
- `brain_of_the_doctor.py`: Contains image analysis functions using the Groq API.
- `voice_of_the_patient.py`: Handles recording and transcribing audio from the patient.
- `voice_of_the_doctor.py`: Generates text-to-speech responses from the doctor.
- `.env`: Stores environment variables like API keys.

### Running the Application

Once everything is set up, run the application using:

```bash
python gradio_app.py
```

This will launch the Gradio interface in your browser. You can then record audio, upload medical images, and receive a diagnosis from the AI doctor.

### How It Works

1. **Record Audio**: You can describe your symptoms, and the system will convert your speech to text.
2. **Upload Image**: Upload any medical image (e.g., a facial image) for analysis. The system will analyze the image for potential issues.
3. **Diagnosis**: The AI doctor will analyze both the symptoms (from the audio) and the image and generate a diagnosis, which will be provided both in text form and as a spoken response.

### Example Use Case

- **Patient**: "I have a rash on my face, and it's painful."
- **AI Doctor Response**: Based on the image of the rash, the AI might suggest, "With what I see, I think you have a skin infection, possibly eczema. You should apply a hydrocortisone cream and consult with a dermatologist."

## Customizing the System

You can easily modify the system to work with other APIs, models, or custom functionalities. You can change the following:

- **Speech-to-Text Model**: If you'd like to use a different model for speech recognition, modify the `transcribe_with_groq` function.
- **Image Analysis Model**: The `analyze_image_with_query` function uses a specific Groq model. You can change the model for different use cases or image types.
- **Text-to-Speech Service**: You can switch between Google’s gTTS and ElevenLabs by calling the respective function (`text_to_speech_with_gtts` or `text_to_speech_with_elevenlabs`).

## License

This project is for educational purposes only. The AI doctor mimics a real doctor's behavior but is not a replacement for professional medical advice.

## Acknowledgments

- **Groq** for providing powerful multimodal models.
- **Google Text-to-Speech (gTTS)** and **ElevenLabs** for providing text-to-speech functionality.
- **Gradio** for creating an easy-to-use user interface.
