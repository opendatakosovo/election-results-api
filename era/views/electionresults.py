from flask.views import View
from flask import Response
from bson import json_util
from bson.son import SON

from era import mongo

import flask_pymongo


class ElectionResults(View):

    methods = ['GET']

    def dispatch_request(self, year, type_slug, commune_slug):
        '''Get the ElectionResults from the given year,
         and election type, and the commune.
         :param year: the given year of the election
         :param type_slug: the given type of election
         :param commune_slug: the given commune
        '''

        results = {
            'year': year,
            'type': type_slug,
            'commune': commune_slug
        }

        election_results = mongo.db.electionresults.find(results)

        resp = Response(
            response=json_util.dumps(election_results), mimetype='application/json')

        return resp
