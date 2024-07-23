from django import forms


class GetQuoteForm(forms.Form):
    # Sending from
    sending_from = sending_from = forms.CharField()
    sending_postcode = forms.CharField(max_length=20)

    # Delivered to
    delivered_to = forms.CharField()
    delivered_postcode = forms.CharField(max_length=20)

    # What are you sending?
    what_sending = forms.ChoiceField(
        choices=[
            ("Parcel", 'Parcel/Large Letter'),
            ("Pallet", 'Pallet'),
            ("Document", 'Document')
        ]
    )

    # Quantity
    quantity = forms.IntegerField(
        initial=1
    )

    # Outer Packaging Type
    packaging_type = forms.ChoiceField(
        choices=[
            ("Cardboard Box", 'Cardboard Box'),
            ("Jiffy", 'Jiffy / Flyer Bag'),
            ("Other", 'Other')
        ],
    )

    # Weight
    weight = forms.FloatField()

    # Dimensions
    length = forms.FloatField()
    width = forms.FloatField()
    height = forms.FloatField()

    # Measurements
    MEASUREMENTS_CHOICES = [
        ('kg/cm', 'kg/cm'),
        ('lb/inches', 'lb/inches')
    ]
    measurements = forms.ChoiceField(
        choices=MEASUREMENTS_CHOICES,
        initial='lb/inches',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

