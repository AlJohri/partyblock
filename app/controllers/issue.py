from . import api
from ..models import Issue

from flask.ext.restful import Resource, reqparse, fields, marshal_with
from dateutil import parser as dateparser

issue_fields = {
	'id': fields.Integer,
	'status': fields.String,
	'description': fields.String,
	'url': fields.String,
	'summary': fields.String,
	'html_url': fields.String,
	'comment_url': fields.String,
	'shortened_url': fields.String,
	'address': fields.String,
	'lat': fields.Raw,
	'lng': fields.Raw,
	'closed_at': fields.Raw, #DateTime,
	'acknowledged_at': fields.Raw, #DateTime,
	'created_at': fields.Raw, #DateTime,
	'updated_at': fields.Raw, #DateTime,
	'reporter_id': fields.String,
}

issue_marshall = {
	'meta': fields.Raw,
	'data': fields.Nested(issue_fields)
}

parser = reqparse.RequestParser()

class IssueController(Resource):

	@marshal_with(issue_marshall)
	def get(self, id):
		issue = Issue.query.get(id)
		return { 'meta': None, 'data': issue.to_dict() }

	@marshal_with(issue_marshall)
	def put(self, id):
		issue = Issue.query.get(id)
		return { 'meta': None, 'data': issue.to_dict() }

class IssueListController(Resource):

	parser.add_argument('page', type = int, required = False, location = 'values')

	@marshal_with(issue_marshall)
	def get(self):
		args = parser.parse_args()
		if not args['page']: args['page'] = 1
		query = Issue.query.order_by(Issue.id)
		count=query.count()
		issues = map(lambda x: x.to_dict(), query.paginate(args['page'], per_page=20).items)
		
		return { 'meta': {'count':count}, 'data': issues }

	@marshal_with(issue_marshall)
	def post(self):
		issue = Issue()
		return { 'meta': null, 'data': issue.to_dict() }

api.add_resource(IssueListController, '/api/issues/', endpoint = 'issues')
api.add_resource(IssueController, '/api/issue/<int:id>/', endpoint = 'issue')