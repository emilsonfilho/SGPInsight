from sqlalchemy import text, create_engine

engine = create_engine("sqlite:///test.db", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1")) # SQLAlchemy não permite que você execute SQL cru direto na unha
    # esse método text() transforma a query que você digita em um object SQLAlchemy, que é algo que a biblioteca entende
    # se fosse em Laravel, pensa nele como um DB::raw() mas com segurança por padrão
    print(result.scalar())

    # quer selecionar todos os usuários?
    result = conn.execute(
        text("SELECT * FROM items WHERE id = :id"),
        { "id": 1 }
    )
    
    print(result.all())
    
    result = conn.execute(
        text("SELECT * FROM items")
    )
    
    print(result.mappings().all())
    
    # e temos vários tipos:
    # .scalar()
    # .scalar_one() -> retorna o valor ou explode se vier 0 ou mais de uma linha
    # .scalar_one_or_none()
    # .first()
    # .one() -> exige exatamente uma linha
    # .one_or_none()
    # .all()
    # .mappings() -> ideal para API porque já vira JSON facin
    # .keys()
    # .rowcount
    # .commit() -> para quando estiver usando Session
    # .begin() -> já abre transação e é mais seguro para escrita
    # .dispose() -> fecha todas as conexões do pool
    # ver SQL = echo=True no create_engine