def get_page_html(form_data):
    print("Received form_data:", form_data)


    data = [
        ("Australia", "Measles", 502000, 2021),
        ("Malaysia", "Pertussis", 87000, 2022),
        ("Japan", "Measles", 145000, 2020),
        ("India", "Measles", 234000, 2019),
        ("USA", "Pertussis", 1200000, 2021),
        ("France", "Rubella", 43000, 2022),
        ("China", "Rubella", 67000, 2023),
        ("Brazil", "Measles", 980000, 2020),
        ("Singapore", "Pertussis", 90000, 2021),
        ("Canada", "Rubella", 52000, 2022)
    ]


    years = sorted({str(d[3]) for d in data})
    infection_types = sorted({d[1] for d in data})

    def pick(parameter):
        v = form_data.get(parameter)
        if isinstance(v, list) and v:
            v = v[0]
        if v is None:
            v = ""
        return str(v).strip()

    sel_year = pick("year")
    sel_infection_type = pick("infection_type")


    filtered_data = []
    for row in data:
        if sel_year and str(row[3]) != sel_year:
            continue
        if sel_infection_type and row[1] != sel_infection_type:
            continue
        filtered_data.append(row)


    year_opts = '<option value="">All Years</option>'
    for y in years:
        sel = " selected" if y == sel_year else ""
        year_opts += f'<option value="{y}"{sel}>{y}</option>'

    infection_opts = '<option value="">All Infection Types</option>'
    for t in infection_types:
        sel = " selected" if t == sel_infection_type else ""
        infection_opts += f'<option value="{t}"{sel}>{t}</option>'


    page_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Infection Statistics</title>
<style>
body{{ 
  font-family: Arial, sans-serif; 
  background: rgba(0,0,0,0.75) url(doc.jpg) center/cover no-repeat fixed;
  background-blend-mode:darken;
  margin:0; 
  padding:24px; 
  }}

header, footer{{
    background-color: rgba(0,0,0,0.6);
    text-align: center;
    padding: 10px;
    width: 1421px;
    position: relative;
    right: 25px;
    bottom: 25px;
    }}

header img{{
    width: 150px;
    height: auto;
    border-radius: 10px;}}

.container{{ 
  max-width: 900px; 
  margin: 0 auto; 
  padding: 20px; 
  }}
h1{{ 
  text-align:center; 
  color:#ffffff; 
  }}
form{{ 
  text-align:center; 
  margin-bottom:20px;
  }}
select, button{{ 
  padding:8px 10px; 
  margin:0 5px; 
  border-radius:5px; 
  border:1px solid #ccc; 
  }}
table{{ 
  width:100%; 
  border-collapse: collapse; 
  background-color:#eeeeee;
  position: relative;
  right: 200px;
  bottom: 490px;

  }}
th, td{{ 
  border:1px solid #ddd; 
  padding:10px; 
  text-align:left; 
  }}
th{{ 
  background-color:#004b7c; 
  color:white; }}
tr:nth-child(even){{ 
  background-color:#f9f9f9; 
  }}
.infection_count{{
  font-weight:bold;
  position: relative;
  top: 35px;
}}
.infection_background{{
  background_color:#ffffff;
  background: white;
  height: 80px;
  width: 900px;
  position: relative;
  top: 235px;
  left: 37px;
  border: solid 2px;
}}
.layout{{
  position: relative;
  bottom: 140px;
}}
.global_infection_image{{
    width: 400px;
    position: relative;
    left: 750px;
}}
.countries_image{{
    width:400px;
    position:relative;
    left:750px;
    top: 10px;
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
  position: relative;
  top: 100px;
}}
.btn1:hover {{
  background: skyblue;
  transition: 0.3s;
}}
</style>
</head>
<body>
<header>
    <img src="World-Health-Organization-WHO-Logo.png" alt="Logo">
</header>
=
<div class="layout">
<div class="Flw">
  <a href="/" class="btn1">Go Back to Home</a>
</div>
<div class="infection_background"><div class="infection_count">Global infection: 3,400,000</div></div>
<div class="container">
<h1>Global Reported Infection</h1>
<form method="get">
<select name="year">{year_opts}</select>
<select name="infection_type">{infection_opts}</select>
<button type="submit">Apply</button>
</form>
<table>
<tr><th>Country</th><th>Infection Type</th><th>Infected People</th><th>Year</th></tr>
<div class="global_infection_chart">
    <img class="global_infection_image" src="Global_Infection_Chart.png" alt="Global_infection"></img>
</div>
<div class="countries_infection">
    <img class="countries_image" src="Countries Infection.png" alt="Global_infection"></img>
</div>
"""

    if filtered_data:
        for country, infection_type, infected_people, year in filtered_data:
            page_html += f"<tr><td>{country}</td><td>{infection_type}</td><td>{infected_people:,}</td><td>{year}</td></tr>"
    else:
        page_html += '<tr><td colspan="4" style="text-align:center;">No data found</td></tr>'

    page_html += """
</table>
</div>
</div>
</body>
</html>
"""

    return page_html


