import pandas as pd
import plotly.express as px

data = pd.DataFrame(
    {
        "Day": [1,2,3,4,5],
        "Sales":[100,150,130,180,200]
    }
)

fig = px.line(
    data, x ="Day",
    y="Sales",
    title= "Daily Sales"
)

fig.show()