import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtGui import QPainter, QPen
import pytesseract
import logging
import mss
from PIL import Image
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Enable DPI awareness on Windows
if sys.platform == "win32":
    from ctypes import windll
    windll.user32.SetProcessDPIAware()

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Overlay AI")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowOpacity(0.5)

        # Add a button to capture and process the region
        self.capture_button = QPushButton("Capture & Process", self)
        self.capture_button.clicked.connect(self.capture_and_process)
        self.capture_button.setGeometry(10, 10, 150, 30)  # Position the button

        self.show()

    def capture_and_process(self):
        # Calculate the bounding box in global screen coordinates
        rect = self.geometry()  # Use geometry() for the visible content
        top_left = self.mapToGlobal(rect.topLeft())
        bottom_right = self.mapToGlobal(rect.bottomRight())

        # Get monitor information from mss
        with mss.mss() as sct:
            monitors = sct.monitors[1:]  # Skip the first entry (virtual screen)
            logging.info(f"Monitors: {monitors}")

            # Find the monitor containing the overlay window
            matched_monitor = None
            for monitor in monitors:
                logging.info(f"Checking monitor: {monitor}")
                if (monitor["left"] <= top_left.x() < monitor["left"] + monitor["width"] and
                    monitor["top"] <= top_left.y() < monitor["top"] + monitor["height"]):
                    # Ensure the overlay window is fully within the monitor
                    if not (monitor["left"] <= bottom_right.x() <= monitor["left"] + monitor["width"] and
                            monitor["top"] <= bottom_right.y() <= monitor["top"] + monitor["height"]):
                        logging.error("Overlay window is not fully within a monitor. Please adjust the window.")
                        QMessageBox.critical(self, "Error", "Overlay window is not fully within a monitor. Please adjust the window.")
                        return

                    matched_monitor = monitor
                    logging.info(f"Using monitor: {monitor}")
                    bbox = {
                        "top": top_left.y() - monitor["top"],
                        "left": top_left.x() - monitor["left"],
                        "width": bottom_right.x() - top_left.x(),
                        "height": bottom_right.y() - top_left.y(),
                    }
                    break

            if not matched_monitor:
                # If no monitor matches, log an error and return
                logging.error("No matching monitor found. Ensure the overlay window is fully within a monitor.")
                QMessageBox.critical(self, "Error", "No matching monitor found. Please adjust the overlay window.")
                return

        logging.info(f"Bounding Box: {bbox}")

        try:
            # Temporarily hide the overlay window to avoid capturing it
            self.hide()
            time.sleep(0.2)  # Add a small delay to ensure the window is fully hidden

            # Capture the selected region using mss
            with mss.mss() as sct:
                screenshot = sct.grab(bbox)
                image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            # Show the overlay window again
            self.show()

            # Process the captured image with Tesseract OCR
            text = pytesseract.image_to_string(image)
            logging.info(f"Extracted Text: {text}")

            if not text.strip():
                QMessageBox.warning(self, "No Text Found", "No text was found in the captured region. "
                                                           "Ensure the overlay window contains visible text and try again.")
                return

            # Perform the desired task with the extracted text
            self.perform_task(text)

        except Exception as e:
            logging.error(f"Error during capture and process: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def perform_task(self, text):
        # Placeholder for performing a task with the extracted text
        # For example, solving, improving, or explaining the code
        result = f"Processed Text:\n{text}"
        QMessageBox.information(self, "Task Result", result)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        painter.drawRect(self.rect())  # Draw window border

    def closeEvent(self, event):
        # Stop the timer when the window is closed
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = OverlayWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()