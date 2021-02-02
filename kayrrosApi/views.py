import logging
from kayrrosApi.serialization import SerializationClass
from kayrrosApi.models import ShowsModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.validators import validate_slug
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

# Enabling Logger
logger = logging.getLogger(__name__)

@api_view(['GET'])
def showAll(request):
    # Check if the request is GET and the path of it
    if request.method=='GET' and request.path =='/episodes/count':
        # Parsing GET parameters
        season = request.query_params.get('season')
        getSeason = request.query_params.get('getseason')
        # Check if season has been set
        if season:
            # Validating the value syntax and format of passed parameter
            try:
                validate_slug(season)
                season = int(season)
            except ValueError:
                # Logged the error for development purposes
                logger.error("invalid literal passed to int()")
                # Throw an error to userside without giving information about the error
                return Response("Hmmm! Are you a robot?!")
            except ValidationError:
                # Logged the error for development purposes
                logger.error("invalid input passed to validate_slug()")
                # Throw an error to user/front side without giving information about the error
                return Response("Hmmm! Are you a robot?!")
            # Query the database and count the number of episodes with specific season number
            results = ShowsModel.objects.filter(episodes_season=season).count()
            # Checking the query result (=0 means, the number of episode is 0 for such a season)
            if results != 0:
                dict = {
                    "TotalEpisodesNumber": results
                }
                return Response(dict)
            else:
                # Logged the error for development purposes
                logger.error("Not a valid season number!")
                # Throw an error to front side without giving information about the error
                return Response("Hmmm! Are you a robot?!")
        # Check if getSeason has been set
        elif getSeason:
            # Validating the GET parameter value
            try:
                validate_slug(getSeason)
                getSeason = int(getSeason)
            except ValueError:
                # Logged the error for development purposes
                logger.error("invalid literal passed to int()")
                return Response("Hmmm! Are you a robot?!")
            except ValidationError:
                # Logged the error for development purposes
                logger.error("invalid input passed to validate_slug()")
                return Response("Hmmm! Are you a robot?!")
            # Querying the db and get the episodes of specific season
            results = ShowsModel.objects.filter(episodes_season=getSeason)
            if results:
                serialize=SerializationClass(results,many=True)
                return Response(serialize.data)
            else:
                # Logged the error for development purposes
                logger.error("Not a valid season number!")
                return Response("Hmmm! Are you a robot?!")
        else:
            return Response("Hmmm! Are you a robot?!")
    # Check if the request is GET and also the path of it is for title 
    elif request.method=='GET' and request.path =='/episodes/title':
        # retriving the GET parameters
        season = request.query_params.get('season')
        episode = request.query_params.get('episode')
        # Checking if they are set correctly
        if season and episode:
            # Validating the syntax and format of both parameters
            try:
                validate_slug(season)
                getSeason = int(season)
                validate_slug(episode)
                getSeason = int(episode)
            except ValueError:
                # Logged the error for development purposes
                logger.error("invalid literal passed to int()")
                return Response("Hmmm! Are you a robot?!")
            except ValidationError:
                # Logged the error for development purposes
                logger.error("invalid input passed to validate_slug()")
                return Response("Hmmm! Are you a robot?!")
            try:
                # Querying the db to find the proper data
                results = ShowsModel.objects.get(episodes_season=season, episodes_number=episode)
            except ObjectDoesNotExist:
                # Logged the error for development purposes
                logger.error("Query values does not matched any record")
                return Response("Hmmm! Are you a robot?!")
            if results.episodes_name:
                dict = {
                    "EpisodeTitle": results.episodes_name
                }
                return Response(dict)
            else:
                # Logged the error for development purposes
                logger.error("Not a valid season number!")
                return Response("Hmmm! Are you a robot?!")
        else:
            # Logged the error for development purposes
            logger.error("parameters not defind properly")
            return Response("Hmmm! Are you a robot?!")
    else:
        # Logged the error for development purposes
        logger.error("Not a valid path!")
        return Response("Hmmm! Are you a robot?!")