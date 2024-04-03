""" Entire API - needs refactoring """
from flask import Flask
from flask_restful import abort, Api, fields, Resource, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bob_ross.db'
db = SQLAlchemy(app)


class Episode(db.Model):
    """ Episode Model """
    ep_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    date = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self) -> str:
        """ String representation of Episode """
        return f'<Episode {self.title}>'


# db.create_all()

# Define required arguments for post
ep_post_args = reqparse.RequestParser()
ep_post_args.add_argument('title', type=str, required=True,
                          help='Episode title required')
ep_post_args.add_argument('date', type=str, required=True,
                          help='Date of episode\'s first air date required')

# Define possible arguments for put
ep_put_args = reqparse.RequestParser()
ep_put_args.add_argument('title', type=str)
ep_put_args.add_argument('date', type=str)

resource_fields = {
    'ep_id': fields.Integer,
    'title': fields.String,
    'date': fields.String
}


class AllEpisodes(Resource):
    """ Class defining methods for all episodes endpoint """
    @marshal_with(resource_fields)
    def get(self):
        """ Define GET request made to /episodes endpoint """
        eps = Episode.query.all()
        return eps


class OneEpisode(Resource):
    """ Class defining methods for specific episode endpoint """
    @marshal_with(resource_fields)
    def get(self, ep_id):
        """ Define GET request made to endpoint including ep_id """
        ep = Episode.query.filter_by(ep_id=ep_id).first()
        if not ep:
            abort(404, message="Episode {} doesn't exist".format(ep_id))
        return ep

    @marshal_with(resource_fields)
    def post(self, ep_id):
        """ Define POST (add) request made to endpoint including ep_id """
        # Define arguments
        args = ep_post_args.parse_args()
        ep = Episode.query.filter_by(ep_id=ep_id).first()
        if ep:
            abort(409, message="Episode {} already exists".format(ep_id))
        ep = Episode(ep_id=ep_id, title=args['title'], date=args['date'])
        db.session.add(ep)
        db.session.commit()
        return ep, 201

    @marshal_with(resource_fields)
    def put(self, ep_id):
        """ Define PUT (update) request made to endpoint including ep_id """
        args = ep_put_args.parse_args()
        ep = Episode.query.filter_by(ep_id=ep_id).first()
        if not ep:
            # If episode doesn't exist, abort with 404 (not found)
            abort(404, message="Episode {} doesn't exist".format(ep_id))
        # Update episode (only these fields allowed)
        if args['title']:
            ep.title = args['title']
        if args['date']:
            ep.date = args['date']
        return ep

    @marshal_with(resource_fields)
    def delete(self, ep_id):
        """ Define DELETE request made to endpoint including ep_id """
        ep = Episode.query.filter_by(ep_id=ep_id).first()
        db.session.delete(ep)
        db.session.commit()
        return '', 204


# Define endpoints matched to classes - routes essentially
api.add_resource(OneEpisode, '/api/v1/episodes/<int:ep_id>')
api.add_resource(AllEpisodes, '/api/v1/episodes')

# endpoint examples
# /api/v1/episodes - all episodes
# /api/v1/episodes/1 - single episode
# /api/v1/episodes/color/1 - all episodes that include that color
# /api/v1/episodes/subject/1 - all episodes that include that subject
# /api/v1/episodes/month/1 - all episodes that aired during that month

if __name__ == '__main__':
    app.run(debug=True)
