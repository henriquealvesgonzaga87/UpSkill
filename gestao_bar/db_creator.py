from main import engine
from base import Model
from models.models import *

Model.metadata.create_all(engine)
