# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_dataset_input.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QWidget)

from modules.CollapsibleWidget import CollapsibleWidget
from modules.DragDropLineEdit import DragDropLineEdit
from modules.ScrollOnSelect import (ComboBox, SpinBox)

class Ui_sub_dataset_input(object):
    def setupUi(self, sub_dataset_input):
        if not sub_dataset_input.objectName():
            sub_dataset_input.setObjectName(u"sub_dataset_input")
        sub_dataset_input.resize(523, 221)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sub_dataset_input.sizePolicy().hasHeightForWidth())
        sub_dataset_input.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(sub_dataset_input)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 0)
        self.image_dir_grid = QGridLayout()
        self.image_dir_grid.setObjectName(u"image_dir_grid")
        self.image_dir_grid.setHorizontalSpacing(8)
        self.image_folder_selector = QPushButton(sub_dataset_input)
        self.image_folder_selector.setObjectName(u"image_folder_selector")

        self.image_dir_grid.addWidget(self.image_folder_selector, 1, 1, 1, 1)

        self.Input_image_dir_label = QLabel(sub_dataset_input)
        self.Input_image_dir_label.setObjectName(u"Input_image_dir_label")

        self.image_dir_grid.addWidget(self.Input_image_dir_label, 0, 0, 1, 2)

        self.image_folder_input = DragDropLineEdit(sub_dataset_input)
        self.image_folder_input.setObjectName(u"image_folder_input")

        self.image_dir_grid.addWidget(self.image_folder_input, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.image_dir_grid, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.flip_augment_enable = QCheckBox(sub_dataset_input)
        self.flip_augment_enable.setObjectName(u"flip_augment_enable")

        self.gridLayout_2.addWidget(self.flip_augment_enable, 0, 1, 1, 1, Qt.AlignLeft)

        self.shuffle_captions_enable = QCheckBox(sub_dataset_input)
        self.shuffle_captions_enable.setObjectName(u"shuffle_captions_enable")

        self.gridLayout_2.addWidget(self.shuffle_captions_enable, 0, 0, 1, 1, Qt.AlignLeft)

        self.random_crop_enable = QCheckBox(sub_dataset_input)
        self.random_crop_enable.setObjectName(u"random_crop_enable")

        self.gridLayout_2.addWidget(self.random_crop_enable, 1, 1, 1, 1, Qt.AlignLeft)

        self.color_augment_enable = QCheckBox(sub_dataset_input)
        self.color_augment_enable.setObjectName(u"color_augment_enable")

        self.gridLayout_2.addWidget(self.color_augment_enable, 1, 0, 1, 1, Qt.AlignLeft)

        self.regularization_images_enable = QCheckBox(sub_dataset_input)
        self.regularization_images_enable.setObjectName(u"regularization_images_enable")

        self.gridLayout_2.addWidget(self.regularization_images_enable, 2, 0, 1, 2, Qt.AlignLeft)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        self.other_form_layout = QFormLayout()
        self.other_form_layout.setObjectName(u"other_form_layout")
        self.other_form_layout.setHorizontalSpacing(12)
        self.repeats_label = QLabel(sub_dataset_input)
        self.repeats_label.setObjectName(u"repeats_label")

        self.other_form_layout.setWidget(0, QFormLayout.LabelRole, self.repeats_label)

        self.repeats_input = SpinBox(sub_dataset_input)
        self.repeats_input.setObjectName(u"repeats_input")
        self.repeats_input.setMaximumSize(QSize(16777215, 16777215))
        self.repeats_input.setFocusPolicy(Qt.StrongFocus)
        self.repeats_input.setMinimum(1)
        self.repeats_input.setMaximum(16777215)

        self.other_form_layout.setWidget(0, QFormLayout.FieldRole, self.repeats_input)

        self.keep_tokens_label = QLabel(sub_dataset_input)
        self.keep_tokens_label.setObjectName(u"keep_tokens_label")

        self.other_form_layout.setWidget(1, QFormLayout.LabelRole, self.keep_tokens_label)

        self.keep_tokens_input = SpinBox(sub_dataset_input)
        self.keep_tokens_input.setObjectName(u"keep_tokens_input")
        self.keep_tokens_input.setMaximumSize(QSize(16777215, 16777215))
        self.keep_tokens_input.setFocusPolicy(Qt.StrongFocus)
        self.keep_tokens_input.setMinimum(1)
        self.keep_tokens_input.setMaximum(16777215)

        self.other_form_layout.setWidget(1, QFormLayout.FieldRole, self.keep_tokens_input)

        self.caption_label = QLabel(sub_dataset_input)
        self.caption_label.setObjectName(u"caption_label")

        self.other_form_layout.setWidget(2, QFormLayout.LabelRole, self.caption_label)

        self.caption_extension_selector = ComboBox(sub_dataset_input)
        self.caption_extension_selector.addItem("")
        self.caption_extension_selector.addItem("")
        self.caption_extension_selector.setObjectName(u"caption_extension_selector")
        self.caption_extension_selector.setFocusPolicy(Qt.StrongFocus)

        self.other_form_layout.setWidget(2, QFormLayout.FieldRole, self.caption_extension_selector)


        self.gridLayout.addLayout(self.other_form_layout, 2, 0, 1, 1)

        self.extra_args = CollapsibleWidget(sub_dataset_input)
        self.extra_args.setObjectName(u"extra_args")

        self.gridLayout.addWidget(self.extra_args, 4, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.masked_image_input = DragDropLineEdit(sub_dataset_input)
        self.masked_image_input.setObjectName(u"masked_image_input")
        self.masked_image_input.setEnabled(False)

        self.gridLayout_3.addWidget(self.masked_image_input, 1, 0, 1, 1)

        self.masked_image_selector = QPushButton(sub_dataset_input)
        self.masked_image_selector.setObjectName(u"masked_image_selector")
        self.masked_image_selector.setEnabled(False)

        self.gridLayout_3.addWidget(self.masked_image_selector, 1, 1, 1, 1)

        self.label = QLabel(sub_dataset_input)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_3, 1, 0, 1, 2)


        self.retranslateUi(sub_dataset_input)

        QMetaObject.connectSlotsByName(sub_dataset_input)
    # setupUi

    def retranslateUi(self, sub_dataset_input):
        sub_dataset_input.setWindowTitle(QCoreApplication.translate("sub_dataset_input", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.image_folder_selector.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>The folder that contains images and caption file pairs. The images and captions must be in that folder and not in folders in that folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.image_folder_selector.setText("")
#if QT_CONFIG(tooltip)
        self.Input_image_dir_label.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>The folder that contains images and caption file pairs. The images and captions must be in that folder and not in folders in that folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Input_image_dir_label.setText(QCoreApplication.translate("sub_dataset_input", u"Input Image Dir", None))
#if QT_CONFIG(tooltip)
        self.image_folder_input.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>The folder that contains images and caption file pairs. The images and captions must be in that folder and not in folders in that folder.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.image_folder_input.setPlaceholderText(QCoreApplication.translate("sub_dataset_input", u"Image Folder", None))
#if QT_CONFIG(tooltip)
        self.flip_augment_enable.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Flip Augment Flips the latents of the images during training.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.flip_augment_enable.setText(QCoreApplication.translate("sub_dataset_input", u"flip augment", None))
#if QT_CONFIG(tooltip)
        self.shuffle_captions_enable.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Shuffle Captions will shuffle the captions for each image as it appears. It shuffles according to commas</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.shuffle_captions_enable.setText(QCoreApplication.translate("sub_dataset_input", u"shuffle captions", None))
#if QT_CONFIG(tooltip)
        self.random_crop_enable.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Random Crop replaces the cropping behavior with a crop that originates from a random location of the image, instead of from the center</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.random_crop_enable.setText(QCoreApplication.translate("sub_dataset_input", u"random crop", None))
#if QT_CONFIG(tooltip)
        self.color_augment_enable.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Color Augment shifts the color of images randomly during training</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.color_augment_enable.setText(QCoreApplication.translate("sub_dataset_input", u"color augment", None))
#if QT_CONFIG(tooltip)
        self.regularization_images_enable.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Regularization Images denotes that this folder is meant to be regularization, not for direct training</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regularization_images_enable.setText(QCoreApplication.translate("sub_dataset_input", u"regularization images", None))
#if QT_CONFIG(tooltip)
        self.repeats_label.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Number of Repeats is the number of times any given image in the folder will be repeated per epoch</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.repeats_label.setText(QCoreApplication.translate("sub_dataset_input", u"Number of Repeats", None))
#if QT_CONFIG(tooltip)
        self.repeats_input.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Number of Repeats is the number of times any given image in the folder will be repeated per epoch</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.keep_tokens_label.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Keep Tokens is what allows you to prevent tokens from randomizing when shuffle captions is selected</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.keep_tokens_label.setText(QCoreApplication.translate("sub_dataset_input", u"Keep Tokens", None))
#if QT_CONFIG(tooltip)
        self.keep_tokens_input.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Keep Tokens is what allows you to prevent tokens from randomizing when shuffle captions is selected</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.caption_label.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Caption Extension is how you tell sd-scripts if your caption files are .txt or .caption</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.caption_label.setText(QCoreApplication.translate("sub_dataset_input", u"Caption Extension", None))
        self.caption_extension_selector.setItemText(0, QCoreApplication.translate("sub_dataset_input", u".txt", None))
        self.caption_extension_selector.setItemText(1, QCoreApplication.translate("sub_dataset_input", u".caption", None))

#if QT_CONFIG(tooltip)
        self.caption_extension_selector.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Caption Extension is how you tell sd-scripts if your caption files are .txt or .caption</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.masked_image_input.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Masked Image Dir is only used when masked loss is checked. This is where the masks for the images in the given folder are to be provided</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.masked_image_selector.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Masked Image Dir is only used when masked loss is checked. This is where the masks for the images in the given folder are to be provided</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.masked_image_selector.setText("")
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("sub_dataset_input", u"<html><head/><body><p>Masked Image Dir is only used when masked loss is checked. This is where the masks for the images in the given folder are to be provided</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("sub_dataset_input", u"Masked Image Dir", None))
    # retranslateUi

