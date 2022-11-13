from pprint import pprint

from rest_framework.test import APIClient
import pytest

from students.models import Course, Student
from django.test import TestCase
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    """Задаём Fixture для модели Course,
        декоратор @pytest.fixture обеспечит быстрый доступ к ним в других тестах def func(course)"""
    def factory(*args, **kwargs):
        """Задаём фабрику для теста курсов"""
        return baker.make(Course, *args, **kwargs)
    return factory
#

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


# проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_get_course_retrieve(client, course_factory):
    print('test_get_course_retrieve')
    course = course_factory(name='Course007')
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert course.name == 'Course007'

# проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_get_course_list(client, course_factory):
    print("test_get_course_list")
    course = course_factory(name='test', _quantity=3)
    response = client.get('/api/v1/courses/')
    print(f'Print:List name = {[c.name for c in Course.objects.all()]}')
    assert response.status_code == 200
    assert Course.objects.count() == 3
    assert [c.name for c in Course.objects.all()] == ['test', 'test', 'test']

# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_get_course_id(client, course_factory):
    print("test_get_course_id")
    course = course_factory(_quantity=3)
    print(f'Print:List id = {[c.id for c in Course.objects.all()]}')
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert [c.id for c in Course.objects.filter(id='5')] == [5]

# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_course_filter_name(client, course_factory):
    print("test_get_course_filter_name")
    course = course_factory(name='Course007')
    response = client.get('/api/v1/courses/?name=Course007')
    # print([r['name'] for r in response.data])
    assert response.status_code == 200
    assert [r['name'] for r in response.data] == ['Course007']
    assert response.json()[0]['name'] == 'Course007'

# тест успешного создания курса
@pytest.mark.django_db
def test_create_course_create(client, course_factory):
    print("test_get_course_create")
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'course05'}, format='json')
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert [c.name for c in Course.objects.all()] == ['course05']
    assert response.json()['name'] == 'course05'

# тест успешного обновления курса
@pytest.mark.django_db
def test_create_course_update(client, course_factory):
    print("test_get_course_update")
    course = course_factory(id=1, name='FalseName')
    print(f'Name create course = {Course.objects.filter(id=1)[0].name}')
    response = client.patch('/api/v1/courses/1/', data={'name': 'TrueName'}, format='json')
    print(f'Update name course = {Course.objects.filter(id=1)[0].name}')
    # print([r['name'] for r in response.data])
    print([c.name for c in Course.objects.all()])
    print(response.status_code)
    assert response.status_code == 200
    assert Course.objects.filter(id=1)[0].name == 'TrueName'

# тест успешного удаления курса
@pytest.mark.django_db
def test_create_course_delete(client, course_factory):
    print("test_get_course_delete")
    course = course_factory(id=1, name='test_course1')
    course = course_factory(id=2, name='test_course2')
    # print([c.name for c in Course.objects.all()])
    print(f"Created name list = {[c.name for c in Course.objects.all()]}")
    response = client.delete('/api/v1/courses/2/', data={'id': '2'})
    print(f"Created name list after delete = {[c.name for c in Course.objects.all()]}")
    print(response.status_code)
    assert response.status_code == 204

