"""Define version and import high-level objects"""
__VERSION_MAJOR__ = '1'
__VERSION_MINOR__ = '0'
__VERSION_BUILD__ = '1'

__DEBUG = False
if __DEBUG:
    import datetime as dt
    __VERSION_TAGS__ = f"d{dt.datetime.now().strftime('%Y%m%d_%H%M')}"
else:
    __VERSION_TAGS__ = ''

__VERSION__ = f'{__VERSION_MAJOR__}.{__VERSION_MINOR__}.{__VERSION_BUILD__}{__VERSION_TAGS__}'

__DATA_VERSION__ = '1.0'

try:
    from reviewanalysis.apple_review import AppReview
except ImportError:
    print("Unable to import the correct files. Please recheck the installation and directories")
