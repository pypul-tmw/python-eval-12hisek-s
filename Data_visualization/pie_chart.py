import plotly.express as px

data = {
    "Category": ["Electronics","Books","Clothes"],
    "Amount":[500,800,900]
}

fig = px.pie(
    data,
    names = "Category",
    values = "Amount",
    title = "Sales Distibution"
)


fig.show()