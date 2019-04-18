_RFC3339_MICROS_NO_ZULU = "%Y-%m-%dT%H:%M:%S.%f"


def format_datetime(dt):
    return dt.strftime(_RFC3339_MICROS_NO_ZULU)


def ip_from_request(request):
    try:
        return request.access_route[0]
    except IndexError:
        return None
