# dev/creator: sahil

import numpy as np
import plotly.graph_objects as go

from config import THEME


def _density_grid(points_xy, frame_w: int, frame_h: int, grid=(24, 14)):
    gx, gy = grid
    counts = np.zeros((gy, gx), dtype=np.float32)
    if points_xy:
        cw, ch = frame_w / gx, frame_h / gy
        for x, y in points_xy:
            cx = min(int(x // cw), gx - 1)
            cy = min(int(y // ch), gy - 1)
            counts[cy, cx] += 1
    return counts


def build_3d_density_figure(
    points_xy, frame_w: int, frame_h: int,
    grid=(24, 14), mode: str = "surface",
) -> go.Figure:
    counts = _density_grid(points_xy, frame_w, frame_h, grid)
    gy, gx = counts.shape
    xs = np.linspace(0, frame_w, gx)
    ys = np.linspace(0, frame_h, gy)

    fig = go.Figure()

    if mode == "surface":
        # Use a floor value so empty/zero cells render as dark background,
        # not as the colour assigned to z=0 in the colorscale.
        z_floor = counts.copy()
        if z_floor.max() == 0:
            # No data yet — show a flat dark plane so the panel isn't blank
            z_floor[:] = 0.001

        fig.add_trace(go.Surface(
            x=xs, y=ys, z=z_floor,
            colorscale=[
                [0.00, THEME["panel_bg"]],
                [0.15, "#0d2137"],
                [0.40, THEME["blue"]],
                [0.70, THEME["cyan"]],
                [1.00, THEME["red"]],
            ],
            showscale=False,
            opacity=0.92,
            contours=dict(
                z=dict(show=False),
                x=dict(show=False),
                y=dict(show=False),
            ),
        ))
    else:
        if not points_xy:
            # Render a single invisible anchor point so panel stays dark
            fig.add_trace(go.Scatter3d(
                x=[frame_w / 2], y=[frame_h / 2], z=[0],
                mode="markers",
                marker=dict(size=0.1, opacity=0),
            ))
        else:
            cw, ch = frame_w / gx, frame_h / gy
            xs_p, ys_p, zs_p, colors = [], [], [], []
            for x, y in points_xy:
                cx = min(int(x // cw), gx - 1)
                cy = min(int(y // ch), gy - 1)
                z = float(counts[cy, cx])
                xs_p.append(x)
                ys_p.append(y)
                zs_p.append(z)
                colors.append(z)
            max_c = max(colors) if colors else 1.0
            min_c = min(colors) if colors else 0.0
            # avoid cmin==cmax (all same density) which makes Plotly go white
            if max_c == min_c:
                max_c = min_c + 1.0
            fig.add_trace(go.Scatter3d(
                x=xs_p, y=ys_p, z=zs_p, mode="markers",
                marker=dict(
                    size=3,
                    color=colors,
                    cmin=min_c,
                    cmax=max_c,
                    colorscale=[
                        [0.0, THEME["cyan"]],
                        [0.6, THEME["orange"]],
                        [1.0, THEME["red"]],
                    ],
                    opacity=0.85,
                    showscale=False,
                ),
            ))

    fig.update_layout(
        paper_bgcolor=THEME["panel_bg"],
        scene=dict(
            xaxis=dict(visible=False, backgroundcolor=THEME["panel_bg"]),
            yaxis=dict(visible=False, backgroundcolor=THEME["panel_bg"]),
            zaxis=dict(
                title="density",
                color=THEME["muted"],
                backgroundcolor=THEME["panel_bg"],
                gridcolor=THEME["border"],
                showticklabels=False,
            ),
            bgcolor=THEME["panel_bg"],
            camera=dict(eye=dict(x=1.4, y=-1.4, z=1.0)),
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=300,
    )
    return fig
