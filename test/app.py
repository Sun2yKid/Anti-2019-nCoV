import random

from pyecharts import options as opts
from pyecharts.charts import Map

from test.common import Data


values = [list(z) for z in zip(Data.provinces, [random.randint(20, 150) for _ in range(len(Data.provinces))])]
print(values)


def map_visualmap() -> Map:
    c = (
        Map()
        .add("Test", values, "china")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（连续型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )
    return c


table = map_visualmap()
table.render()
