# import peewee


# db = peewee.SqliteDatabase("crypto.db")
# db.connect()


# ## create de Base Model and create the table user with unique_id username and password
# class BaseModel(peewee.Model):
#     """Classe model base"""

#     class Meta:
#         # Indica em qual banco de dados a tabela
#         # 'author' sera criada (obrigatorio). Neste caso,
#         # utilizamos o banco 'codigo_avulso.db' criado anteriormente
#         database = db

# class User(BaseModel):
#     """
#     Classe que representa a tabela User
#     """
#     # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
#     id = peewee.CharField(unique=True)
#     username = peewee.CharField(unique=True)
#     password = peewee.CharField()