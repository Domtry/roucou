from pydantic import BaseModel


class ArticleBase(BaseModel):
    label: str
    description: str
    price: int
    img_url: str
    category_id: str | None


class ArticleIn(ArticleBase):
    label: str
    description: str
    price: int
    img_url: str
