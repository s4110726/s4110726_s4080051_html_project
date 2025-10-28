def get_page_html(form_data):
    page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page 4</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: rgba(0,0,0,0.77) url('doc.jpg');
                background-size: cover;
                background-position: center;
                color: white;
                margin: 0;
                padding: 0;
                background-blend-mode: darken;
            }

            header, footer {
                background-color: rgba(0,0,0,0.6);
                text-align: center;
                padding: 15px 0;
            }

            header img {
                width: 150px;
                height: auto;
                border-radius: 10px;
            }

            .container {
                text-align: center;
                padding: 20px;
            }

            h1 {
                font-size: 36px;
                margin: 40px 0;
            }

            .section {
                display: flex;
                justify-content: space-around;
                align-items: center;
                margin: 60px 0;
                flex-wrap: wrap;
            }

            .chart-box img {
                width: 250px;
                height: 200px;
                object-fit: cover;
                border: 2px solid white;
                border-radius: 10px;
                background-color: rgba(255,255,255,0.1);
                position: relative;
                bottom: 50px;
            }

            button {
                background-color: transparent;
                border: 2px solid white;
                border-radius: 25px;
                padding: 10px 25px;
                font-size: 16px;
                color: white;
                cursor: pointer;
                transition: 0.3s;
                position: relative;
                top: 100px;
            }
            
            .btn1{
                display: inline-block;
                border-radius: 8px;
                background: #e5e7eb;
                color: #0f172a;
                text-decoration: none;
                font-weight: 700;
                border: 1px solid #d1d5db;
                box-shadow: 0 3px 8px rgba(0, 0, 0, 0.25);
                transition: background 0.12s 
                ease, transform 0.12s 
                ease;
                position: relative;
                right: 200px;
                bottom: 50px;    
            }

            button:hover {
                background-color: white;
                color: black;
            }

            h2 {
                font-size: 22px;
                margin-bottom: 15px;
            }

            .text-center {
                text-align: center;
                postion:relative;
                top:300px;
            }
            .rate_infection_name{
                position:relative;
                bottom: 120px;
                right: 180px;
            }
            .global_infection_name{
                position: relative;
                top: 300px;
                right: 300px;
            }
            .infection_chart{
                position:relative;
            }

            .global_chart{
            position:relative;
            top:200px;
            }

        </style>
    </head>
    <body>
        <header>
            <img src="World-Health-Organization-WHO-Logo.png" alt="Logo">
        </header>

       

            <div class="section">
                <div class="chart-box">
                    <div class="infection_chart">
                        <img src="rate_of_infection_chart.jpeg" alt="Rate of Infection Chart">
                    </div>
                </div>
                <div class="text-center">
                
                    <div class="rate_infection_name"><h2>Rate of Infection</h2></div>
                    <div class="button"><a href="/page5" class="btn1">VACCINATION RATE</a>
                </div>
            </div>

            <div class="section">
                <div class="text-center">
                    <div class="global_infection_name"><h2>Global Reported Infection</h2>
                    <button><div class="button"><a href="/page5" class="btn1">VACCINATION RATE</a></button>
                </div>
                <div class="global_chart">
                    <img src="global_rate_of_infection_chart.jpeg" alt="Global Infection Chart" width="300">
                </div>
            </div>
        
        
    </body>
    </html>
    """
    return page_html
