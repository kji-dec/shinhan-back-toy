# shinhan-back-toy
shinhan pda backend toy project repository

<br>

## Requirements

```text
asgiref==3.6.0
Django==4.1.5
django-cors-headers==3.13.0
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
PyJWT==2.6.0
pytz==2022.7.1
sqlparse==0.4.3
tzdata==2022.7
xlwt==1.3.0
```

<br>

## How to run server

```shell
$python manage.py runserver
```

<br>

## Features

- Users can signup, login, logout
- Users can see the order list in page
  - Inform users order number, order date
- Users can use order detail page as community
  - Users can post comments on specific order
  - Users can delete comments (only own comments)
  - Inform users order details such as account number, etc.

<br>

- all the pages are just for the api test.

<br>

## References

