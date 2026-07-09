# Final Project

This repository contains the source code and documentation for the final project.

## About the Project

An AI-powered web application built with Flask. It utilizes the IBM Watson NLP API to analyze the emotional tone of a given text.

The application features:

- A standalone, reusable Python package called **EmotionDetection**.
- Accurate classification of 5 core emotions: anger, disgust, fear, joy, and sadness.
- Automated tracking to determine the dominant emotion of a given text input.

## Getting Started

### Prerequisites

- Python 3.XX
- `requests` library

### Running the Package Test

To verify the application package functionality directly from the terminal, execute the following command (replace the <example> placeholder with the actual input text):

```bash
python3 -c "from EmotionDetection import emotion_detector; print(emotion_detector('<example>'))"
```
