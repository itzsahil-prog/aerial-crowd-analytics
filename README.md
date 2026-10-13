---
title: Drone Crowd Intelligence
emoji: 🚁
colorFrom: cyan
colorTo: blue
sdk: streamlit
sdk_version: "1.45.1"
app_file: app.py
pinned: false
license: mit
---

# Drone Crowd Intelligence

An aerial crowd analytics dashboard built with Streamlit, OpenCV, and Plotly.  
Simulates drone footage with real-time crowd detection, density heatmaps, 3D visualisation, and alert tracking.

## Features

- Synthetic aerial crowd simulation with clustering
- Real YOLO person detection on uploaded video (optional)
- Heuristic content-aware crowd estimation fallback
- Bird's-eye density view and 3D surface reconstruction
- ROI-based density scoring and alert timeline
- Demo video export

## Deploy

### Streamlit Community Cloud
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aerial-crowd-analytics.streamlit.app)

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app → pick repo → `app.py`

### Hugging Face Spaces
1. Create a new Space → select **Streamlit** SDK
2. Push this repo — the front-matter above auto-configures the Space

### Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

1. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub repo
2. `Procfile` is already configured

### Render
1. Go to [render.com](https://render.com) → New Web Service → connect repo
2. Start command: `streamlit run app.py --server.port=$PORT --server.headless=true`

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Stack

- [Streamlit](https://streamlit.io)
- [OpenCV](https://opencv.org) (headless)
- [Plotly](https://plotly.com)
- [NumPy](https://numpy.org)
- [Ultralytics YOLOv8](https://ultralytics.com) *(optional — enables real detection)*

## Author

dev/creator: sahil
