""" Define routes/endpoints for API """
from .models import Episode
from .schemas import Add_Episode, Update_Episode
from .utils import find_value, color_dict, subject_dict, month_dict
from fastapi import Depends, HTTPException, APIRouter, Query, status
from initiate import Session, get_db
from typing import Optional


# Router provides blueprint for all endpoints
router = APIRouter(
    prefix="/api/v1/episodes"
)


@router.get("/")
def all_episodes(*, color: Optional[int] = Query(0, ge=0, lt=19),
                 subject: Optional[int] = Query(0, ge=0, lt=48),
                 month: Optional[int] = Query(0, ge=0, le=12),
                 db: Session = Depends(get_db)):
    """ Define GET request made to /episodes endpoint (including params) """
    # If no query params, return all episodes
    if color == 0 and subject == 0 and month == 0:
        return db.query(Episode).all()
    c_filt = find_value(color_dict, color)
    s_filt = find_value(subject_dict, subject)
    m_filt = find_value(month_dict, month)
    # Note: I am aware this is a dumb way to do this
    # If only color param, return all eps with color
    if color and subject == 0 and month == 0:
        return db.query(Episode).filter_by(**{c_filt: True}).all()
    # If only subject param, return all eps with subject
    if subject and color == 0 and month == 0:
        return db.query(Episode).filter_by(**{s_filt: True}).all()
    # If only month param, return all eps with month
    if month and color == 0 and subject == 0:
        return db.query(Episode).filter(Episode.date.like(f"%{m_filt}%")).all()
    # If only color and subject params, return all eps with color and subject
    if color and subject and month == 0:
        return db.query(Episode).filter_by(**{c_filt: True})\
                                .filter_by(**{s_filt: True}).all()
    # If only color and month params, return all eps with color and month
    if color and month and subject == 0:
        return db.query(Episode).filter_by(**{c_filt: True})\
                                .filter(Episode.date.like(f"%{m_filt}%")).all()
    # If only subject and month params, return all eps with subject and month
    if subject and month and color == 0:
        return db.query(Episode).filter_by(**{s_filt: True})\
                                .filter(Episode.date.like(f"%{m_filt}%")).all()
    # If all query params, return eps that match all query params
    if color and subject and month:
        return db.query(Episode).filter_by(**{c_filt: True})\
                                .filter_by(**{s_filt: True})\
                                .filter(Episode.date.like(f"%{m_filt}%")).all()


@router.get("/{ep_id}")
def one_episode(ep_id: int, db: Session = Depends(get_db)):
    """ Define GET request made to endpoint including ep_id """
    ep = db.query(Episode).filter_by(id=ep_id).first()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    return ep


@router.post("/{ep_id}")
def add_episode(ep_id: int, ep: Add_Episode, db: Session = Depends(get_db)):
    """ Define POST request made to endpoint """
    new_ep = Episode(**ep.dict(), id=ep_id)
    db.add(new_ep)
    db.commit()
    db.refresh(new_ep)
    return new_ep


@router.put("/{ep_id}")
def update_episode(ep_id: int, ep: Update_Episode, db: Session = Depends(get_db)):
    """ Define PUT request made to endpoint """
    update_ep = db.query(Episode).filter_by(id=ep_id).first()
    if not update_ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    for key, value in ep.dict().items():
        if value:
            setattr(update_ep, key, value)
    db.commit()
    db.refresh(update_ep)
    return update_ep


@router.delete("/{ep_id}")
def delete_episode(ep_id: int, db: Session = Depends(get_db)):
    """ Define DELETE request made to endpoint including ep_id """
    ep = db.query(Episode).filter_by(id=ep_id).first()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    db.delete(ep)
    db.commit()
    return {"message": "Episode deleted"}


@router.get("/color/{color_id}")
def all_episodes_by_color(color_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/colors/:id endpoint """
    column_name = find_value(color_dict, color_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Color not found")
    # Search for eps within column name based on color_id
    eps = db.query(Episode).filter_by(**{column_name: True}).all()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps


@router.get("/subject/{subject_id}")
def all_episodes_by_subject(subject_id: int,
                            db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/subject/:id endpoint """
    column_name = find_value(subject_dict, subject_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Subject not found")
    # Search for eps within column name based on subject_id
    eps = db.query(Episode).filter_by(**{column_name: True}).all()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps


@router.get("/month/{month_id}")
def all_episodes_by_month(month_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/month/:id endpoint """
    column_name = find_value(month_dict, month_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Month not found")
    # Search for eps where date column includes month based on month_id
    eps = db.query(Episode).filter(Episode.date.like(f"%{column_name}%")).all()
    if not eps:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No episodes found")
    return eps
