#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""


# count=0
# for key, value in page.items():
#     template = template.replace("?", page[key])
#     print(template)
# sort=template.format(**page)

title_placeholder = " ? "
charset_placeholder = "charset=?"
alert_placeholder = "alert(?)"
p_placeholder = ">?<"

new_template = template.replace(title_placeholder, page["title"])
new_template = new_template.replace(charset_placeholder, f"charset={page['charset']}")
new_template = new_template.replace(alert_placeholder, f"alert('{page['alert']}')")
new_template = new_template.replace(p_placeholder, f">{page['p']}<")
print(new_template)
# тут два решения