from plyer import notification
title = 'Hello Developer'

message= 'This is your coffee time!'
notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
