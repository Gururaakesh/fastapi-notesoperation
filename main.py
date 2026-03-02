from fastapi import FastAPI,Depends
from database import SessionLocal,engine
import database
from sqlalchemy.orm import Session
from schemas import note


app=FastAPI()

database.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

product=[ note(id=1,title="gurunote",content="this is my first fastapi project"),
        note(id=2,title="raakeshnote",content="this is my first fastapi project"),
        note(id=3,title="dummynote",content="this is my first fastapi project")]

def init_db():
    db=SessionLocal()
    count=db.query(database.Product).count()


    if count==0:
        for i in product:
            db.add(database.Product(**i.model_dump()))
        db.commit()
init_db()



@app.get("/returnnotes")
def Return_allnotes(db:Session=Depends(get_db)):
    givedb=db.query(database.Product).all()
    return givedb

@app.post("/createnote")
def Add_notes(note:note,db:Session=Depends(get_db)):
    db.add(database.Product(**note.model_dump()))
    db.commit()

@app.get("/note/{id}")
def search(id:int,db:Session=Depends(get_db)):
    givedb=db.query(database.Product).filter(database.Product.id==id).first()
    return givedb

@app.put("/noteupdate/{id}")
def update(id:int,name:note,db:Session=Depends(get_db)):
    dbp=db.query(database.Product).filter(database.Product.id==id).first()
    if dbp:
        dbp.title=name.title
        dbp.content=name.content
        db.commit()
    else:
        return "No notes"