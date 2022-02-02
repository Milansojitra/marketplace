from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .recommandation import find_risk, find_recommandation
import random


class internal_recommand(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        data = request.data
        par_1 = data.get('par_1', '')
        par_2 = data.get('par_2', '')
        par_3 = data.get('par_3', '')
        par_4 = data.get('par_4', '')
        par_5 = data.get('par_5', '')
        par_6 = data.get('par_6', '')
        par_7 = data.get('par_7', '')
        par_8 = data.get('par_8', '')
        par_9 = data.get('par_9', '')
        par_10 = data.get('par_10', '')

        risks = find_risk(par_1, par_2, par_3, par_4,
                par_5, par_6, par_7, par_8, par_9, par_10)

        recommandations = find_recommandation(par_1, par_2, par_3, par_4,
                par_5, par_6, par_7, par_8, par_9, par_10)


        # this will be risks and recommandation from other apps 
        external_risks = random.sample([f'external_risk_{i}' for i in range(1,51)], 2)
        external_recommandations = random.sample( [f'external_recommandation_{i}' for i in range(1,51)], 2) 

        risks.extend(external_risks)
        recommandations.extend(external_recommandations)
        return Response({
            'risk': risks,
            'recommandation': recommandations,
            })

# this will for merging parameter from internal and external 
class external_recommand(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        # this 5 are the external parameters
        data = request.data
        par_1 = data.get('par_1', '')
        par_2 = data.get('par_2', '')
        par_3 = data.get('par_3', '')
        par_4 = data.get('par_4', '')
        par_5 = data.get('par_5', '')


        # this will be risks and recommandation from other apps 
        external_risks = random.sample([f'external_risk_{i}' for i in range(1,51)], 2)
        external_recommandations = random.sample( [f'external_recommandation_{i}' for i in range(1,51)], 2) 

        return Response({
            'risk': external_risks,
            'recommandation': external_recommandations,
            })


# for testing 
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
