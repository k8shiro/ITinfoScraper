import falcon
from resource import PageResource, TagResource #, SiteResource, KeywordResource


api = falcon.API()

api.add_route('/api/page', PageResource())
api.add_route('/api/page/{order}', PageResource())
api.add_route('/api/tag', TagResource())
#api.add_route('/api/keyword', KeywordResource())
