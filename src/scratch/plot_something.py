import marimo

__generated_with = "0.11.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import numpy as np
    import pandas as pd
    from os.path import join
    import matplotlib.pyplot as plt
    return alt, join, np, pd, plt


@app.cell
def _(join):
    DATA_DIR = "data"
    PLOT_DIR = join(DATA_DIR, "plots")
    return DATA_DIR, PLOT_DIR


@app.cell
def _(DATA_DIR, join, pd):
    df = pd.read_csv(join(DATA_DIR, "scSTAR - table of interactive tools - non-systematic.csv"), index_col=0)
    return (df,)


@app.cell
def _(plt):
    tab20_rgb = [f"rgb({int(r*255)},{int(g*255)},{int(b*255)})" for (r, g, b, a) in [plt.cm.tab20(i) for i in range(20)]]
    return (tab20_rgb,)


@app.cell
def _(alt, tab20_rgb):
    color_scale = alt.Scale(domain=["Keyword Search", "Other"], range=tab20_rgb[:2])
    return (color_scale,)


@app.cell
def _(alt, color_scale, df):
    plot = alt.Chart(df).mark_bar().encode(
        x=alt.X("Year published:N"),
        y=alt.Y("count():Q", axis=alt.Axis(title="Number of Tools")),
        color=alt.Y("Source:N", scale=color_scale),
        row=alt.Row("Source:N", header=alt.Header(orient="top", title=None))
    ).properties(height=120, title="Count of Interactive Tools")
    plot
    return (plot,)


@app.cell
def _(DATA_DIR, join, plot):
    plot.save(join(DATA_DIR, "bar_plot.pdf"))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
