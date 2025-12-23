# ---------- GET ----------
import requests
from pydantic import BaseModel


BASE_URL = "https://fakestoreapi.com"


class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str

def test_get_product_positive():
    # Act — выполняем GET-запрос на получение продукта с валидным id
    response = requests.get(f"{BASE_URL}/products/1")

    # Assert — проверяем, что запрос успешный
    assert response.status_code == 200

    # Assert — проверяем, что тело ответа соответствует схеме Product
    # (поля присутствуют и имеют корректные типы)
    Product.model_validate(response.json())