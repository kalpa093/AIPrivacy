Compatibility
-------------

Starting from version ``4.0.0``, ``Faker`` dropped support for Python 2 and from version ``5.0.0``
only supports Python 3.7 and above. If you still need Python 2 compatibility, please install version ``3.0.1`` in the
meantime, and please consider updating your codebase to support Python 3 so you can enjoy the
latest features ``Faker`` has to offer. Please see the `extended docs`_ for more details, especially
if you are upgrading from version ``2.0.4`` and below as there might be breaking changes.

This package was also previously called ``fake-factory`` which was already deprecated by the end
of 2016, and much has changed since then, so please ensure that your project and its dependencies
do not depend on the old package.

Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install Faker

Use ``faker.Faker()`` to create and initialize a faker
generator, which can generate data by accessing properties named after
the type of data you want.


Korean Address 
-----------
create korean address and save csv
.. code:: python

    import pandas as pd
    from faker import Faker

    fake = Faker('ko_KR')

    #생성할 주소의 갯수 설정
    def generate_fake_addresses(num=10000):
        addresses = [fake.address() for _ in range(num)]
        return addresses

    #csv파일로 주소 저장
    def save_to_csv(data, filename='202301_kor_adr/fake_addresses.csv'):
        df = pd.DataFrame(data, columns=['Address'])
        df.to_csv(filename, index=False, encoding='cp949')

Korean Name
-----------
create korean name
.. code:: python

    import pandas as pd
    from faker import Faker

    fake = Faker('ko_KR')
    # 생성할 이름의 개수 설정
    num_names = 100

    # 이름을 저장할 리스트 초기화
    names = []

    # 한국 이름 생성
    for _ in range(num_names):
        name = fake.name()
        names.append(name)

    df = pd.DataFrame({'Name': names})
    # CSV 파일로 저장
    filename = 'korean_names.csv'
    df.to_csv(filename, index=False, encoding='cp949')

Korean registration number
-----------
create korean registration number

.. code:: python

    import pandas as pd
    from faker import Faker

    fake = Faker('ko_KR')
    # 생성할 주민등록번호갯수
    num_data = 100

    # 주민등록번호 저장할 리스트 초기화
    registration_data = []

    # 한국 이름 생성
    for _ in range(num_data):
        registration_data = fake.ssn()
    registration_data.append(registration_data)

    df = pd.DataFrame({'Registration_data': registration_data})
    # CSV 파일로 저장
    filename = 'korean_registration.csv'
    df.to_csv(filename, index=False, encoding='cp949')

Korean phone number
-----------
create korean phone number

.. code:: python

    import pandas as pd
    from faker import Faker

    fake = Faker('ko_KR')
    # 생성할 전화번호 개수
    num_phone = 100

    # 전화번호를 저장할 리스트 초기화
    phone_list = []

    # 전화번호 생성
    for _ in range(num_phone):
        phone = fake.phone_number()
        phone_list.append(phone)

    df = pd.DataFrame({'Phone': phone_list})
    # CSV 파일로 저장
    filename = 'korean_phone.csv'
    df.to_csv(filename, index=False, encoding='cp949')

