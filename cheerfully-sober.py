"""
Cheerfully Sober - BAC Calculator Application

A Blood Alcohol Content (BAC) calculator to estimate your BAC level
based on personal information and drinking patterns.
"""

from gui import BACCalculatorApp


def main():
    """Main entry point for the application"""
    app = BACCalculatorApp()
    app.run()


if __name__ == "__main__":
    main()
