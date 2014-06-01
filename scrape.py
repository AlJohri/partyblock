from sqlalchemy.exc import IntegrityError
from app.models import db, Issue, Reporter

import requests, json

per_page = 10

places = [
  'raleigh-six-forks-corridor', 
  'six-forks',
  'raleigh',
  'falls-of-neuse',
  'glenwood_wake',
  'five-points_wake',
  'mordecai',
  'wake-county',
  'wade_wake',
  'raleigh_downtown',
  'north-central_wake',
  'hillsborough_wake',
  'east-raleigh',
  'central_wake',
  'north_wake',
  'south-central_wake'
]


for place in places:

  page = 1

  while True:
    response = requests.get('https://seeclickfix.com/api/v2/issues?page=%s&per_page=%i&place_url=%s' % (page,per_page,place))
    data = response.json()
    next_page = data['metadata']['pagination'].get('next_page')
    if next_page == None: break

    for item in data['issues']:

      if not item['reporter']['id']: continue

      issue = Issue(
        id=item.get('id'), 
        status=item.get('status'),
        description=item.get('description'),
        url=item.get('url'),
        summary=item.get('summary'),
        html_url=item.get('html_url'),
        comment_url=item.get('comment_url'),
        shortened_url=item.get('shortened_url'),
        address=item.get('address'),
        lat=item.get('lat'),
        lng=item.get('lng'),
        closed_at=item.get('closed_at'),
        acknowledged_at=item.get('acknowledged_at'),
        created_at=item.get('created_at'),
        updated_at=item.get('updated_at')
      )

      reporter = Reporter(
        id=item['reporter'].get('id'),
        witty_title=item['reporter'].get('witty_title'),
        civic_points=item['reporter'].get('civic_points'),
        name=item['reporter'].get('name')
      )

      issue.reporter_id = reporter.id

      print issue.id, issue.description
      print reporter.id, reporter.name

      try:
        db.session.add(issue)
        db.session.commit()
      except IntegrityError:
        db.session.rollback()

      try:
        db.session.add(reporter)
        db.session.commit()
      except IntegrityError:
        db.session.rollback()

    page += 1