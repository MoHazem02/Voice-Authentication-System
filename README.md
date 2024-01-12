# Voice Authentication System

Welcome to the Voice Authentication System repository! This Python desktop application utilizes voice fingerprint and spectrogram technology to identify individuals based on their unique vocal characteristics. The system can be trained on up to 8 individuals and operates in two distinct modes to ensure secure access.

## Features

1. **Mode 1 – Security Voice Code:**
   - Access is granted only if the user speaks a specific pass-code sentence.
   
2. **Mode 2 – Security Voice Fingerprint:**
   - Access is granted to specific individuals who say the valid pass-code sentence.
   
The program calculates matching probabilities and decides whether access should be granted or denied based on the input.

## Installation

To run the Voice Authentication System, make sure you have the following libraries installed:

```bash
pip install PyQt5 matplotlib sounddevice soundfile librosa numpy scikit-learn
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/MoHazem02/Voice-Authentication-System.git
```

2. Navigate to the project directory:

```bash
cd Voice-Authentication-System
```

3. Run the application:

```bash
python Voice_Recognizer.py
```

## Dependencies

- PyQt5
- Matplotlib
- Sounddevice
- Soundfile
- Librosa
- Numpy
- Scikit-learn

## Screenshots

You can find snapshots of the application in the "Snapshots" folder within this repository. Feel free to explore and add your own snapshots to showcase the program's functionality.

## Contributing

If you would like to contribute to the project, please follow the [contribution guidelines](CONTRIBUTING.md).

## Acknowledgments

Special thanks to the developers of the libraries used in this project.

Happy coding!
