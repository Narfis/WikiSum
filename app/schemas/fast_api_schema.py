from pydantic import BaseModel

class Summary(BaseModel):
    wiki_summary: str

class KeyPoints(BaseModel):
    wiki_key_points: list[str] | str

class internalStats(BaseModel):
    most_common_words: list[list[str]]
    mean_word_length: float
    last_changes: list[str]

class Stats(BaseModel):
    wiki_stats: internalStats | str