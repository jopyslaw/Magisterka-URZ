from django_unicorn.components import UnicornView

class ProfileCardView(UnicornView):
    DEFAULT_ROLE = 'TEST'

    name = "Jan"
    role = "User"

