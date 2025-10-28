import pyhtml

def get_page_html(form_data):

    def pick(k):
        v = form_data.get(k)
        if isinstance(v, list) and v:
            v = v[0]
        if v is None:
            v = ""
        return str(v).strip()

    start   = pick("start_year")
    end     = pick("end_year")
    antigen = pick("antigen")
    topn    = pick("top_n")

    years    = pyhtml.get_results_from_query("immunisation.db", "SELECT DISTINCT year FROM Vaccination ORDER BY year;")
    antigens = pyhtml.get_results_from_query("immunisation.db", "SELECT AntigenID, name FROM Antigen ORDER BY name;")

    results = []

    if start and end and antigen:
        query = f"""
        SELECT 
            c.name AS Country,
            ROUND(v_start.coverage, 2) AS StartRate,
            ROUND(v_end.coverage, 2)   AS EndRate,
            ROUND(v_end.coverage - v_start.coverage, 2) AS Improvement
        FROM Country c
        JOIN Vaccination v_start 
            ON v_start.country = c.CountryID
        JOIN Vaccination v_end   
            ON v_end.country = c.CountryID 
            AND v_end.antigen = v_start.antigen
        WHERE 
            v_start.year = '{start}' 
            AND v_end.year = '{end}'
            AND v_start.antigen = '{antigen}' 
            AND v_end.antigen = '{antigen}'
        ORDER BY Improvement DESC
        """

        try:
            limit = int(topn)
            if limit > 0:
                query += f" LIMIT {limit}"
        except:
            pass

        query += ";"
        results = pyhtml.get_results_from_query("immunisation.db", query)

    # Dropdown options
    sy = '<option value="">Start Year</option>'
    for y in years:
        v = str(y[0])
        sel = " selected" if v == start else ""
        sy += f'<option value="{v}"{sel}>{v}</option>'

    ey = '<option value="">End Year</option>'
    for y in years:
        v = str(y[0])
        sel = " selected" if v == end else ""
        ey += f'<option value="{v}"{sel}>{v}</option>'

    ag = '<option value="">Select Antigen</option>'
    for a in antigens:
        v = str(a[0])
        t = str(a[1])
        sel = " selected" if v == antigen else ""
        ag += f'<option value="{v}"{sel}>{t}</option>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<title>Level 3 Deep Dive</title>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
    body {{
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
        background: rgba(0,0,0,0.75) url(doc.jpg) center/cover no-repeat fixed;
        color: #111;
        background-blend-mode: darken;
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
        margin: 20px 0;
        font-size: 22px;
        color: #fff;
        text-align: center;
        letter-spacing: 0.5px;
    }}
    .controls {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin: 20px 0 24px;
        justify-content: center;
    }}
    select, input {{
        padding: 8px 10px;
        border: 1px solid #bbb;
        background: #fff;
        color: #111;
        border-radius: 6px;
        min-width: 150px;
        font-size: 14px;
    }}
    button {{
        padding: 8px 14px;
        border: 1px solid #bbb;
        background: #2563eb;
        color: #fff;
        border-radius: 6px;
        font-weight: bold;
        cursor: pointer;
        transition: 0.3s;
    }}
    button:hover {{
        background: #1e4ed8;
    }}
    .tablewrap {{
        background: #fff;
        border: 1px solid #bbb;
        border-radius: 8px;
        margin-top: 20px;
        overflow-x: auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        background: #fff;
        color: #111;
    }}
    th, td {{
        border: 1px solid #bbb;
        padding: 10px;
        font-size: 14px;
        text-align: center;
    }}
    th {{
        background: #f3f4f6;
        font-weight: bold;
    }}
    tr:nth-child(even) td {{
        background: #fafafa;
    }}
    .Flw {{
        text-align: center;
        margin: 14px 0;
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
        transition: 0.3s;
    }}
    .btn1:hover {{
        background: skyblue;
    }}
</style>
</head>
<body>
    <div class="shell">
        <div class="Flw">
            <a href="/" class="btn1">Go Back to Home</a>
        </div>

        <div class="logo">
            <img src="download.png" width="100%">
        </div>

        <h1>Improvement</h1>

        <form method="get">
            <div class="controls">
                <select name="start_year">{sy}</select>
                <select name="end_year">{ey}</select>
                <select name="antigen">{ag}</select>
                <input type="number" name="top_n" placeholder="Country Count" value="{topn}">
                <button type="submit">Apply</button>
            </div>
        </form>

        <div class="tablewrap">
            <table>
                <tr>
                    <th>Country</th>
                    <th>Start Rate (%)</th>
                    <th>End Rate (%)</th>
                    <th>Improvement (%)</th>
                </tr>
"""
    if results:
        for r in results:
            html += f"<tr><td>{r[0]}</td><td>{r[1]:.2f}</td><td>{r[2]:.2f}</td><td>{r[3]:.2f}</td></tr>"
    else:
        html += '<tr><td colspan="4" style="text-align:center;">No data found</td></tr>'
    
    html += """
            </table>
        </div>
    </div>
</body>
</html>
"""
    return html
