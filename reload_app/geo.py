import os


def geo_by_addr(ip):
    raise Exception("Problem loading geoip2 client")


def _init_geoip():
    global geo_by_addr
    try:
        import geoip2.database
    except ImportError:
        return

    geoip_path = os.environ.get("GEOIP_PATH")
    if not geoip_path:
        print("GEOIP_PATH environment variable required")
        return

    try:
        geo_db = geoip2.database.Reader(geoip_path)
    except Exception:
        print("Error opening GeoIP database: %s" % geoip_path)
        return

    geo_by_addr = geo_db.city


_init_geoip()
