from flask.ext.wtf import Form
from wtforms import TextField, validators

class RetrieveDBInfo(Form):
    textQuery = TextField(label='Search For Articles', description="db_get")
