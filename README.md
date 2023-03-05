---
title: Fast Arbitrary Image Style Transfer
emoji: 🎨
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.4.0
app_file: app.py
pinned: false
license: openrail
---

# Setup and Installation
## Install Requirements
```shell
pip install -r requirements.txt
```
### Local Package Install
```shell
pip install -e .
```
### Run app locally
```shell
streamlit run app.py
```

## Hugging Face Tips

- [When syncing with Hugging Face via Github Actions](https://huggingface.co/docs/hub/spaces-github-actions) the [User Access Token](https://huggingface.co/docs/hub/security-tokens) created on Hugging Face (HF) should have write access
- [When creating the Spaces Configuration Reference](https://huggingface.co/docs/hub/spaces-config-reference) ensure the [Streamlit Space](https://huggingface.co/docs/hub/spaces-sdks-streamlit) version (sdk_version) specified is supported by HF

## Demo Links
- Hugging Face Space: https://huggingface.co/spaces/pkiage/fast_arbitrary_image_style_transfer
- Streamlit Community Cloud: https://pkiage-tool-neural-style-transfer-app-st9nqy.streamlit.app/
