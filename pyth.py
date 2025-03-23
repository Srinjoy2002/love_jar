
"""
Aesthetic Python GUI (PyQt5) for Scientific Use
Layout:
 ┌───────────────────────────────────────────────────────────────────────┐
 │                               TITLE                                  │
 │                                        [LOGO]                        │
 ├───────────────┬───────────────────────────────────────┬──────────────┤
 │ CONTROL        │                LIVE FEED             │ LAST IMAGE   │
 │ [ UP ]         │ (Camera View)                       │ [VIEW DIR]   │
 │ [ DN ]         │                                     │ EMERGENCY STOP│
 │ UB [red] LB[g] │                                     │              │
 │ [Run Task]     │                                     │              │
 │ [FocusStack]   │                                     │              │
 └────────────────┴───────────────────────────────────────┴──────────────┘
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QGridLayout, QFrame, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Window Settings
        self.setWindowTitle("Microscope Control GUI")
        self.setGeometry(100, 100, 1200, 700)
        
        # Main Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # =========== TOP BAR LAYOUT ===========
        top_bar = QHBoxLayout()
        
        # Title Label
        title_label = QLabel("DEEP LEARNING + FUZZY LOGIC MICROSCOPE CONTROL")
        title_font = QFont("Arial", 16, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        
        # Logo (placeholder)
        logo_label = QLabel()
        # Use an actual image path or resource
        # e.g., pixmap = QPixmap("path/to/logo.png")
        pixmap = QPixmap(100, 50)  
        pixmap.fill(Qt.lightGray)
        logo_label.setPixmap(pixmap.scaled(100, 50, Qt.KeepAspectRatio))
        
        # Add items to top bar
        top_bar.addWidget(title_label, stretch=1)
        top_bar.addWidget(logo_label, alignment=Qt.AlignRight)
        
        # =========== LEFT CONTROL PANEL ===========
        left_panel = QVBoxLayout()
        left_panel.setSpacing(10)
        
        # Up/Down Buttons
        btn_up = QPushButton()
        btn_up.setIcon(QIcon.fromTheme("arrow-up"))  # Or setIcon(QIcon("path/to/up_arrow.png"))
        btn_up.setText(" UP")
        btn_up.setStyleSheet("background-color: #E0E0E0; font-weight: bold;")
        
        btn_down = QPushButton()
        btn_down.setIcon(QIcon.fromTheme("arrow-down"))
        btn_down.setText(" DN")
        btn_down.setStyleSheet("background-color: #E0E0E0; font-weight: bold;")
        
        # UB / LB indicators
        ub_label = QLabel("UB")
        ub_label.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        ub_label.setAlignment(Qt.AlignCenter)
        
        lb_label = QLabel("LB")
        lb_label.setStyleSheet("background-color: green; color: white; font-weight: bold;")
        lb_label.setAlignment(Qt.AlignCenter)
        
        # Buttons for tasks
        run_task_btn = QPushButton("Run Task")
        run_task_btn.setStyleSheet("background-color: #FFC107; font-weight: bold;")
        focus_stack_btn = QPushButton("Focus Stack")
        focus_stack_btn.setStyleSheet("background-color: #FFC107; font-weight: bold;")
        
        # Add items to left panel
        left_panel.addWidget(btn_up)
        left_panel.addWidget(btn_down)
        
        # UB / LB horizontally
        bounds_layout = QHBoxLayout()
        bounds_layout.addWidget(ub_label)
        bounds_layout.addWidget(lb_label)
        left_panel.addLayout(bounds_layout)
        
        left_panel.addWidget(run_task_btn)
        left_panel.addWidget(focus_stack_btn)
        left_panel.addStretch(1)  # push them up, leaving empty space at bottom
        
        # =========== CENTER LIVE FEED ===========
        live_feed_layout = QVBoxLayout()
        
        live_feed_label = QLabel("LIVE FEED")
        live_feed_label.setStyleSheet("border: 2px solid #000000; background-color: #F0F0F0;")
        live_feed_label.setAlignment(Qt.AlignCenter)
        # Large placeholder
        live_feed_label.setMinimumSize(600, 400)
        
        live_feed_layout.addWidget(live_feed_label)
        
        # =========== RIGHT PANEL ===========
        right_panel = QVBoxLayout()
        right_panel.setSpacing(10)
        
        # Last image placeholder
        last_image_label = QLabel("LAST IMAGE")
        last_image_label.setStyleSheet("border: 2px solid #000000; background-color: #F0F0F0;")
        last_image_label.setAlignment(Qt.AlignCenter)
        last_image_label.setFixedSize(200, 150)
        
        # View Directory button
        view_dir_btn = QPushButton("View Directory")
        view_dir_btn.setStyleSheet("background-color: #E0E0E0; font-weight: bold;")
        
        # Emergency Stop button
        emergency_btn = QPushButton("EMERGENCY STOP")
        emergency_btn.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        emergency_btn.setFixedHeight(50)
        
        right_panel.addWidget(last_image_label)
        right_panel.addWidget(view_dir_btn)
        right_panel.addStretch(1)
        right_panel.addWidget(emergency_btn)
        
        # =========== BOTTOM LAYOUTS COMBINATION ===========
        bottom_layout = QHBoxLayout()
        bottom_layout.addLayout(left_panel, stretch=1)
        bottom_layout.addLayout(live_feed_layout, stretch=4)
        bottom_layout.addLayout(right_panel, stretch=1)
        
        # =========== MAIN VERTICAL LAYOUT ===========
        main_layout = QVBoxLayout(central_widget)
        main_layout.addLayout(top_bar)
        
        # Horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        
        main_layout.addLayout(bottom_layout)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
