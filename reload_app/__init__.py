# HACK(mattrobenolt): In Python 3.7, Google libraries spew a few DeprecationWarnings
# for changes in Python 3.8. There's nothing we can do about them yet, so just keep
# in mind when upgrading to 3.8.
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
