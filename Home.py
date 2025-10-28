import sqlite3

def get_page_html(form_data):
    print("About to return home page...")

   
    with sqlite3.connect("immunisation.db") as con:
        cur = con.cursor()

        # Country Count
        cur.execute("SELECT COUNT(*) FROM Country;")
        country_count = cur.fetchone()[0]

        # Highest Vaccine Coverage Region
        cur.execute("""
            SELECT c.region, ROUND(AVG(v.coverage), 2)
            FROM Vaccination v
            JOIN Country c ON c.CountryID = v.country
            GROUP BY c.region
            ORDER BY AVG(v.coverage) DESC
            LIMIT 1;
        """)
        row = cur.fetchone()
        cov_region = row[0] if row else "N/A"
        cov_value = row[1] if row else 0

        #  Region with Highest Infection
        cur.execute("""
            SELECT c.region, SUM(i.cases)
            FROM InfectionData i
            JOIN Country c ON c.CountryID = i.country
            GROUP BY c.region
            ORDER BY SUM(i.cases) DESC
            LIMIT 1;
        """)
        row = cur.fetchone()
        inf_region = row[0] if row else "N/A"
        inf_cases = row[1] if row else 0

        #  Average Coverage (all countries)
        cur.execute("SELECT ROUND(AVG(coverage), 2) FROM Vaccination;")
        avg_cov = cur.fetchone()[0] or 0

  
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<div class="logo">
    <img src="download.png" alt="">
</div>
<hr>
<div class="ctry">
 <h1 class="cnt">Country Count: {country_count}</h1>
 <h1 class="region">Coverage Region: {cov_region} ({cov_value}%)</h1>
 <h1 class="high">Region with Highest Infection: {inf_region} ({inf_cases:,} cases)</h1>
 <h1 class="Avg">Average Coverage: {avg_cov}%</h1>
</div>

<div class="Button">
 <div class="Flw">
  <a href="/page4" class="btn1">Flowchart</a>
 </div>
 <div class="Flw">
  <a href="/page2" class="btn1">Vaccination Data Summary</a>
 </div>
</div>

</body>
</html>

<style>
body {{
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  color: #f5f6f7;
  background: rgba(0,0,0,0.77) url(doc.jpg);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-blend-mode: darken;
}}

.logo {{
  width: 120px;
  margin: 22px auto 10px;
  background: #fff;
  padding: 8px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.25);
  text-align: center;
}}
.logo img {{
  width: 100%;
  height: auto;
}}

hr {{
  width: 80%;
  margin: 16px auto 22px;
  border: 0;
  height: 1px;
  background: #ffffff38;
}}

.ctry {{
  text-align: center;
  margin-top: 26px;
}}

.cnt, .region, .high, .Avg {{
  display: block;
  margin: 16px auto;
  padding: 18px 24px;
  width: 66%;
  max-width: 600px;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 700;
  color: #f8fafc;
  background: rgba(17, 24, 39, 0.65);
  border: 1px solid rgba(255,255,255,0.15);
  box-shadow: 0 3px 8px rgba(0,0,0,0.25);
  border-left: 4px solid transparent;
  transition: background 0.15s ease;
}}

.cnt   {{ border-left-color: #5aa7ff; border-right-color: rgb(209, 78, 78); }}
.region{{ border-left-color: #3bd0a0; border-right-color: rgb(86, 94, 203); }}
.high  {{ border-left-color: #f5a524; border-right-color: rgb(90, 222, 127); }}
.Avg   {{ border-left-color: #ef5b7b; border-right-color: rgb(226, 240, 78); }}

.cnt:hover, .region:hover, .high:hover, .Avg:hover {{
  background: rgba(17, 24, 39, 0.75);
}}

.Flw {{
  text-align: center;
  margin-top: 20px;
}}

.btn1 {{
  display: inline-block;
  padding: 10px 22px;
  border-radius: 8px;
  background: #e5e7eb;
  color: #0f172a;
  text-decoration: none;
  font-weight: 700;
  border: 1px solid #d1d5db;
  box-shadow: 0 3px 8px rgba(0,0,0,0.25);
  transition: background 0.12s ease, transform 0.12s ease;
}}
.btn1:hover {{
  background: skyblue;
  transform: translateY(-1px);
  transition: 0.5s;
}}
</style>
"""
    return page_html
