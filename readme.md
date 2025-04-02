# Overlay AI

Overlay AI is a PyQt5-based tool for capturing and processing screen regions. It uses `mss` for screen capture and `pytesseract` for OCR (Optical Character Recognition). This tool is designed to work across multiple monitors and perform customizable tasks on the extracted text.

---

## Features
- **Overlay Window**: Drag the semi-transparent overlay window to select a screen region.
- **Capture & Process**: Capture the selected region and process it with OCR.
- **Multi-Monitor Support**: Works across multiple monitors (ensure the overlay window is fully within one monitor).
- **Customizable Tasks**: Perform tasks like solving, improving, or explaining the extracted text.

---

## Requirements
- Python 3.8+
- PyQt5
- mss
- pytesseract
- Pillow

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/overlay-ai.git
    cd overlay-ai
    ```

2. **Install Dependencies**:
    Install the required Python libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Tesseract**:
    Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
    Add Tesseract to your system's PATH.

---

## Usage

1. **Run the Program**:
    ```bash
    python main.py
    ```

2. **Select a Region**:
    Drag the overlay window to the desired screen region. Ensure the overlay window is fully within one monitor.

3. **Capture & Process**:
    Click the "Capture & Process" button to capture the region and process it with OCR.

4. **View Results**:
    The extracted text will be displayed in a dialog box. You can perform tasks like solving, improving, or explaining the extracted text.

---

## Known Issues

- **Multi-Monitor Setups**:
    - The overlay window must be fully within a single monitor for proper capture.
    - Misaligned monitors in the display settings may cause incorrect captures.

- **No Text Found**:
    - Ensure the overlay window contains visible text before capturing.

---

## Contributing
Contributions are welcome! If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## Acknowledgments
- **PyQt5** for the GUI framework.
- **mss** for screen capturing.
- **Tesseract OCR** for text recognition.
