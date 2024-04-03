/**
 * Creates a table to store episode date information.
 * - id: Primary key column.
 * - title: Episode title text. 
 * - episode_date: Date the episode aired.
 */

CREATE TABLE IF NOT EXISTS episode_dates(
	id SERIAL PRIMARY KEY,
	title text NOT NULL,
	episode_date text NOT NULL
);

/**
 * Creates tables to store episode data:
 * 
 * - colors_used: Stores data on colors used in each episode painting
 *    - id: Primary key 
 *    - painting_index: Index of the painting in the episode 
 *    - img_src: Image source URL
 *    - painting_title: Title of the painting
 *    - season: Season number 
 *    - episode: Episode number
 *    - num_colors: Number of colors used
 *    - youtube_src: YouTube video source URL  
 *    - colors: Array of color names used
 *    - color_hex: Array of color hex values used  
 *    - Columns for number of times each color used
 *      
 * - subject_matter: Stores data on subject matter in each episode
 *    - id: Primary key
 *    - episode: Episode number
 *    - title: Episode title
 *    - Columns for presence of different subject matter
 */
CREATE TABLE IF NOT EXISTS colors_used(
	id SERIAL PRIMARY KEY,
	painting_index INTEGER NOT NULL,
	img_src text NOT NULL,
	painting_title text NOT NULL,
	season INTEGER NOT NULL,
	episode INTEGER NOT NULL,
	num_colors INTEGER NOT NULL,
	youtube_src text NOT NULL,
	colors text[] NOT NULL,
	color_hex text[] NOT NULL,
	Black_Gesso INTEGER NOT NULL,
	Bright_Red INTEGER NOT NULL,
	Burnt_Umber INTEGER NOT NULL,
	Cadmium_Yellow INTEGER NOT NULL,
	Dark_Sienna INTEGER NOT NULL,
	Indian_Red INTEGER NOT NULL,
	Indian_Yellow INTEGER NOT NULL,
	Liquid_Black INTEGER NOT NULL,
	Liquid_Clear INTEGER NOT NULL,
	Midnight_Black INTEGER NOT NULL,
	Phthalo_Blue INTEGER NOT NULL,
	Phthalo_Green INTEGER NOT NULL,
	Prussian_Blue INTEGER NOT NULL,
	Sap_Green INTEGER NOT NULL,
	Titanium_White INTEGER NOT NULL,
	Van_Dyke_Brown INTEGER NOT NULL,
	Yellow_Ochre INTEGER NOT NULL,
	Alizarin_Crimson INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS subject_matter(
	id SERIAL PRIMARY KEY,
	episode text NOT NULL,
	title text NOT NULL,
	APPLE_FRAME INTEGER NOT NULL,
	AURORA_BOREALIS INTEGER NOT NULL,
	BARN INTEGER NOT NULL,
	BEACH INTEGER NOT NULL,
	BOAT INTEGER NOT NULL,
	BRIDGE INTEGER NOT NULL,
	BUILDING INTEGER NOT NULL,
	BUSHES INTEGER NOT NULL,
	CABIN INTEGER NOT NULL,
	CACTUS INTEGER NOT NULL,
	CIRCLE_FRAME INTEGER NOT NULL,
	CIRRUS INTEGER NOT NULL,
	CLIFF INTEGER NOT NULL,
	CLOUDS INTEGER NOT NULL,
	CONIFER INTEGER NOT NULL,
	CUMULUS INTEGER NOT NULL,
	DECIDUOUS INTEGER NOT NULL,
	DIANE_ANDRE INTEGER NOT NULL,
	DOCK INTEGER NOT NULL,
	DOUBLE_OVAL_FRAME INTEGER NOT NULL,
	FARM INTEGER NOT NULL,
	FENCE INTEGER NOT NULL,
	FIRE INTEGER NOT NULL,
	FLORIDA_FRAME INTEGER NOT NULL,
	FLOWERS INTEGER NOT NULL,
	FOG INTEGER NOT NULL,
	FRAMED INTEGER NOT NULL,
	GRASS INTEGER NOT NULL,
	GUEST INTEGER NOT NULL,
	HALF_CIRCLE_FRAME INTEGER NOT NULL,
	HALF_OVAL_FRAME INTEGER NOT NULL,
	HILLS INTEGER NOT NULL,
	LAKE INTEGER NOT NULL,
	LAKES INTEGER NOT NULL,
	LIGHTHOUSE INTEGER NOT NULL,
	MILL INTEGER NOT NULL,
	MOON INTEGER NOT NULL,
	MOUNTAIN INTEGER NOT NULL,
	MOUNTAINS INTEGER NOT NULL,
	NIGHT INTEGER NOT NULL,
	OCEAN INTEGER NOT NULL,
	OVAL_FRAME INTEGER NOT NULL,
	PALM_TREES INTEGER NOT NULL,
	PathPath INTEGER NOT NULL,
	PERSON INTEGER NOT NULL,
	PORTRAIT INTEGER NOT NULL,
	RECTANGLE_3D_FRAME INTEGER NOT NULL,
	RECTANGULAR_FRAME INTEGER NOT NULL,
	RIVER INTEGER NOT NULL,
	ROCKS INTEGER NOT NULL,
	SEASHELL_FRAME INTEGER NOT NULL,
	SNOW INTEGER NOT NULL,
	SNOWY_MOUNTAIN INTEGER NOT NULL,
	SPLIT_FRAME	INTEGER NOT NULL,
	STEVE_ROSS INTEGER NOT NULL,
	STRUCTURE INTEGER NOT NULL,
	SUN	INTEGER NOT NULL,
	TOMB_FRAME INTEGER NOT NULL,
	TREE INTEGER NOT NULL,
	TREES INTEGER NOT NULL,
	TRIPLE_FRAME INTEGER NOT NULL,
	WATERFALL INTEGER NOT NULL,
	WAVES INTEGER NOT NULL,
	WINDMILL INTEGER NOT NULL,
	WINDOW_FRAME INTEGER NOT NULL,
	WINTER INTEGER NOT NULL,
	WOOD_FRAMED INTEGER NOT NULL
);