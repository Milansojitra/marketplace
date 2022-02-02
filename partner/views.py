from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from core.recommandation import find_risk, find_recommandation
from rest_framework.permissions import IsAuthenticated


# external app can access our recommandation from here
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

        risk = find_risk(par_1, par_2, par_3, par_4,
                par_5, par_6, par_7, par_8, par_9, par_10)

        recommandation = find_risk(par_1, par_2, par_3, par_4,
                par_5, par_6, par_7, par_8, par_9, par_10)
        return Response({
            'risks': risk,
            'recommandations': recommandation,
            })
