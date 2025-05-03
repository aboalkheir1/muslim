from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def qibla_finder():
    html_template = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>الداعي إلى الله - دليل القبلة</title>
        <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Rubik', sans-serif;
            }
            body {
                background-color: #f8f9fa;
                color: #333;
                line-height: 1.6;
            }
            .header {
                background: linear-gradient(135deg, #1e88e5, #0d47a1);
                color: white;
                padding: 1.2rem;
                text-align: center;
                font-size: 1.8rem;
                font-weight: 700;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                position: sticky;
                top: 0;
                z-index: 100;
            }
            .container {
                max-width: 1200px;
                margin: 1.5rem auto;
                padding: 0 1rem;
            }
            .iframe-container {
                position: relative;
                width: 100%;
                padding-bottom: 75%; /* Aspect ratio 4:3 */
                height: 0;
                overflow: hidden;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.1);
                background-color: white;
            }
            .iframe-container iframe {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: none;
            }
            .footer {
                text-align: center;
                margin: 1.5rem 0;
                color: #666;
                font-size: 0.9rem;
                padding: 0 1rem;
            }
            @media (max-width: 768px) {
                .header {
                    font-size: 1.4rem;
                    padding: 1rem;
                }
                .iframe-container {
                    padding-bottom: 100%; /* More square aspect ratio for mobile */
                }
            }
        </style>
    </head>
    <body>
        <div class="header">الداعي إلى الله</div>
        <div class="container">
            <div class="iframe-container">
                <iframe src="https://qiblafinder.withgoogle.com/intl/ar/onboarding" 
                        title="دليل القبلة من جوجل"
                        allow="geolocation *"></iframe>
            </div>
        </div>
        <div class="footer">
            دليل القبلة مقدمة من جوجل - ضمن مشروع الداعي إلى الله
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
