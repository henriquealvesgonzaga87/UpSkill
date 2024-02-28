from main import engine
from base import Model
from models.user import *
from models.produtos import *

Model.metadata.create_all(engine)
