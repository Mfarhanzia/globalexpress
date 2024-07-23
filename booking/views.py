from django.shortcuts import render
from django.views import View
from django.conf import settings

from booking.forms import GetQuoteForm

import requests

# Create your views here.

class HomeView(View):
    
    @staticmethod
    def _get_countries():
        url = "https://staging2.services3.transglobalexpress.co.uk/Country/V2/GetCountries"
        payload = {
            "Credentials": {
                "APIKey": f"{settings.API_KEY}",
                "Password": f"{settings.API_PASSWORD}"
            }
        }

        try:
            response = requests.post(url, json=payload)
            json_data = response.json() 
            if json_data["Status"] == "SUCCESS":
                return json_data["Countries"]
            return False
        except Exception as e:
            return False
    
    @staticmethod
    def _get_minimal_quotation(form):
        sending_from_country_id, sending_from_country_code = form.cleaned_data["sending_from"].split("-")
        delivered_to_country_id, delivered_to_country_code = form.cleaned_data["delivered_to"].split("-")
        payload = {
            "Credentials": {
                # "APIKey": f"{settings.API_KEY}",
                # "Password": f"{settings.API_PASSWORD}"
                "APIKey": "8uVtgK5K5w",
                "Password": "i]w39gYCOo"
            },
            "Shipment": {
                "Consignment": {
                    "ItemType": form.cleaned_data["what_sending"],
                    "Packages": [
                        {
                        "Weight": form.cleaned_data["weight"],
                        "Length": form.cleaned_data["length"],
                        "Width": form.cleaned_data["width"],
                        "Height": form.cleaned_data["height"]
                        }
                    ]
                },
                "CollectionAddress": {
                    # "City": form.cleaned_data["city"],
                    "Postcode": form.cleaned_data["sending_postcode"],
                    "Country": {
                        "CountryID": sending_from_country_id,
                        "CountryCode": sending_from_country_code
                    }
                },
                "DeliveryAddress": {
                    # "City": form.cleaned_data["city"],
                    "Postcode": form.cleaned_data["delivered_postcode"],
                    "Country": {
                        "CountryID": delivered_to_country_id,
                        "CountryCode": delivered_to_country_code
                    }
                }
            }
        }
        # url = "https://staging2.services3.transglobalexpress.co.uk/Quote/V2/GetQuoteMinimal"
        url = "https://services3.transglobalexpress.co.uk/Quote/V2/GetQuoteMinimal"
        # url = "https://staging2.services3.transglobalexpress.co.uk/Quote/V2/GetQuote"
        response = requests.post(url, json=payload)
        json_data = response.json() 
        print("\n===json_data", json_data)
        if json_data["Status"] == "SUCCESS":
            return json_data["ServiceResults"]
        # else:
            # messages.error


    def get(self, request, *args, **kwargs):
        countries = self._get_countries()
        return render(request, "home.html", {"countries_list": countries})
    
    def post(self, request):
        form = GetQuoteForm(request.POST)
        print("valid==", form.is_valid())
        if form.is_valid():
            quotations = self._get_minimal_quotation(form)
            print("==quotation==", quotations[0])
            return render(request, "list_quotations.html", {"quotations": quotations})
        else:
            countries = self._get_countries()
            return render(request, "home.html", {"form": form, "countries_list": countries})
