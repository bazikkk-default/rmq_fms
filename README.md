# fms_agreement

Сервис для проверки ограничений на въезд.

По средствам запросов сперва к сервису ФМС(http://services.fms.gov.ru/info-service.htm?sid=3000),
далее забирает капчу, и идём к сервису Rucapcha для регистрации изображения(https://rucaptcha.com/in.php),
после успешной регистрации спустя 5 секунд идём забирать ответ из Rucapcha(https://rucaptcha.com/res.php), 
после получения "успешного" - разгаданного ответа, подставляем его в запрос к сервису ФМС и данные которые
отдали на вход, а именно ФИО, ИО на латинице, Дата рождения, Тип документа, Серия и номер данного документа,
Дату окончания срока действия данного документа, Гражданство, Страну выдавшую данный документ.

В случае удачного ответа мы получим "There are no restrictions" и статус "success", 
иначе "fail" и "There are restrictions".

Вот и всё из последних нововведений докерфайл.
