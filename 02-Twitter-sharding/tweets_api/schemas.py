from pydantic import BaseModel, ConfigDict

# Tweet section


class TweetBase(BaseModel):
    text: str


class TweetCreate(TweetBase):
    owner_id: int
    location: str
    like_count: int


class Tweet(TweetBase):
    id: int

    # Common pattern in SQLAlchemy
    # Fetch objects from a database and return them directly as Pydantic models
    # Instead of instead of handling the conversion from DB object to pydantic model
    model_config = ConfigDict(from_attributes=True)
