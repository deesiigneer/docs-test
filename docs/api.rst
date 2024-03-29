.. _api:

============
SPWorlds API
============

Получение токена и ID карты
===========================

Для использования API вам надо знать ID и token для карты, с которой вы
хотите совершить действие. Получить их можно в секции “Поделиться
картой” на сайте.

Выполнение запросов
===================

Все запросы к SPWorlds API должны обслуживаться через HTTPS и должны быть предоставлены в слудующей форме:

.. topic:: GET
  
  .. code-block:: HTTP 
  
    https://spworlds.ru/api/public/card


Поддерживаются **GET** и **POST** методы. Направляя любые запросы к API, добавляйте header ``Authorization`` имеющий
форму ``Bearer key``

.. hint::

  Где ``key`` - base64 закодированная строка ``ID:TOKEN``, где ``ID`` - ID вашей карты, ``TOKEN`` - token от нее.
  
Операции с картой
======

Создание запроса на оплату
--------------------------

Чтобы принять оплату АРами, надо сначала создать запрос на оплату. Он
делается таким **POST** запросом:


.. topic:: POST
  
  .. code-block:: HTTP 
  
     https://spworlds.ru/api/public/payment

.. table:: В body запроса должен быть JSON-объект, содержащий:

  ===============   ====================================================================================
  ``amount``        Стоимость покупки в АРах
  ``redirectUrl``   URL страницы, на которую попадет пользователь после оплаты
  ``webhookUrl``    URL, куда наш сервер направит запрос, чтобы оповестить ваш сервер об успешной оплате
  ``data``          Строка до 100 символов, сюда можно поместить любые полезные данные
  ===============   ====================================================================================
  

.. table:: Ответ будет в формате JSON и будет содержать только:

  =======   =======================================================================
  ``url``   Ссылка на страницу оплаты, на которую стоит перенаправить пользователя.
  =======   =======================================================================

Получение данных об успешной оплате
-----------------------------------

После успешной оплаты наш сервер указанный в ``webhookUrl`` отправит **POST** запрос по URL, который вы
указали при создании запроса на оплату (webhookUrl).

.. table:: Body запроса будет в формате JSON:

  ==========  ========================================================
  ``payer``   Ник игрока, который совершил оплату
  ``amount``  Стоимость покупки
  ``data``    Данные, которые вы отдали при создании запроса на оплату
  ==========  ========================================================
  
.. important::

  При обработке этого запроса надо подтвердить, что данные пришли из нашего сервера. Для этого в headers запроса есть ``X-Body-Hash`` который содержит закодированнный в base64 SHA256 `HMAC <https://ru.wikipedia.org/wiki/HMAC>`__ hash тела запроса, использующий как ключ ``token`` вашей карты. При приеме запроса вы сначала должны сгенерировать свой hash и убедиться что он совпадает с тем что в ``X-Body-Hash``, прежде чем обрабатывать запрос.

Запрос баланса
--------------

Что бы посмотреть баланс карты, необходимо сделать следующий **GET** запрос:

.. topic:: GET
  
  .. code-block:: HTTP 

   https://spworlds.ru/api/public/card


.. admonition:: Пример ответа:

  .. code:: json

     { "balance": 16 }

Переводы
--------

Чтобы совершить перевод надо сделать подобный **POST** запрос:

.. topic:: POST
  
  .. code-block:: HTTP 
  
     https://spworlds.ru/api/public/transactions

.. table:: Body - JSON объект, содержащий:

  ============  ==============================
  ``receiver``  Строка, номер карты получателя
  ``amount``    Количество аров для перевода
  ``comment``   Комментарий для перевода
  ============  ==============================

Получение ника
--------------

Чтобы получить ник надо сделать подобный **GET** запрос:

.. topic:: GET
  
  .. code-block:: HTTP 
  
     https://spworlds.ru/api/public/users/DISCORDID
   
.. hint::

  Где ``DISCORDID`` в URL - ID пользователя в Discord.

.. table:: В ответ вы получите JSON, где будет только 1 поле:

  ============  ===================================================================
  ``username``  Ник пользователя или null, если у пользователя нет входа на сервер.
  ============  ===================================================================
