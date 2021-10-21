from repositorio  import Repositorio
from databases.postgres import PostgresDB

db_conn = PostgresDB()
repo = Repositorio()

repo.insert(db_conn)