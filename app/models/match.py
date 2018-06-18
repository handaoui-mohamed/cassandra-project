from types import SimpleNamespace
from cassandra.cqlengine import columns
from app.models.base import Base
import uuid

results = SimpleNamespace(**{'DRAW': 0, 'WIN': 1, 'LOSS': 2})


class Match(Base):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    date = columns.Text()
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
