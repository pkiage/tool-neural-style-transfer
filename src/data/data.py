import os
import streamlit as st
import tensorflow as tf

from ..image_utils import load_img, imshow, transform_img


def upload_image_url(ImageSelectionPrompt, ImageType, image_upload_method):
    st.write(f"{ImageSelectionPrompt}: {image_upload_method}")
    url = st.text_input(f"{ImageType} Image URL")
    try:
        image_path = tf.keras.utils.get_file(
            os.path.join(os.getcwd(), f"{ImageType.lower()}.jpg"), url
        )
    except:
        pass
    try:
        return load_img(image_path)
    except:
        pass


def upload_image_file(ImageSelectionPrompt, ImageType, image_upload_method):
    st.write(f"{ImageSelectionPrompt}: {image_upload_method}")
    image_file = st.file_uploader(
        f"Upload {ImageType} Image File (png or jpg)", type=("png", "jpg")
    )
    try:
        image_file = image_file.read()
        return transform_img(image_file)
    except:
        pass


def upload_image_capture(ImageSelectionPrompt, ImageType, image_upload_method):
    st.write(f"{ImageSelectionPrompt}: {image_upload_method}")
    image_file = st.camera_input(f"Capture {ImageType} Image")
    try:
        image_file = image_file.read()
        return transform_img(image_file)
    except:
        pass


def upload_image(ColumnTitle, ImageSelectionPrompt, ImageType, KeyString):
    st.write(ColumnTitle)
    image_upload_method = st.radio(
        label="", options=["🔗 URL", "📁 File Upload", "📸 Capture"], key=KeyString
    )
    if image_upload_method == "🔗 URL":
        image_file = upload_image_url(
            ImageSelectionPrompt, ImageType, image_upload_method
        )

    if image_upload_method == "📁 File Upload":
        image_file = upload_image_file(
            ImageSelectionPrompt, ImageType, image_upload_method
        )

    if image_upload_method == "📸 Capture":
        image_file = upload_image_capture(
            ImageSelectionPrompt, ImageType, image_upload_method
        )
    try:
        st.write(f"{ImageType} Image")
        st.image(imshow(image_file))
        return image_file
    except:
        pass
