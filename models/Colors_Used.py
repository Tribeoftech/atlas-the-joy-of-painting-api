"""
Declares Colors_Used model for storing information about the colors used in Bob Ross paintings.

Contains columns for painting metadata like title, season, episode, etc. as well as columns 
for the number of times each color was used in the painting. Allows querying painting info
by color usage.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Colors_Used(Base):
	__tablename__ = 'colors_used'
	id = Column(Integer, primary_key=True, index=True)
	painting_index = Column(Integer, nullable=False)
	img_src = Column(String, nullable=False)
	painting_title = Column(String, nullable=False)
	season = Column(Integer, nullable=False)
	episode = Column(Integer, nullable=False)
	num_colors = Column(Integer, nullable=False)
	youtube_src = Column(String, nullable=False)
	# colors is an array of strings
	colors = Column(String, nullable=False)
	# color_hex is an array of strings
	color_hex = Column(String, nullable=False)
	Black_Gesso = Column(Integer, nullable=False)
	Bright_Red = Column(Integer, nullable=False)
	Burnt_Umber = Column(Integer, nullable=False)
	Cadmium_Yellow = Column(Integer, nullable=False)
	Dark_Sienna = Column(Integer, nullable=False)
	Indian_Red = Column(Integer, nullable=False)
	Indian_Yellow = Column(Integer, nullable=False)
	Liquid_Black = Column(Integer, nullable=False)
	Liquid_Clear = Column(Integer, nullable=False)
	Midnight_Black = Column(Integer, nullable=False)
	Phthalo_Blue = Column(Integer, nullable=False)
	Phthalo_Green = Column(Integer, nullable=False)
	Prussian_Blue = Column(Integer, nullable=False)
	Sap_Green = Column(Integer, nullable=False)
	Titanium_White = Column(Integer, nullable=False)
	Van_Dyke_Brown = Column(Integer, nullable=False)
	Yellow_Ochre = Column(Integer, nullable=False)
	Alizarin_Crimson = Column(Integer, nullable=False)