from dataclasses import dataclass
from typing import List
import faker

fake = faker.Faker('uk_UA')
fake_us = faker.Faker('en_US')

REVIEW_DATA = [
    'піца смачна',
    'було смачно',
    'кухня на висоті',
    'не сподобалось',
    'могло бути краще',
    'офіціантка повільно обслуговувала',
    'довго чекали на замовлення',
    'раджу відвідати',
    'борщ був несмачний',
    'довго чекали на чек',
    'погане обслуговування',
    'страви були холодні',
    'раджу спробувати напої власного виробництва',
    'принесли пересмажений стейк',
    'принесли холодну каву',
    'чудово',
    'жахливо',
    'велика сирна тарілка',
    'непоганий салат',
    'найкращі роли',
    'класне обслуговування',
    'світлий зал із чудовим краєвидом',
    'гарна територія',
    'затишне місце',
    'чистий столик',
    'комфортно',
    'сучасний iнтер`єр',
    'атмосфера чудова',
    'велике меню',
    'приємні ціни',
    'враження позитивні',
    'рекомендую'
]

RESTAURANT_NAME_FIRST_PART = [
    'Затишна',
    'Смачна',
    'Найкраща',
    'Сучасна',
    'Апетитна',
    'Добра',
    'Пікантна',
    'Стильна',
    'Вишукана',
    'Чудова',
    'Божественна',
    'Соковита',
    'Ароматна',
    'Мʼясна',
    'Грибова',
    'Відома',
    'Наша',
    'Маленька',
    'Райська'
]

RESTAURANT_NAME_SECOND_PART = [
    'Курочка',
    'Кавʼярня',
    'Закусочна',
    'Пекарня',
    'Бургерна',
    'Варенична',
    'Кухня',
    'Шашлична',
    'Страва',
    'Кава',
    'Забігайлівка',
    'Кебабна',
    'Колиба',
    'Канапка',
    'Піцерія',
    'Пирогівня',
    'Шампанерія',
    'Таверна',
    'Насолода'
]


@dataclass
class RestaurantReview:
    id: int
    restaurant_name: str
    reviewer_name: str
    review_text: str
    rating: int
    date_of_visit: str
    location: str


def generate_restaurant_name(count: int):
    return [
        fake.random_element(elements=RESTAURANT_NAME_FIRST_PART)
        + ' '
        + fake.random_element(elements=RESTAURANT_NAME_SECOND_PART)
        for i in range(count)
    ]


def generate_reviews() -> List[RestaurantReview]:
    reviews = []
    restaurant_names = generate_restaurant_name(30)

    for i in range(500):
        restaurant_name = fake.random_element(elements=restaurant_names)
        reviewer = fake.first_name()
        review_text = fake.paragraph(nb_sentences=fake.random_int(min=1, max=3), ext_word_list=REVIEW_DATA)
        rate = fake.random_int(min=1, max=5)
        date_of_visit = fake.date_between('-2y')
        city = fake.city_name()

        review = RestaurantReview(
            id=i,
            restaurant_name=restaurant_name,
            reviewer_name=reviewer,
            review_text=review_text,
            rating=rate,
            date_of_visit=date_of_visit,
            location=city
        )
        reviews.append(review)

    return reviews


def save_reviews_to_csv(reviews: List[RestaurantReview]) -> None:
    with open('reviews.csv', 'w') as file:
        file.write('id,restaurant_name,reviewer_name,review_text,rating,date_of_visit,location\n')

        for review in reviews:
            file.write(f'{review.id},'
                       f'{review.restaurant_name},'
                       f'{review.reviewer_name},'
                       f'{review.review_text},'
                       f'{review.rating},'
                       f'{review.date_of_visit},'
                       f'{review.location}\n'
                       )


if __name__ == '__main__':
    reviews = generate_reviews()
    save_reviews_to_csv(reviews)
