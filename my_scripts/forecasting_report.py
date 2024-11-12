# forecasting_report.py
from fpdf import FPDF
import pandas as pd

def create_forecasting_report(predictions):
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="COVID-19 Forecasting Report", ln=True, align='C')

    pdf.cell(200, 10, txt="Predicted New Cases for Next 7 Days:", ln=True)
    
    for date, prediction in predictions:
        pdf.cell(200, 10, txt=f"{date}: {prediction:.2f}", ln=True)

    pdf.output("reports/forecasting_report.pdf")

def main():
    # Example predictions (replace with actual data)
    predictions = [('2024-09-25', 150), ('2024-09-26', 180), ('2024-09-27', 200)]
    create_forecasting_report(predictions)

if __name__ == '__main__':
    main()
