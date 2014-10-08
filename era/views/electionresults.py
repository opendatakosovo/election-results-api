from flask.views import View
from flask import Response
from bson import json_util

from era import mongo


class ElectionResults(View):

    methods = ['GET']

    def dispatch_request(self, year, type_slug, commune_slug):
        '''Get the ElectionResults from the given year,
         and election type, and the commune.
         :param year: the given year of the election
         :param type_slug: the given type of election
         :param commune_slug: the given commune
        '''

        query = {
            'year': year,
            #We use dot notation below because we are feeding to mongo
            'type.slug': type_slug,
            'commune.slug': commune_slug
        }

        election_results = mongo.db.electionresults.find(query)

        resp = Response(
            response=json_util.dumps(election_results),
            mimetype='application/json')

        return resp
