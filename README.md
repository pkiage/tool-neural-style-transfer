---
title: Fast Arbitrary Image Style Transfer
emoji: 🎨
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.17.0
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