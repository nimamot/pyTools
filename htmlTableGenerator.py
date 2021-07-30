rows = int(input("number of rows: "))
columns = int(input("numbber of columns: "))
table_header = ""
table_headers = columns*'    <th class="tg-0lax"> </th> \n'

table_rows = columns * """
        <td class="tg-0lax"></td>
    """
table_rows = "\n<tr>" + table_rows + "\n</tr>"

table_rows = rows * table_rows

final_code =  """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>

""" + """
  <tr> \n""" + table_headers + """ </tr> \n</thead>
<tbody>""" + table_rows + """ </tbody>\n </table> """


print(final_code)
