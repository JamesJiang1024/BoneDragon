from example.common import service
from example.api import app


service.prepare_service([])

application = app.VersionSelectorApplication() 
