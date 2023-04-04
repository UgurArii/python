import plotly.offline as offline
import plotly.graph_objs as go

offline.plot({'data':[{'y':[14,22,30,44]}],
              'layout':{'title':'Offline Plotly','font':dict(size=16)}},image='png')
