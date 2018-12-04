import os

# default is no-op
def geo_by_addr(ip):
    print('nope')
    pass

def _init_geoip():
    global geo_by_addr
    try:
        import GeoIP
    except ImportError:
        return

    geoip_path = os.environ.get('GEOIP_PATH')
    if not geoip_path:
        print("GEOIP_PATH environment variable required")
        return

    try:
        geo_db = GeoIP.open(geoip_path, GeoIP.GEOIP_MEMORY_CACHE)
    except Exception:
        print("Error opening GeoIP database: %s" % geoip_path)
        return

    geo_by_addr = geo_db.record_by_addr


_init_geoip()
