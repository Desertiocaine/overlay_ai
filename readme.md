# Overlay AI

Overlay AI is a PyQt5-based tool for capturing and processing screen regions. It uses `mss` for screen capture and `pytesseract` for OCR (Optical Character Recognition). This tool is designed to work across multi-monitor setups and allows users to capture a specific region of the screen, process it, and perform tasks like solving, improving, or explaining code.

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

   
