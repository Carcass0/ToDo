from utils import resource_path

SCROLL_AREA_STYLESHEET = """
        QScrollArea {
        border: none;
        }

        QScrollBar:vertical {
            background: #f0f0f0;
            width: 12px;
        }

        QScrollBar::handle:vertical {
            background: #c0c0c0;
            min-height: 30px;
        }

        QScrollBar::add-line:vertical {
            height: 20px;
            subcontrol-position: bottom;
        }

        QScrollBar::sub-line:vertical {
            height: 20px;
            subcontrol-position: top;
        }
        """

MAIN_WINDOW_STYLESHEET=f"""
        font: 12pt "SegoeUI";
        QCheckBox::indicator:checked
        {{
            image: url({resource_path("checkmark.png")});
        }}
        QCheckBox::indicator:unchecked
        {{
            image: url({resource_path("checkmark_unchecked.png")});
        }}
"""