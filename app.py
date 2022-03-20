# IMPORT LIBRARIES & FUNCTIONS
# External Libraries
import streamlit as st

# Project Functions
# - Model
from src.model.model import load_model, stylize_content_image
from src.model.utils import use_low_resource_settings, suppress_warnings

# - Data
from src.data.data import upload_image
from src.data.utils import remove_source_images

use_low_resource_settings("Yes")

suppress_warnings("Yes")

st.write("# 🖼️Neural🎨Style🖌️Transfer🖼️")

# LOAD MODEL
with st.spinner("🖌️Loading Model"):
    model = load_model()
st.success("🖌️Model Loaded")

content_image_def, style_image_def = st.columns(2)
with content_image_def:
    st.write("🖼️ Content Image: Image to style")
with style_image_def:
    st.write("🎨 Style Image: Style to transfer to content image")

content_image, style_image = st.columns(2)

# UPLOAD IMAGES
with content_image:
    ContentColumnTitle = "## 🖼️ Content Image 🖼️"
    ContentImageSelectionPrompt = "Pick a Content image"
    content_image_file = upload_image(
        ContentColumnTitle, ContentImageSelectionPrompt, "Content", "content"
    )

with style_image:
    StyleColumnTitle = "## 🎨 Style Image 🎨"
    StyleImageSelectionPrompt = "Pick a Style image"
    style_image_file = upload_image(
        StyleColumnTitle, StyleImageSelectionPrompt, "Style", "style"
    )

if None not in (content_image_file, style_image_file):
    try:
        # CLEAR IMAGES
        clear_images = st.button(
            label="🔄❌ Clear Image Cache ❌🔄",
            on_click=remove_source_images(),
        )
    except:
        pass

    # STYLIZE CONTENT IMAGE
    stylize_image = st.button("🖼️🖌️🎨 Start Neural Style Transfer 🖼️🖌️🎨")

    if stylize_image:
        final_image = stylize_content_image(model, content_image_file, style_image_file)
        st.write("# Styled Image:")
        st.image(final_image)
        try:
            remove_source_images()
        except:
            pass

else:
    st.write("Please upload content and style image to go to next step.")
