from src.infrastructure.database.postgres import engine
from sqlalchemy import text
from sqlalchemy.orm import Session

# stm ="""CREATE TABLE test_table (
#         id numeric NOT NULL,
#         name VARCHAR(64) NOT NULL,
#         password VARCHAR(256),
#         email VARCHAR(64)
#     )"""


# stm = """INSERT INTO 
#             test_table 
#                 (id, name, password, email) 
#             VALUES
#                 ('1', 'testuser', 'password123','dev@dev.com')
#     """

stm = "SELECT * FROM test_table"

# stm = "DROP TABLE IF EXISTS test_table"


# with engine.connect() as conn:
#     conn.execute(text(stm))
#     conn.commit()

with Session(engine) as session:
    result = session.execute(text(stm))
    session.commit()
    print(result.all())