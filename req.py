sql_request = "SELECT `users`.`Name`, count(`messages`.`msg`) FROM `users` " \
              "LEFT JOIN `messages` ON `messages`.`UID` == `users`.`UID` " \
              "GROUP BY `messages`.`UID`;"
