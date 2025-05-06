import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer

class FetchCountriesView(APIView):
    def get(self, request, *args, **kwargs):
        url='https://restcountries.com/v3.1/all'
        response=requests.get(url, timeout=10)

        if response.status_code!=200:
            return Response({"Error":"Failed to fetch data from API"}, status=status.HTTP_502_BAD_GATEWAY)
        
        data=response.json()
        created=0

        for item in data:
            country_data={
                "name":item.get("name", {}).get("common"),
                "official_name":item.get("name", {}).get("official"),
                "capital":item.get("capital", [None])[0],
                "region":item.get("region", ""),
                "subregion":item.get("subregion", ""),
                "area":item.get("area", 0.0),
                "population":item.get("population", 0),
                "flag_url":item.get("flags", {}).get("png",""),
            }

            if not Country.objects.filter(name=country_data["name"]).exists():
                serializer=CountrySerializer(data=country_data)

                if serializer.is_valid():
                    serializer.save()
                    created+=1
        
        return Response({"Message": f"{created} counties stored successfully"})