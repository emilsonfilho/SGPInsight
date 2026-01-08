""" 
    com Engine + Connection você precisa: 
    1. abrir conexão
    2. controlar a transação
    3. dar commit()
    4. dar rollback()
    5. fechar a conexão (se não estiver fazendo com o with)
    6. lembrar disso em toda query
    
    Session vem para diminuir a sua carga de trabalho!
    
    Session usa Engine por baixo dos panos, tá?
    Imagina ele como se fosse uma Request do Laravel
    Usa ORM
    save() [Laravel] -> .add() [Python]
    DB::transaction -> Session.begin()
    commit()
    
    você cria a engine
    e aí cria a FACTORY da session
"""

from User import User
from sessionFactory import SessionLocal

session = SessionLocal()

user = User(
    username="carlosddev",
    email="carlosdanieldev@email.com",
    hashed_password="12345678",
    full_name="Carlos Daniel Helmar"
)
session.add(user)
session.commit()

print(user.id) # já vem do banco automaticamente

user = session.query(User).filter(User.email == "ana.dev@email.com").first()
print(user)