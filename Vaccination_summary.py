import pyhtml

def get_page_html(form_data):
    print("About to return page 2...")
    print("Received form_data:", form_data)

    def pick(param_name):
        v = form_data.get(param_name)
        if isinstance(v, list) and v:
            v = v[0]
        if v is None:
            v = ""
        return str(v).strip()

    sel_year    = pick("year")
    sel_antigen = pick("antigen")   # AntigenID
    sel_country = pick("country")   # CountryID
    sel_region  = pick("region")    # RegionID

    years     = pyhtml.get_results_from_query("immunisation.db", "SELECT DISTINCT year FROM Vaccination ORDER BY year;")
    antigens  = pyhtml.get_results_from_query("immunisation.db", "SELECT AntigenID, name FROM Antigen ORDER BY name;")
    countries = pyhtml.get_results_from_query("immunisation.db", "SELECT CountryID, name FROM Country ORDER BY name;")
    regions   = pyhtml.get_results_from_query("immunisation.db", "SELECT RegionID, region FROM Region ORDER BY region;")

    query = """
    SELECT
      a.name AS Antigen,
      v.year AS Year,
      c.name AS Country,
      r.region AS Region,
      ROUND(v.coverage, 2) AS Coverage
    FROM Vaccination v
    JOIN Antigen a ON a.AntigenID = v.antigen
    JOIN Country c ON c.CountryID = v.country
    JOIN Region  r ON r.RegionID  = c.region
    """
    filters = []
    if sel_year:
        filters.append(f"v.year = '{sel_year}'")
    if sel_antigen:
        filters.append(f"v.antigen = '{sel_antigen}'")
    if sel_country:
        filters.append(f"c.CountryID = '{sel_country}'")
    if sel_region:
        filters.append(f"r.RegionID = '{sel_region}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    query += " ORDER BY a.name, v.year, c.name;"

    results = pyhtml.get_results_from_query("immunisation.db", query)

    year_opts = '<option value="">Select Year</option>'
    for y in years:
        val = str(y[0])
        sel = " selected" if val == sel_year else ""
        year_opts += f'<option value="{val}"{sel}>{val}</option>'

    antigen_opts = '<option value="">Select Antigen</option>'
    for a in antigens:
        val = str(a[0])
        text = str(a[1])
        sel = " selected" if val == sel_antigen else ""
        antigen_opts += f'<option value="{val}"{sel}>{text}</option>'

    country_opts = '<option value="">Select Country</option>'
    for c in countries:
        val = str(c[0])
        text = str(c[1])
        sel = " selected" if val == sel_country else ""
        country_opts += f'<option value="{val}"{sel}>{text}</option>'

    region_opts = '<option value="">Select Region</option>'
    for r in regions:
        val = str(r[0])
        text = str(r[1])
        sel = " selected" if val == sel_region else ""
        region_opts += f'<option value="{val}"{sel}>{text}</option>'

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>Vaccination Data</title>
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

    <div class="logo"><img src="download.png" width="100%"></div>
    <h1>Vaccination Data Summary</h1>

    <form method="get">
      <div class="controls">
        <select name="year">{year_opts}</select>
        <select name="antigen">{antigen_opts}</select>
        <select name="country">{country_opts}</select>
        <select name="region">{region_opts}</select>
        <button type="submit">Apply</button>
      </div>
    </form>

    <div class="tablewrap">
      <table>
        <tr>
          <th>Antigen</th>
          <th>Year</th>
          <th>Country</th>
          <th>Region</th>
          <th>Coverage (%)</th>
        </tr>
"""
    if results:
        for row in results:
            page_html += "<tr>" + "".join([f"<td>{col}</td>" for col in row]) + "</tr>\n"
    else:
        page_html += '<tr><td colspan="5" style="text-align:center;">No data found</td></tr>'

    page_html += """
      </table>
    </div>

    
    
</body>
</html>
"""
    return page_html
