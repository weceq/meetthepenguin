"""Model calsses
"""

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DB = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
BASE = declarative_base()
