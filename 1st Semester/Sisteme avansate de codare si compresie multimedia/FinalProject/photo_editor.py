import ntpath
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from functools import partial
from img_modifier import img_helper
from img_modifier import color_filter
from PIL import ImageQt

# original img, can't be modified
_img_original = None
_img_preview = None

# constants
THUMB_BORDER_COLOR_ACTIVE = "#3893F4"
THUMB_BORDER_COLOR = "#ccc"
BTN_MIN_WIDTH = 120
THUMB_SIZE = 120


class Operations:
    # Gonna be used for undo/redo on a image processing
    def __init__(self):
        self.color_filter = None

    def reset(self):
        self.color_filter = None

    def has_changes(self):
        return self.color_filter

    def __str__(self):
        return f"color_filter: {self.color_filter}"


operations = Operations()


def _get_ratio_height(width, height, r_width):
    return int(r_width / width * height)


def _get_ratio_width(width, height, r_height):
    return int(r_height / height * width)


def _get_img_with_all_operations():
    img = _img_preview
    return img


class ActionTabs(QTabWidget):
    """Action tabs widget"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.filters_tab = FiltersTab(self)
        self.addTab(self.filters_tab, "Wavelets")
        self.setMaximumHeight(250)


class FiltersTab(QWidget):
    """Color filters widget"""
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.main_layout = QHBoxLayout()
        self.main_layout.setAlignment(Qt.AlignCenter)

        for key, val in color_filter.ColorFilters.filters.items():
            self.add_filter_thumb(key, val)

        self.setLayout(self.main_layout)

    def add_filter_thumb(self, name, title=""):
        thumb_lbl = QLabel()
        thumb_lbl.name = name
        thumb_lbl.setStyleSheet("border:2px solid #ccc;")

        thumb_lbl.setToolTip(f"Apply wavelet transformation on <b>{title}</b> image")

        thumb_lbl.setCursor(Qt.PointingHandCursor)
        thumb_lbl.setFixedSize(THUMB_SIZE, THUMB_SIZE)
        thumb_lbl.mousePressEvent = partial(self.on_filter_select, name)

        self.main_layout.addWidget(thumb_lbl)

    def on_filter_select(self, filter_name, e):
        global _img_preview
        _img_preview = img_helper.color_filter(filter_name)

        operations.color_filter = filter_name
        self.toggle_thumbs()

        self.parent.parent.place_preview_img()

    def toggle_thumbs(self):
        for thumb in self.findChildren(QLabel):
            color = THUMB_BORDER_COLOR_ACTIVE if thumb.name == operations.color_filter else THUMB_BORDER_COLOR
            thumb.setStyleSheet(f"border:2px solid {color};")


class MainLayout(QVBoxLayout):
    """Main layout"""

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.img_lbl = QLabel("<h1>Welcome!</h1>"
                              "<p> In this app we are going to be able to see the different wavelets of an image<p>"
                              "<ul><li>Horizontal detail</li>"
                              "<li>Vertical detail</li>"
                              "<li>Diagonal detail</li>"
                              "Press <b>'Next'</b> to to start<br>")
        self.img_lbl.setAlignment(Qt.AlignCenter)

        self.file_name = None

        self.img_size_lbl = None
        self.img_size_lbl = QLabel()
        self.img_size_lbl.setAlignment(Qt.AlignCenter)

        upload_btn = QPushButton("Next")
        upload_btn.setMinimumWidth(BTN_MIN_WIDTH)
        upload_btn.clicked.connect(self.on_upload)
        upload_btn.setStyleSheet("font-weight:bold;")

        self.save_btn = QPushButton("Save")
        self.save_btn.setMinimumWidth(BTN_MIN_WIDTH)
        self.save_btn.clicked.connect(self.on_save)
        self.save_btn.setEnabled(False)
        self.save_btn.setStyleSheet("font-weight:bold;")

        self.addWidget(self.img_lbl)
        self.addWidget(self.img_size_lbl)
        self.addStretch()

        self.action_tabs = ActionTabs(self)
        self.addWidget(self.action_tabs)
        self.action_tabs.setVisible(False)

        btn_layout = QHBoxLayout()
        btn_layout.setAlignment(Qt.AlignCenter)
        btn_layout.addWidget(upload_btn)
        btn_layout.addWidget(self.save_btn)

        self.addLayout(btn_layout)

    def place_preview_img(self):
        img = _get_img_with_all_operations()

        preview_pix = ImageQt.toqpixmap(img)
        self.img_lbl.setPixmap(preview_pix)

    def on_save(self):
        new_img_path, _ = QFileDialog.getSaveFileName(self.parent, "QFileDialog.getSaveFileName()",
                                                      f"ez_pz_{self.file_name}",
                                                      "Images (*.png *.jpg)")

        if new_img_path:
            img = _get_img_with_all_operations()
            img.save(new_img_path)

    def on_upload(self):
        global _img_original
        _img_original = None

        self.action_tabs.setVisible(True)

        self.update_img_size_lbl()

        for thumb in self.action_tabs.filters_tab.findChildren(QLabel):
            img_filter_preview = img_helper.color_filter(thumb.name)

            preview_pix = ImageQt.toqpixmap(img_filter_preview)
            thumb.setPixmap(preview_pix)

        self.save_btn.setEnabled(True)

    def update_img_size_lbl(self):
        self.img_size_lbl.setText(
            f"<span style='font-size:13px, margin-top:20px'>Click an image down below to see the wavelet "
            f"transformation</span>")


class EasyPzUI(QWidget):
    """Main widget"""

    def __init__(self):
        super().__init__()

        self.main_layout = MainLayout(self)
        self.setLayout(self.main_layout)

        self.setMinimumSize(600, 500)
        self.setMaximumSize(900, 900)
        self.setGeometry(600, 600, 600, 600)
        self.setWindowTitle('Wavelets')
        self.center()
        self.show()

    def center(self):
        """align window center"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        if operations.has_changes():
            reply = QMessageBox.question(self, "",
                                         "You have unsaved changes<br>Are you sure?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def resizeEvent(self, e):
        pass


class QVLine(QFrame):
    """Vertical line"""

    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
