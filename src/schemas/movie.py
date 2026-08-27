from pydantic import BaseModel, ConfigDict


class MovieSchema(BaseModel):
    id: int
    title: str
    year: int | None
    genres: list[str]

    model_config = ConfigDict(from_attributes=True)