from cassandra.cqlengine import columns
from app.models.base import Base
import uuid


class Match(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    date = columns.Date()
    venue = columns.Text()
    tournament = columns.Text()
    competitor_1 = columns.Map(columns.Text(), columns.Integer())
    competitor_2 = columns.Map(columns.Text(), columns.Integer())
    result = columns.SmallInt()

    def get_data(self):
        return {
            'id': str(self.id),
            'date': self.date,
            'venue': self.venue,
            'tournament': self.tournament,
            'competitor_1': self.competitor_1,
            'competitor_2': self.competitor_2,
            'result': self.result
        }
