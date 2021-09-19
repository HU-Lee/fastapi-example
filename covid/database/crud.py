from sqlalchemy.orm import Session

from . import models

# -----------------------------------------------------
#                       Korea
# -----------------------------------------------------

def get_korea(db: Session, date: str):
    return db.query(models.CovidKorea).filter(models.CovidKorea.date==date).first()
    
def get_korea_limit(db: Session, skip: int = 0, limit: int = 7):
    return db.query(models.CovidKorea).order_by(models.CovidKorea.date.desc()).offset(skip).limit(limit).all()

def create_or_update_korea(db: Session, date:str, detected:int, death:int):
    db_korea = get_korea(db, date)
    if not db_korea:
        db_korea = models.CovidKorea(date=date, detected=detected, death=death)
    else:
        setattr(db_korea, "detected", detected)
        setattr(db_korea, "death", death)
    try:
        db.add(db_korea)
        db.commit()
        db.refresh(db_korea)
        return db_korea
    except:
        db.rollback()
    finally:
        db.close()


# -----------------------------------------------------
#                       Inter
# -----------------------------------------------------

def get_inter(db: Session, date: str):
    return db.query(models.CovidInter).filter(models.CovidInter.date == date).first()
    
def get_inter_limit(db: Session, skip: int = 0, limit: int = 7):
    return db.query(models.CovidInter).order_by(models.CovidInter.date.desc()).offset(skip).limit(limit).all()

def create_or_update_inter(db: Session, date:str, jap:int, usa:int):
    db_inter = get_inter(db, date)
    if not db_inter:
        db_inter = models.CovidInter(date=date, jap=jap, usa=usa)
    else:
        setattr(db_inter, "jap", jap)
        setattr(db_inter, "usa", usa)
    try:
        db.add(db_inter)
        db.commit()
        db.refresh(db_inter)
        return db_inter
    except:
        db.rollback()
    finally:
        db.close()