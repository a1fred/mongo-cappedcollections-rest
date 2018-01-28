from sanic import Sanic
from webapp import views


app = Sanic()
app.add_route(views.CollectionsIndexView.as_view(), '/', )
app.add_route(views.CollectionView.as_view(), '/<collection_name>', )
