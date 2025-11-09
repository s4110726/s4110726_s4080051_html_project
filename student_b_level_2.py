import pyhtml

def get_page_html(form_data):
    print("About to return home...")
    print("Received form_data:", form_data)

    def pick(param_name):
        v = form_data.get(param_name)
        if isinstance(v, list) and v:
            v = v[0]
        if v is None:
            v = ""
        return str(v).strip()

    sel_year= pick("year")
    sel_infection_type= pick("infection_type")
    sel_economic_phase= pick("economic_phase")
    sel_population= pick("population")

    years= pyhtml.get_results_from_query("immunisation.db", "SELECT DISTINCT year FROM InfectionData ORDER BY year;")
    infection_type= pyhtml.get_results_from_query("immunisation.db", "SELECT id, description FROM Infection_Type ORDER BY description;")
    economic_phase= pyhtml.get_results_from_query("immunisation.db", "SELECT economyID, phase FROM Economy ORDER BY phase;")
    population= pyhtml.get_results_from_query("immunisation.db", "SELECT DISTINCT population FROM CountryPopulation ORDER BY population;")

    query = """
    SELECT
      it.description AS Infection_Type,
      i.year AS Year,
      e.phase AS Economic_Phase,
      p.population AS Population,
      ROUND(i.cases, 2) AS Cases
    FROM InfectionData i
    JOIN Infection_Type it ON it.id = i.inf_type
    JOIN Country c ON c.CountryID = i.country
    JOIN Economy e ON e.economyID = c.economy
    JOIN CountryPopulation p ON p.country = i.country AND p.year = i.year
    """

    filters = []
    if sel_year:
        filters.append(f"i.year = '{sel_year}'")
    if sel_infection_type:
        filters.append(f"i.inf_type = '{sel_infection_type}'")
    if sel_economic_phase:
        filters.append(f"e.economyID = '{sel_economic_phase}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += " ORDER BY it.description, i.year, e.phase;"

    results= pyhtml.get_results_from_query("immunisation.db", query)


    year_opts= '<option value="">Select Year</option>'
    for y in years:
        val= str(y[0])
        sel= " selected" if val == sel_year else ""
        year_opts += f'<option value="{val}"{sel}>{val}</option>'

    infection_type_opts= '<option value="">Select Infection Type</option>'
    for i in infection_type:
        val= str(i[0])
        text= str(i[1])
        sel= " selected" if val == sel_infection_type else ""
        infection_type_opts += f'<option value="{val}"{sel}>{text}</option>'

    economic_phase_opts= '<option value="">Select Economic Phase</option>'
    for e in economic_phase:
        val= str(e[0])
        text= str(e[1])
        sel= " selected" if val == sel_economic_phase else ""
        economic_phase_opts += f'<option value="{val}"{sel}>{text}</option>'


    page_html= f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>Infection Data</title>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width,initial-scale=1.0" />
<style>
body {{
  margin: 0;
  font-family: Arial, sans-serif;
  background: rgba(0,0,0,0.75) url(doc.jpg) center/cover no-repeat fixed;
  background-blend-mode: darken;
  color: #111;
}}
.shell {{
  max-width: 980px;
  margin: 0 auto;
  padding: 24px 14px 40px;
}}
.logo {{
  width: 110px;
  padding: 6px;
  border: 1px solid #ccc;
  background: #fff;
  border-radius: 6px;
}}
h1 {{
  margin: 12px 0;
  font-size: 20px;
  color: #fff;
  text-align: center;
}}
.controls {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 10px 0 14px;
  justify-content: center;
}}
select {{
  padding: 6px 8px;
  border: 1px solid #bbb;
  background: #fff;
  color: #111;
  border-radius: 4px;
  min-width: 150px;
}}
button {{
  padding: 6px 10px;
  border: 1px solid #bbb;
  background: #eee;
  color: #111;
  border-radius: 4px;
  font-weight: bold;
}}
.tablewrap {{
  background: #fff;
  border: 1px solid #bbb;
  border-radius: 6px;
  margin-top: 10px;
  overflow-x: auto;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  background: #fff;
  color: #111;
}}
th, td {{
  border: 1px solid #bbb;
  padding: 8px;
  font-size: 14px;
  text-align: left;
}}
th {{
  background: #eee;
  font-weight: bold;
}}
tr:nth-child(even) td {{
  background: #fafafa;
}}
.Flw {{
  text-align: center;
  margin: 12px 0;
}}
.btn1 {{
  display: inline-block;
  padding: 10px 22px;
  border-radius: 6px;
  background: #e5e7eb;
  color: #0f172a;
  text-decoration: none;
  font-weight: 700;
  border: 1px solid #d1d5db;
}}
.btn1:hover {{
  background: skyblue;
  transition: 0.3s;
}}
.btn2 {{
  display: inline-block;
  padding: 10px 22px;
  border-radius: 6px;
  background: #e5e7eb;
  color: #0f172a;
  text-decoration: none;
  font-weight: 700;
  border: 1px solid #d1d5db;
  position: relative;
  bottom: 52px;
  left: 700px;
}}
.btn2:hover {{
  background: skyblue;
  transition: 0.3s;
}}
.footer {{
  text-align: center;
  color: #ccc;
  font-size: 14px;
  margin-top: 20px;
}}
</style>
</head>
<body>
  <div class="shell">
    <div class="Flw">
      <a href="/" class="btn1">Go Back to Home</a>
    </div>
    <a href="/page6" class="btn2">Global Reported Infection</a>
    <div class="logo"><img src="World-Health-Organization-WHO-Logo.png" width="100%"></div>
    <h1>Infection Data Summary</h1>

    <form method="get">
      <div class="controls">
        <select name="year">{year_opts}</select>
        <select name="infection_type">{infection_type_opts}</select>
        <select name="economic_phase">{economic_phase_opts}</select>
        <button type="submit">Apply</button>
      </div>
    </form>

    <div class="tablewrap">
      <table>
        <tr>
          <th>Infection Type</th>
          <th>Year</th>
          <th>Economic Phase</th>
          <th>Population</th>
          <th>Cases</th>
        </tr>
"""
    if results:
        for row in results:
            page_html+= "<tr>" + "".join([f"<td>{col}</td>" for col in row]) + "</tr>\n"
    else:
        page_html+= '<tr><td colspan="5" style="text-align:center;">No data found</td></tr>'

    page_html+= """
      </table>
    </div>
</body>
</html>
"""
    return page_html

