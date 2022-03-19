import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub

from ..image_utils import tensor_to_image


@st.cache
def load_model():
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    # return hub_model
    return hub.load(hub_handle)
    


def stylize_content_image(model, content_image_file, style_image_file):
    try:
        stylized_image = model(tf.constant(
            content_image_file), tf.constant(style_image_file))[0]
        return tensor_to_image(stylized_image)  # stylized image
    except:
        stylized_image = model(tf.constant(
            tf.convert_to_tensor(content_image_file[:, :, :, :3])
        ),
            tf.constant(
                tf.convert_to_tensor(style_image_file[:, :, :, :3])
        )
        )[0]
        return tensor_to_image(stylized_image)  # stylized image
