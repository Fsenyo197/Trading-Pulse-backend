from django.urls import reverse

def generate_url():
    """
    Generates a URL for the 'economic-event-api' endpoint.

    This function utilizes Django's reverse function to generate a URL
    based on the URL configuration defined in the project's URL patterns.

    Returns:
        str: The generated URL for the 'economic-event-api' endpoint.
    """
    url = reverse('economic-event-api')
    return url
