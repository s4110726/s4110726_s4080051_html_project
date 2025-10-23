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
                
            }

        </style>
    </head>
    <body>
        <header>
            <img src="download.png" alt="Logo">
        </header>

       

            <div class="section">
                <div class="chart-box">
                    <img src="Rate of infection.jpeg" alt="Rate of Infection Chart">
                </div>
                <div class="text-center">
                    <h2>Rate of Infection</h2>
                    <button>Button</button>
                </div>
            </div>

            <div class="section">
                <div class="text-center">
                    <h2>Global Reported Infection</h2>
                    <button>Button</button>
                </div>
                <div class="chart-box">
                    <img src="Global infection.jpeg" alt="Global Infection Chart">
                </div>
            </div>
        
        
    </body>
    </html>
    """
    return page_html
