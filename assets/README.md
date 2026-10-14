# Sample Aerial Video

The app runs fully without a sample video — the built-in synthetic simulation starts immediately on launch.

To test with **real aerial footage**, download one of these free CC0/royalty-free clips and upload it via the sidebar **"Upload video"** option:

---

## Best free aerial crowd videos

| Source | Link | Notes |
|--------|------|-------|
| **Pexels** | [Aerial View of Crowded Outdoor Gathering](https://www.pexels.com/video/aerial-view-of-crowded-outdoor-gathering-36410760/) | Top-down, dense crowd, ideal for detection |
| **Pexels** | [Aerial View of People in a Queue](https://www.pexels.com/video/aerial-view-of-people-in-a-queue-outside-37215067/) | Drone shot, clear individual silhouettes |
| **Pexels** | [Crowd at a Concert (night aerial)](https://www.pexels.com/video/light-city-landscape-people-3941289/) | Large crowd, good for density heatmap testing |
| **Pixabay** | [Search: aerial crowd people top view](https://pixabay.com/videos/search/aerial%20crowd/) | Many free CC0 clips, no account needed |

All Pexels and Pixabay videos are free to use (CC0 / Pexels License). No attribution required.

---

## Auto-download script

Run this from the project root to download a sample clip automatically:

```bash
python assets/download_sample.py
```

The script saves `assets/sample_aerial.mp4` which you can then upload in the app sidebar.
