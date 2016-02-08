# -*- coding: utf-8 -*-
sql_request = "SELECT `users`.`Name` AS 'Имя пользователя', count(`messages`.`msg`) AS 'Общее количество сообщений' " \
              "FROM `users` " \
              "LEFT JOIN `messages` ON `messages`.`UID` == `users`.`UID` " \
              "GROUP BY `messages`.`UID`;"
