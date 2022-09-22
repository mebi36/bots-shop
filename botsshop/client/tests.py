import json
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Client


DEMO_CLIENT = {
    "id": 1,
    "username": "overlord",
    "password": "overlord101",
    "first_name": "Regal",
    "last_name": "Overlord",
    "email": "loremipsum@gmail.com",
    "is_staff": True,
    "street": "54 King's drive",
    "city": "Ikeja",
    "state": "Lagos",
    "country": "Nigeria",
}
DEMO_CLIENT_SAME_EMAIL = {
    "id": 2,
    "username": "lorem224",
    "password": "lorem224",
    "first_name": "Lorem",
    "last_name": "Ipsum",
    "email": "loremipsum@gmail.com",
    "is_staff": False,
    "street": "Apartment 17B, Chief Austin Close",
    "city": "Onitsha",
    "state": "Anambra",
    "country": "Nigeria",
}
# API tests
class ClientCreationViewTestCase(APITestCase):
    """
    This test case is for the api view ClientCreationView.
    """

    url = reverse("client:create")

    def setUp(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        self.response = self.client.post(self.url, DEMO_CLIENT, format="json")

    def test_client_creation(self):
        """
        This is a test for the client creation feature of the api
        point.
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            json.loads(self.response.content)["username"],
            DEMO_CLIENT["username"],
        )
        self.assertTrue(
            Client.objects.filter(username=DEMO_CLIENT["username"]).exists()
        )
        self.assertTrue(
            Client.objects.get(username=DEMO_CLIENT["username"]).check_password(
                DEMO_CLIENT["password"]
            )
        )

    def test_duplicate_email_client_creation(self):
        """
        This is a test for creating a new client with email of an already
        existing client.
        """
        duplicate_email_response = self.client.post(
            self.url, DEMO_CLIENT_SAME_EMAIL, format="json"
        )
        self.assertEqual(
            duplicate_email_response.status_code, status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            list(json.loads(duplicate_email_response.content).keys()), ["email"]
        )
        self.assertEqual(
            json.loads(duplicate_email_response.content)["email"],
            ["user with this email already exists."],
        )

    def test_duplicate_username_client_creation(self):
        """
        This is a test for creating a new client with username of an already
        existing client.
        """
        duplicate_email_client = DEMO_CLIENT_SAME_EMAIL
        # modifying client duplicate email
        duplicate_email_client["email"] = "new_email@gmail.com"

        # setting client username to match already existing client
        # username
        duplicate_email_client["username"] = "overlord"

        duplicate_email_response = self.client.post(
            self.url, duplicate_email_client, format="json"
        )
        self.assertEqual(
            duplicate_email_response.status_code, status.HTTP_400_BAD_REQUEST
        )


class ClientViewTestCase(APITestCase):
    """
    This test suite will test the api point for editing and
    viewing a client object.
    """

    client_detail_url = reverse(
        "client:details", kwargs={"pk": DEMO_CLIENT["id"]}
    )

    def setUp(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        self.user = Client.objects.create_user(**DEMO_CLIENT)

        login_url = reverse("api-token-auth")
        self.login_response = self.client.post(
            login_url, DEMO_CLIENT, format="json"
        )
        self.client.credentials(
            HTTP_AUTHORIZATION="Token "
            + json.loads(self.login_response.content)["token"]
        )

    def test_login(self):
        """Test for client login api point."""
        self.assertEqual(self.login_response.status_code, status.HTTP_200_OK)

    def test_client_detail_get_method(self):
        """
        Test for the get method of the ClientView api view.
        Should return details for a particular client model instance.
        """
        response = self.client.get(self.client_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_detail_patch_method(self):
        """
        Test for client detail modification. This represents the 
        put method of the ClientView api view.
        """
        modified_fields = {"first_name": "Nova", "last_name": "Super"}
        response = self.client.patch(
            self.client_detail_url, modified_fields, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertDictContainsSubset(
            modified_fields, json.loads(response.content)
        )
