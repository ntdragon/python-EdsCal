#!/bin/bash

# Generate html files from jhtml files
echo "Generating HTML pages for Desktop -----------------------------------------"
cd calendar.d
python3 html_try.py > ../html_pages.d/calendar.html
echo "--->  calendar generated"

cd ..
echo "Done! ------------------------------------------------------------------------  Done!"
