import pyhtml
def get_page_html(form_data):
    print("About to return page 3")

    economic_phase = (form_data.get("economic") or "").strip()
    infection_type = (form_data.get("Infection") or "").strip()
    year_filter = (form_data.get("year") or "").strip()
    sort_order = (form_data.get("Sort") or "").strip()

    page_html="""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Subtask B 1st part</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: #eeeded;
      margin: 0;
      padding: 0;
    }
    .logo {
      text-align: center;
      width: 1500px;
      background-color: white;


    }
    .logo img {
      width: 120px;
      height: auto;
    }
    header {
      background-color: #0089bf;
      color: white;
      padding: 40px;
    }
    h1 {
      margin: 0;
    }
    h2{
      font-weight: bold;
    }
    .layout{
      position: relative;
      bottom: 100px;
      right:90px;
    }
    .filter_table{
      position: relative;
      top: 200px;
    }
    h3 {
        font-size: 30px;
        padding: 0;
        margin: 0px;
        text-align: left;
        position:relative;
        left: 165px;
        top:50px;

    }
    .economic_box{
      width: 200px;
      height: 150px;
      border:2px solid black;
      position: relative;
      background-color: white;
      left: 100px;
      bottom: 150px;


    }
    .economic{
      position: relative;
      width: 180px;
      left: 100px;
      bottom: 300px;
      text-align: left;

    }
    .box_economic{
      border: 2px solid black;
      background-color: #009de1;
      width: 200px;
      height: 25px;
      position: relative;
      text-align: center;
      bottom:305px;
      left: 100px;
      font-weight: bold;
    }
    .year_box{
      border: 2px solid black;
      background-color: #009de1;
      width: 200px;
      height: 25px;
      position: relative;
      bottom: 280px;
      left: 100px;
      font-weight: bold;
    }
    .year_box_2{
      border: 2px solid black;
      width: 200px;
      height: 100px;
      background-color: white;
      position: relative;
      left: 100px;
      bottom:282px;
    }
    .year_textbox{
      position: relative;
      top:40px;
    }
    .infection_box{
      border: 2px solid black;
      background-color: #009de1;
      width: 200px;
      height: 25px;
      position: relative;
      bottom: 290px;
      left: 100px;
      font-weight: bold;
    }

    .infection_box_2{
      border: 2px solid black;
      width: 200px;
      height: 100px;
      background-color: white;
      position: relative;
      left: 100px;
      bottom:292px;
      text-align: left;
    }
    .infection_aligment{
      position:relative;
      left: 20px;
    }
    
    .sort_name{
      font-weight: bold;
      position: relative;
      top: 200px;
      font-size: 27px;
      right: 350px;
    }

    .sort_box {
      border: 2px solid black;
      position: relative;
      width: 1250px;
      top: 185px;
      background-color: white;
      text-align: left;
      padding: 10px;
      margin: 15px auto;
      left: 240px;
    }

        .data_table {
      margin: 20px auto;
      position: relative;
      left: 230px;
      bottom: 400px;
      width: 85%;
      background-color: white;
      border: 2px solid black;
      padding: 20px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .data_table h3 {
      text-align: left;
      margin-bottom: 15px;
      color: #0089bf;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 15px;
    }

    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: center;
    }

    th {
      background-color: #009de1;
      color: white;
    }

    tr:nth-child(even) {
      background-color: #e8e8ff;
    }

    tr:hover {
      background-color: #d9f2ff;
    }

  </style>
</head>
<body>
<div class="logo"><img src="World-Health-Organization-WHO-Logo.png" alt=""></div>
  <h2>INFECTION RATE</h2>
  <div class="layout">
  <form method="GET" action="">
    <div class="sort_name">Sort</div>
    <div class="sort_box">
      <div class="Ascending"><input type="radio" name="Sort" value="Ascending">Ascending</div>
      <div class="Descending"><input type="radio" name="Sort" value="Descending">Descending</div>
      <input type="reset" value="Reset">
      <button type="submit">Apply</button>
    </div>
    <h3>Filter</h3>
    <div class="filter_table">
      <div class="economic_box">economic box</div>
      <div class="box_economic">Economic Phase</div>
      <div class="economic">
      <div><input type="radio" name="economic" value="Developing">Developing</div>
      <div><input type="radio" name="economic" value="Developed">Developed</div>
      <div><input type="radio" name="economic" value="Economy in Transition">Economy in Transition</div>
      <div><input type="radio" name="economic" value="Least Developed">Least Developed</div>

      </div>
      <div class="year_box">Year</div>
      <div class="year_box_2">
        <div class="year_textbox"><input 
                  type="text" 
                  id="year" 
                  name="year" 
                  inputmode="numeric"
                  pattern="[0-9]{4}" 
                  maxlength="4" 
                  placeholder="enter the year" ></input>
        </div>
      </div>
      <div class="infection_box">Infection Type</div>
      <div>
        <div class="infection_box_2">
          <div class="infection_aligment">
            <div><input type="radio" name="Infection" value="Measles">Measles</div>
            <div><input type="radio" name="Infection" value="Rubella">Rubella</div>
            <div><input type="radio" name="Infection" value="Pertussis">Pertussis</div>
        </div>
      </div>
    </div>
  </form>
  </div>

"""
    

    def esc(s): 
        return str(s).replace("'", "''")

    where_parts = []
    if economic_phase:
        where_parts.append(f"e.phase = '{esc(economic_phase)}'")
    if infection_type:
        where_parts.append(f"it.description = '{esc(infection_type)}'")
    if year_filter and year_filter.isdigit():
        where_parts.append(f"i.year = {int(year_filter)}")

    where_clause = ("WHERE " + " AND ".join(where_parts)) if where_parts else ""

    if sort_order.lower() == "ascending":
        order_clause = "ORDER BY i.year ASC"
    elif sort_order.lower() == "descending":
        order_clause = "ORDER BY i.year DESC"
    else:
        order_clause = "ORDER BY c.name ASC, i.year ASC"

    query = f"SELECT c.name AS Country, i.year AS Year, it.description AS InfectionType, i.cases AS Cases, e.phase AS EconomicPhase, p.population AS Population FROM InfectionData i JOIN Country c ON i.country = c.CountryID JOIN Economy e ON c.economy = e.economyID JOIN CountryPopulation p ON i.country = p.country AND i.year = p.year JOIN Infection_Type it ON i.inf_type = it.id {where_clause} {order_clause};"

    results = pyhtml.get_results_from_query("database/immunisation.db",query)
    

    page_html += """
    <div class="data_table">
      <table>
        <tr>
    """

    col_names = ["Country", "Year", "Infection Type", "Cases","Economic Phase", "Population"]
    for col in col_names:
        page_html += f"<th>{col}</th>"
    page_html += "</tr>"

    if results:
        for row in results:
            page_html += "<tr>"
            for cell in row:
                page_html += f"<td>{cell}</td>"
            page_html += "</tr>"
    else:
        page_html += "<tr><td colspan='6'>No data found</td></tr>"

    page_html += """
      
          
      </table>
    </div>

      </div>
    </div>
  </div>
  
</body>
</html>
"""

    return page_html    